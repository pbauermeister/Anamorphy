"""
This module subclasses AutogeneratedMainFrame from the
autogenerated_GUI.py module (which should never be editted manually,
because, as the name suggests, it is auto-generated, by wxGlade).

It implements all GUI-related actions and validations, as well as
instantiates the dialogs and call the wxWidgets event loop.
"""

import threading
import Queue
import wx
import time
import math
import tempfile
import subprocess
import os
import os.path
import sys
import traceback
import wx.lib.imagebrowser as imagebrowser

from autogenerated_GUI import AutogeneratedMainFrame
from wizard import WizardFrame
import perspective
import shape
from display_wx import PaintDisplay
import config_wx
import config
from anamorphosis import Anamorphosis
import geometry
import bitmap
import pdf
from PIL import Image
import undo
import exporters
import printing
import myapp
import constants
import version

PAPER_SIZES_MM = {
            # http://en.wikipedia.org/wiki/A4_paper#A_series
            "a3": (297, 420),
            "a4": (210, 297),
            "a5": (148, 210),
            # http://en.wikipedia.org/wiki/Letter_%28paper_size%29
            "letter": (216, 279),
            "a3 landscape": (420, 297),
            "a4 landscape": (297, 210),
            "a5 landscape": (210, 148),
            "letter landscape": (279, 216),
            }


class MainFrame(AutogeneratedMainFrame):
    """This class overrides the autogenerated frame generated by wxGlade"""

    def __init__(self, filename, defaults, scene):
        super(MainFrame, self).__init__(None, -1, "")

        # this fixes weird BG color on Windows
        if os.name == "nt":
            self.SetBackgroundColour(wx.Colour(225, 225, 225))

        # restore config
        self._config = config_wx.Config()
        conf = self._config
        load_from = filename or self._config.last_saved
        values = config.load(load_from)
        if filename is not None and values:
            self._config.last_saved = filename
            self._config.save()
        if not values:
            self._config.last_saved = None
            self._config.save()

        # undo/redo
        self.undo = undo.Undo()
        self.setUndoMenu()

        # restore main frame
        if conf.checkGeometry():
            self.SetPosition((conf.pos_x, conf.pos_y))
            self.SetSize((conf.pos_w, conf.pos_h))

        # key events
        self.recursivelySetKeyEvent(self)
        self.window_anamorphosis.SetFocus()

        # mouse support
        self.window_perspective.Bind(wx.EVT_LEFT_DOWN, self.OnMouseClick)
        self.window_perspective.Bind(wx.EVT_LEFT_UP, self.OnMouseRelease)
        self.window_perspective.Bind(wx.EVT_MOTION, self.OnMouseMove)
        self.window_perspective.Bind(wx.EVT_MOUSEWHEEL, self.OnMouseWheel)
        self.click_pos = None

        self.defaults = defaults

        # camera and scene, and values
        self.scene = scene
        self.applyValues(values)

        # bind events
        self.Bind(wx.EVT_CLOSE, self.OnCloseFrame)
        self.window_perspective.Bind(wx.EVT_PAINT, self.OnPaintPersp)
        self.window_perspective.Bind(wx.EVT_SIZE, self.OnSizePersp)
        self.window_anamorphosis.Bind(wx.EVT_PAINT, self.OnPaintAnam)
        self.window_anamorphosis.Bind(wx.EVT_SIZE, self.OnSizeAnam)

        # misc
        self.updateCardFormatMenu()
        self.ctrl_pressed = False
        self.shift_pressed = False
        self.updateHint()
        self.anamorphosis = None

        self.frames_p = 0
        self.frames_a = 0
        self.queue = Queue.Queue()
        # start the thread for deferred anamorphosis redraw
        myapp.RequestRedrawThread(self.queue,
                                  self.redrawAnamorphosisNow).start()

    #
    # State helpers
    #

    def handleChanges(self, dirty=True):
        if not dirty:
            self.undo.fixup(lambda x: [True, x[1]])
        self.dirty = dirty
        item = [self.dirty, self.values]
        self.undo.add(item)
        self.updateState()

    def updateState(self):
        self.setTitle()
        self.setUndoMenu()
        self.refresh()

    #
    # Controls & values helpers
    #

    def applyValues(self, values):
        self.title = None

        # populate controls
        self.values = values
        self.refreshControls()

        dlg = wx.ProgressDialog("Working...", "Loading images...",
                                parent=self,
                                style=wx.PD_APP_MODAL | wx.PD_SMOOTH)
        # marquee
        self.marquee_ratio = 1
        self.marquee_bmp = None
        print "Loading marquee..."
        self.loadMarquee(progress_dlg=dlg)

        # card BG
        self.card_bg_bmp = None
        if self.getValue("card_background_show"):
            print "Loading card bg..."
            self.loadCardBg(progress_dlg=dlg)

        dlg.Destroy()
        self.handleChanges(dirty=False)

    def getValue(self, name):
        default = self.defaults[name]
        val = self.values.get(name, default)
        if val in (None, ""):
            val = default
        #print name, default, "->", val
        return val

    def setValue(self, name, value):
        if name in self.values and self.values[name] == value:
            return
        self.values[name] = value
        self.handleChanges()

    def setNumVal(self, name, val):
        ctrl = eval("self.spin_ctrl_%s" % name)
        val = min(val, ctrl.GetMax())
        val = max(val, ctrl.GetMin())
        ctrl.SetValue(val)
        self.setValue(name, val)

    def setNumFromSpin(self, name):
        val = eval("self.spin_ctrl_%s.GetValue()" % name)
        self.setNumVal(name, val)

    def initNum(self, name):
        val = self.values.get(name, self.defaults[name])
        self.setNumVal(name, val)

    def refreshControls(self):
        self.initNum("camera_azimuth")
        self.initNum("camera_altitude")
        self.initNum("camera_distance")
        self.initNum("camera_fov")

        self.initNum("card_width")
        self.initNum("card_height")
        self.initNum("card_angle")
        self.initNum("card_elevation")
        self.choice_card_fold.SetSelection(self.getValue("card_fold"))

        self.text_ctrl_marquee_image.SetValue(self.getValue("marquee_image"))
        self.checkbox_marquee_show.SetValue(self.getValue("marquee_show"))
        self.initNum("marquee_width")
        self.initNum("marquee_distance")
        self.initNum("marquee_voff")
        self.initNum("marquee_hoff")

        self.initNum("export_bitmap_width")
        self.initNum("export_bitmap_height")

        self.text_ctrl_card_image.SetValue(self.getValue("card_background"))
        self.checkbox_card_background.SetValue(self.getValue(
                "card_background_show"))
        self.updateCardBackground()
        # units_length

    def updateCardBackground(self):
        show = self.getValue("card_background_show")
        self.text_ctrl_card_image.Enable(show)
        self.button_card_filename.Enable(show)

    def setCardBackground(self, path):
        self.values["card_background"] = path
        self.text_ctrl_card_image.SetValue(path)
        self.values["card_background_show"] = True
        self.checkbox_card_background.SetValue(True)
        self.loadCardBg()
        self.handleChanges()

    def endEdits(self):
        # call me upon menu/hotkey actions, to exit focus from any
        # input widgets, so as to finish any editing session and
        # update value prior said action
        self.window_perspective.SetFocus()
        wx.Yield()

    #
    # GUI helpers
    #

    def setTitle(self):
        filename = self._config.last_saved
        if filename:
            d, name = os.path.split(filename)
        else:
            name = "no name"

        title = "*" if self.dirty else ""
        title += "%s - Anamorphy" % name
        if title != self.title:
            self.title = title
            self.SetTitle(title)

    def recursivelySetKeyEvent(self, what):
        for c in what.GetChildren():
            self.recursivelySetKeyEvent(c)
        what.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        what.Bind(wx.EVT_KEY_UP, self.OnKeyUp)

    def updateHint(self):
        if self.shift_pressed:
            l = " (locked along axis)"
        else:
            l = ""
        if self.ctrl_pressed:
            dtext = "Drag: marquee offset%s" % l
        else:
            dtext = "Drag: camera angle%s" % l

        if self.shift_pressed:
            wtext = "Wheel: card fold angle"
        elif self.ctrl_pressed:
            wtext = "Wheel: marquee distance"
        else:
            wtext = "Wheel: camera distance"

        text = wtext + " " * 10 + dtext
        self.label_hint.SetLabel(text)

    def setUndoMenu(self):
        self.menu_undo.Enable(self.undo.canUndo())
        self.menu_redo.Enable(self.undo.canRedo())

    def updateCardFormatMenu(self):
        name, dim = self.getCardFormat()
        i = 0
        for s in self.choice_card_format.GetStrings():
            choice = s.strip("[]")
            if choice.lower() == name:
                choice = "[%s]" % choice
            self.choice_card_format.SetString(i, choice)
            i += 1
        self.choice_card_format.SetSelection(0)

    def setMarqueeImage(self, path):
        self.values["marquee_image"] = path
        self.text_ctrl_marquee_image.SetValue(path)
        self.values["marquee_show"] = True
        self.checkbox_marquee_show.SetValue(True)
        self.loadMarquee()
        self.handleChanges()

    def callWizard(self, values, full, new):
        # show wizard
        w = WizardFrame(self, full)
        w.ShowModal()
        w.Destroy()
        if w.settings is None:
            return

        self.values = values
        if new:
            self._config.last_saved = None

        # copy returned settings to ours
        for k, v in w.settings.items():
            self.values[k] = v
        self.refreshControls()

        # load image
        path = self.getValue("marquee_image")
        self.setMarqueeImage(path)

        if new:
            self.dirty = False
            self.setTitle()

    #
    # Canvas & rendering helpers
    #

    def refresh(self):
        self.redraw(None)

    def redraw(self, arg):
        self.window_perspective.Refresh()

    def render(self, canvas):
        pdc = wx.PaintDC(canvas)  # simple device context
        dc = wx.GCDC(pdc)  # device context with alpha and anti-alias
        w, h = canvas.GetClientSize()
        display = PaintDisplay(dc, w, h)
        display.setScale(15, 15)

        # camera pos
        theta = math.radians(90 - self.getValue("camera_altitude"))
        phi = math.radians(90 - self.getValue("camera_azimuth"))
        r = self.getValue("camera_distance")
        y = r * math.cos(theta)
        x = r * math.cos(phi) * math.sin(theta)
        z = r * math.sin(phi) * math.sin(theta)
        pos = "x:%d  y:%d  z:%d" % (x, y, z)
        self.label_camera_pos.SetLabel(pos)

        # compute perspective
        persp = perspective.Perspective(
            self.getValue("camera_azimuth"),
            self.getValue("camera_altitude"),
            self.getValue("camera_distance"),
            self.getValue("camera_fov"))

        # compute scene
        self.scene.setCard(
            self.getValue("card_width"),
            self.getValue("card_height"),
            self.getValue("card_fold"),
            self.getValue("card_angle"),
            self.getValue("card_elevation"),
            self.card_bg_bmp if self.getValue("card_background_show") else None
            )
        self.scene.setMarquee(
            persp.getCameraRotateMatrix(),
            self.getValue("camera_distance"),
            self.getValue("marquee_width"),
            self.getValue("marquee_width") * self.marquee_ratio,
            self.getValue("marquee_distance"),
            self.getValue("marquee_hoff"),
            self.getValue("marquee_voff")
            )
        self.scene.setCameraPos(persp.getCamera())
        self.scene.setMarqueeTiles(5, 5)

        # compute 3D -> 2D
        shapes = self.scene.getShapes()
        marquee_show = self.getValue("marquee_show")
        for each in shapes:
            if each is None:
                continue
            if marquee_show:
                show = each.name not in ("marquee", "CBP", "CFP")
            else:
                show = True
            try:
                each.render(display, persp, show=show)
            except ValueError, e:
                traceback.print_exc()
                print e
                pass  # some point cannot be rendered
            except OverflowError, e:
                traceback.print_exc()
                print e
                pass  # some point cannot be rendered

        # render marquee image
        if self.getValue("marquee_show") and self.marquee_bmp is not None:
            marquee_2d_points = shape.getShape("marquee").get2dPoints()
            (x, y), w, h = geometry.boundingRect(marquee_2d_points)

            bmp = self.marquee_bmp.getScaled(w, h)
            display.DrawBitmap(bmp, x, y)

        # draw 2D anamorphosis
        if self.marquee_bmp is not None:
            self.anamorphosis = Anamorphosis(self.getValue("marquee_show"),
                                             self.marquee_bmp)

        self.frames_p += 1
        #print "P frames:", self.frames_p
        self.redrawAnamorphosis()

    def redrawAnamorphosis(self):
        if self.getValue("marquee_show"):
            # time-consuming -> schedule to be redrawn when quiet
            self.queue.put(True)
        else:
            # only gridline -> refresh in real-time
            self.redrawAnamorphosisNow()

    def redrawAnamorphosisNow(self):
        self.window_anamorphosis.Refresh()

    #
    # Image loading helpers
    #

    def loadMarquee(self, progress_dlg=None):
        name = self.getValue("marquee_image")
        bmp = self.loadImage(name, "Loading marquee image", progress_dlg)
        self.marquee_bmp = bmp
        if bmp is not None:
            w, h = bmp.getWidth(), bmp.getHeight()
            ratio = float(h) / float(w)
            self.marquee_ratio = ratio
            self.marquee_size = w, h

    def loadCardBg(self, progress_dlg=None):
        name = self.getValue("card_background")
        if name:
            bmp = self.loadImage(name, "Loading BG image", progress_dlg)
            self.card_bg_bmp = bmp

    def loadImage(self, file_name, message, progress_dlg):
        if progress_dlg is None:
            dlg = wx.ProgressDialog("Working...", message,
                                    parent=self,
                                    style=wx.PD_APP_MODAL | wx.PD_SMOOTH)
        else:
            dlg = progress_dlg
        size = wx.Size()
        size.SetWidth(300)
        dlg.SetSize(size)
        wx.Yield()
        wx.MilliSleep(10)

        def updateProgress(s):
            dlg.Pulse("%s: %s" % (message, s))
            wx.Yield()
        try:
            bmp = bitmap.makeFromFile(file_name, updateProgress)
            bmp.getPilThumb()  # to cache, while progress dlg is here
            bmp.resetProgressFn()
        except Exception, e:
            traceback.print_exc()
            print e
            bmp = None
        if progress_dlg is None:
            dlg.Destroy()
        if bmp is None:
            wx.MessageDialog(self, "Error loading image\n%s" % file_name,
                             style=wx.OK).ShowModal()
        return bmp

    #
    # Lifetime helpers
    #

    def closeNow(self):
        self.queue.put(None)

        # store config
        # - main frame
        pos = self.GetPosition()
        self._config.pos_x = pos[0]
        self._config.pos_y = pos[1]

        size = self.GetSize()
        self._config.pos_w = size[0]
        self._config.pos_h = size[1]

        self._config.save()

        # close WX stuff
        self.Destroy()

    #
    # Data helpers
    #
    def getCardFormat(self):
        cw = self.getValue("card_width")
        ch = self.getValue("card_height")
        dim = (cw, ch)
        # TODO: if dim is in inches, convert and round to mm
        name = None
        for k, v in PAPER_SIZES_MM.items():
            if v == dim:
                name = k.lower()
                break
        return name, dim

    def makePageParams(self):
        self.setNumFromSpin("export_bitmap_height")
        cw = self.getValue("card_width")
        ch = self.getValue("card_height")
        bmh = self.getValue("export_bitmap_height")
        bmw = (bmh * cw) / ch
        self.setNumVal("export_bitmap_width", bmw)

        name, paper_dim_mm = self.getCardFormat()
        w_mm, h_mm = paper_dim_mm

        dpi = 100
        if name:
            name, orientation = (name + " x").lower().split()[:2]
            is_landscape = orientation == "landscape"

            w, h = pdf.getBitmapSize(name, dpi, is_landscape)
        else:
            f = 0.0393701
            w_inch, h_inch = w_mm * f, h_mm * f
            i2d = lambda x: int(x * dpi + 0.5)
            w, h = i2d(w_inch), i2d(h_inch)

        return w, h, w_mm, h_mm

    #
    # File & project helpers
    #

    def saveAs(self):
        path = self._config.last_saved
        if path is not None:
            d, f = os.path.split(path)
        else:
            d, f = "", ""
        saveFileDialog = wx.FileDialog(self, "Save Project", d, f,
                                       "*" + constants.EXTENSION,
                                       wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if saveFileDialog.ShowModal() == wx.ID_CANCEL:
            saved = False
        else:
            filename = saveFileDialog.GetPath()
            filename = myapp.fixPath(filename, constants.EXTENSION)
            self._config.last_saved = filename
            self.save()

            saved = True
        saveFileDialog.Destroy()
        return saved

    def save(self):
        if self._config.last_saved is None:
            return self.saveAs()
        else:
            config.save(self._config.last_saved, self.values)
            self.undo.undo()  # unstack last change
            self.handleChanges(dirty=False)  # will stack current values
            return True

    def saveIfNeeded(self, text):
        if self.dirty:
            flags = wx.YES_NO | wx.CANCEL | wx.CENTRE | wx.ICON_QUESTION
            ok = wx.MessageBox(text, _("Unsaved changes"), flags)
            if ok == wx.YES:
                if not self.save():
                    return False
                else:
                    return True
            elif ok == wx.CANCEL:
                return False
            elif ok == wx.NO:
                return True
        return True

    def openFile(self, filename):
        if not self.saveIfNeeded(
            _("Save project before opening %s?" % filename)):
            return
        self.loadFile(filename)

    def new(self):
        if not self.saveIfNeeded(_("Save project before creating new one?")):
            return
        self.callWizard({}, full=True, new=True)

    def printProject(self):
        img_w, img_h, pdf_w_mm, pdf_h_mm = self.makePageParams()

        dlg = wx.ProgressDialog("Working...", "Generating PDF for printing...",
                                parent=self,
                                style=wx.PD_APP_MODAL | wx.PD_SMOOTH)

        def update_fn(msg):
            dlg.Pulse(msg)
            wx.Yield()

        def done_fn(msg):
            dlg.Destroy()
            wx.Yield()

        printing.printPdf(self.anamorphosis.renderImage, update_fn, done_fn,
                          img_w, img_h, pdf_w_mm, pdf_h_mm)

    def loadFile(self, filename):
        values = config.load(filename)
        if values:
            self.values = values
            self._config.last_saved = filename
            self.applyValues(values)
            return True
        else:
            return False

    def dropFiles(self, paths):
        f = paths[0]
        if f.lower().endswith(constants.EXTENSION):
            # project file
            if not self.saveIfNeeded(_("Save project before opening %s?" % f)):
                return
            if self.loadFile(f):
                return
        else:
            # try image file
            try:
                Image.open(f)
            except:
                dlg = wx.MessageDialog(self, _("Unrecognized file format."),
                                       _("Error"), wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
                return
            self.setMarqueeImage(f)
            return

    #
    # Manually bound handlers
    #

    def OnCloseFrame(self, event):
        if not self.saveIfNeeded(_("Save project before closing?")):
            return
        self.closeNow()

    def OnKeyUp(self, event):
        self.OnKey(event, False)

    def OnKeyDown(self, event):
        self.OnKey(event, True)

    def OnKey(self, event, pressed):
        code = event.GetKeyCode()
        if code == wx.WXK_SHIFT:
            self.shift_pressed = pressed
            self.updateHint()
        elif code == wx.WXK_CONTROL:
            self.ctrl_pressed = pressed
            self.updateHint()
        event.Skip()

    def OnMouseClick(self, event):
        self.click_pos = event.GetX(), event.GetY()
        self.click_azimuth = self.getValue("camera_azimuth")
        self.click_altitude = self.getValue("camera_altitude")
        self.click_hoff = self.getValue("marquee_hoff")
        self.click_voff = self.getValue("marquee_voff")
        self.click_ctrl = event.ControlDown()

    def OnMouseRelease(self, event):
        self.click_pos = None
        self.handleChanges()

    def OnMouseMove(self, event):
        if self.click_pos is None:
            return
        # determine drag size
        dx = -event.GetX() + self.click_pos[0]
        dy = +event.GetY() - self.click_pos[1]
        if event.ShiftDown():
            # lock one direction
            if abs(dx) > abs(dy):
                dy = 0
            else:
                dx = 0
        w, h = self.window_perspective.GetClientSize()

        self.undo.enable(False)

        if self.click_ctrl:
            # move marquee
            d = self.getValue("marquee_distance") / 3
            mh = self.click_hoff - dx / (w / d)
            mv = self.click_voff - dy / (h / d)
            self.setNumVal("marquee_hoff", mh)
            self.setNumVal("marquee_voff", mv)
        else:
            # move card
            daz = (dx * 360) / w
            dal = (dy * 90) / h
            az = self.click_azimuth + daz
            az = max(min(az, 180), 0)
            al = self.click_altitude + dal
            self.setNumVal("camera_azimuth", az)
            self.setNumVal("camera_altitude", al)

        self.undo.enable(True)
        self.handleChanges()
        #self.updateState()

    def OnMouseWheel(self, event):
        if event.WheelRotation > 0:
            direction = -1
        else:
            direction = 1

        if event.ShiftDown():
            angle = self.getValue("card_angle")
            self.setNumVal("card_angle", angle + direction * 5)
        elif event.ControlDown():
            dist = self.getValue("marquee_distance")
            self.setNumVal("marquee_distance", dist + direction * 5)
        else:
            dist = self.getValue("camera_distance")
            self.setNumVal("camera_distance", dist + direction * 5)

    def OnPaintPersp(self, event):
        canvas = self.window_perspective
        self.render(canvas)

    def OnSizePersp(self, event):
        canvas = self.window_perspective
        canvas.Refresh()

    def OnPaintAnam(self, event):
        canvas = self.window_anamorphosis
        if self.anamorphosis is not None:
            self.anamorphosis.renderCanvas(canvas)
            self.frames_a += 1
            #print "A frames:", self.frames_a
            #self.anamorphosis = None

    def OnSizeAnam(self, event):
        #canvas = self.window_anamorphosis
        #wx.PaintDC(canvas).Clear()
        self.queue.put(True)

    #
    # Handler bound by wxglade
    #

    def OnCameraAltitudeSpin(self, event):
        self.setNumFromSpin("camera_altitude")

    def OnCameraAzimuthSpin(self, event):
        self.setNumFromSpin("camera_azimuth")

    def OnCameraDistanceSpin(self, event):
        self.setNumFromSpin("camera_distance")

    def OnCameraFovSpin(self, event):
        self.setNumFromSpin("camera_fov")

    def OnCardAngleSpin(self, event):
        self.setNumFromSpin("card_angle")

    def OnCardBackgroundCheck(self, event):
        show = self.checkbox_card_background.GetValue()
        self.values["card_background_show"] = show
        self.updateCardBackground()
        if show:
            self.values["card_background"] = \
                self.text_ctrl_card_image.GetValue()
            self.loadCardBg()
        self.handleChanges()

    def OnCardBackgroundChoose(self, event):
        parent = os.path.split(self.getValue("card_background"))[0]
        dlg = imagebrowser.ImageDialog(self, parent)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetFile()
            self.setCardBackground(path)
        dlg.Destroy()

    def OnCardBackgroundImage(self, event=None):
        path = self.text_ctrl_card_image.GetValue()
        self.values["card_background"] = path
        self.checkbox_card_background.SetValue(False)

    def OnCardElevationSpin(self, event):
        self.setNumFromSpin("card_elevation")

    def OnCardFoldChoice(self, event):
        sel = self.choice_card_fold.GetSelection()
        self.values["card_fold"] = sel
        self.handleChanges()

    def OnCardFormatChoice(self, event):
        name = self.choice_card_format.GetStringSelection().lower()
        name = name.strip("[]")
        size = PAPER_SIZES_MM.get(name, None)
        if size is None:
            return
        w, h = size  # rot 90 for fold
        self.setNumVal("card_width", w)
        self.setNumVal("card_height", h)
        self.choice_card_format.SetSelection(0)
        self.OnExportBitmapWidthSpin(event)
        self.updateCardFormatMenu()
        self.handleChanges()

    def OnCardHeightSpin(self, event):
        self.setNumFromSpin("card_height")
        self.updateCardFormatMenu()

    def OnCardWidthSpin(self, event):
        self.setNumFromSpin("card_width")
        self.updateCardFormatMenu()

    def OnExportBitmapWidthSpin(self, event):
        self.setNumFromSpin("export_bitmap_width")
        cw = self.getValue("card_width")
        ch = self.getValue("card_height")
        bmw = self.getValue("export_bitmap_width")
        bmh = (bmw * ch) / cw
        self.setNumVal("export_bitmap_height", bmh)

    def OnExportImageClicked(self, event):
        h = self.getValue("export_bitmap_height")
        w = self.getValue("export_bitmap_width")

        path = self.getValue("export_bitmap") or ""
        d, f = os.path.split(path)
        saveFileDialog = wx.FileDialog(self, "Save Image", d, f,
                                       "PNG files (*.png)|*.png",
                                       wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        self.button_export_image.Enable(False)
        res = saveFileDialog.ShowModal()
        name = saveFileDialog.GetPath()
        saveFileDialog.Destroy()
        if res != wx.ID_CANCEL:
            name = myapp.fixPath(name, ".png")
            self.setValue("export_bitmap", name)

            dlg = wx.ProgressDialog("Working...", "Saving image...",
                                    parent=self, maximum=100,
                                    style=wx.PD_APP_MODAL | wx.PD_SMOOTH |
                                    wx.PD_AUTO_HIDE)

            def updater(pcent):
                dlg.Update(pcent)

            exp = exporters.ImageExporter(self.anamorphosis.renderImage, w, h,
                                          updater)
            exp.generate()
            exp.save(name)

            updater(100)
            dlg.Destroy()

        self.button_export_image.Enable(True)
        return

    def OnExportPdfClicked(self, event):
        w, h, w_mm, h_mm = self.makePageParams()

        path = self.getValue("export_pdf") or ""
        d, f = os.path.split(path)
        saveFileDialog = wx.FileDialog(self, "Save PDF", d, f,
                                       "PDF files (*.pdf)|*.pdf",
                                       wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        self.button_export_pdf.Enable(False)
        res = saveFileDialog.ShowModal()
        name = saveFileDialog.GetPath()
        saveFileDialog.Destroy()
        if res != wx.ID_CANCEL:
            name = myapp.fixPath(name, ".pdf")
            self.setValue("export_pdf", name)

            dlg = wx.ProgressDialog("Working...", "Saving PDF...",
                                    parent=self,
                                    style=wx.PD_APP_MODAL | wx.PD_SMOOTH |
                                    wx.PD_AUTO_HIDE)

            def updater(pcent):
                dlg.Update(pcent)

            exp = exporters.PdfExporter(self.anamorphosis.renderImage,
                                        w, h, w_mm, h_mm, updater)
            exp.generate()
            exp.save(name)

            updater(100)
            dlg.Destroy()

        self.button_export_pdf.Enable(True)
        return

    def OnMarqueeChoose(self, event):
        parent = os.path.split(self.getValue("marquee_image"))[0]
        #dlg = ib.ImageDialog(self, "Choose an image",
        #                    defaultFile=self.getValue("marquee_image"))
        dlg = imagebrowser.ImageDialog(self, parent)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetFile()
            self.setMarqueeImage(path)
        dlg.Destroy()

    def OnMarqueeDistanceSpin(self, event):
        self.setNumFromSpin("marquee_distance")

    def OnMarqueeHOffSpin(self, event):
        self.setNumFromSpin("marquee_hoff")

    def OnMarqueeImage(self, event=None):
        path = self.text_ctrl_marquee_image.GetValue()
        self.values["marquee_image"] = path
        self.checkbox_marquee_show.SetValue(False)

    def OnMarqueeShowCheck(self, event):
        show = self.checkbox_marquee_show.GetValue()
        self.values["marquee_show"] = show
        if show:
            im = self.text_ctrl_marquee_image.GetValue()
            self.values["marquee_image"] = im
            self.loadMarquee()
        self.handleChanges()

    def OnMarqueeImageDrop(self, paths):
        self.setMarqueeImage(paths[0])

    def OnMarqueeWidthSpin(self, event):
        self.setNumFromSpin("marquee_width")

    def OnMarqueeVOffSpin(self, event):
        self.setNumFromSpin("marquee_voff")

    def OnMenuAbout(self, event):
        info = wx.AboutDialogInfo()

        description = _("""\
Anamorphy lets you create anamorphosis images.

An anamorphosis is a drawing mapped on a surface, and
sheared in such a way that, when seen from a well-defined
location, it appears as not deformed, but floating in front of
the surface.  For more information look for 'Anamorphosis'
on Wikipedia.

Outputs of this program can be printed as simple or folded
cards, or can be used to paint anamorphosis on buildings,
boxes or on the floor.

This progam is dedicated to the Instructables.com community.""")

        licence = _("""\
Anamorphy is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.

Anamorphy is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details. You should have received a
copy of the GNU General Public License along with Anamorphy; if not,
write to the Free Software Foundation, Inc., 59 Temple Place, Suite
330, Boston, MA 02111-1307 USA""")

        info.SetIcon(wx.Icon('logo64.png', wx.BITMAP_TYPE_PNG))
        info.SetName('Anamorphy')
        info.SetVersion(version.getVersion())
        info.SetDescription(description)
        info.SetCopyright(_('(C) Copyright 2013 by Pascal Bauermeister'))
        info.SetWebSite('http://www.instructables.com/id/Anamorphy')
        info.SetLicence(licence)
        info.AddDeveloper('Pascal Bauermeister')
        info.AddDocWriter('Pascal Bauermeister')
        #info.AddArtist('Pascal Bauermeister')
        #info.AddTranslator('Pascal Bauermeister')
        wx.AboutBox(info)

    def OnMenuHelp(self, event):
        if sys.platform.startswith('darwin'):
            subprocess.call(('open', 'README.html'))
        elif os.name == 'nt':
            os.startfile('README.html')
        elif os.name == 'posix':
            subprocess.call(('xdg-open', 'README.html'))

    def OnMenuNew(self, event):
        self.endEdits()
        self.new()

    def OnMenuOpen(self, event):
        self.endEdits()
        if not self.saveIfNeeded(_("Save project before opening one?")):
            return

        path = self._config.last_saved
        if path is not None:
            d, f = os.path.split(path)
        else:
            d, f = "", ""

        openFileDialog = wx.FileDialog(self, "Open Project", d, f,
                                       "*" + constants.EXTENSION,
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() != wx.ID_CANCEL:
            filename = openFileDialog.GetPath()
            self.loadFile(filename)
        openFileDialog.Destroy()

    def OnMenuPrint(self, event):
        self.endEdits()
        self.printProject()

    def OnMenuQuit(self, event):
        self.endEdits()
        self.OnCloseFrame(event)

    def OnMenuRedo(self, event):
        self.endEdits()
        if self.undo.canRedo():
            res = self.undo.redo()
            if res is not None:
                self.dirty, self.values = res
                self.refreshControls()
                self.updateState()

    def OnMenuUndo(self, event):
        self.endEdits()
        if self.undo.canUndo():
            res = self.undo.undo()
            if res is not None:
                self.dirty, self.values = res
                self.refreshControls()
                self.updateState()

    def OnMenuSave(self, event):
        self.endEdits()
        self.save()

    def OnMenuSaveAs(self, event):
        self.endEdits()
        self.saveAs()

    def OnPresetWizardClicked(self, event):
        self.endEdits()
        self.callWizard(self.values, full=False, new=False)

    def OnShowFullscreenClicked(self, event):
        self.endEdits()
        self.anamorphosis.renderScreen(self)

    def OnUnitsLengthChoice(self, event):
        XXX
