"""
This module launches the WX App.

It then uses the module GUI to build the dialogs and frames.
"""
import sys
import wx
import threading
import time

from GUI import MainFrame
import constants
import subprocess
import gettext

class DropTarget(wx.FileDropTarget):
    """Class to implement a file drag-n-drop target"""

    def __init__(self, frame, handler):
        # Initialize the wxFileDropTarget Object
        wx.FileDropTarget.__init__(self)
        # Store the Object Reference for dropped files
        self.frame = frame
        self.handler = handler

    def OnDropFiles(self, x, y, filenames):
        """ Implement File Drop """
        self.handler(filenames)


def fixPath(name, suffix):
    if name.lower().endswith(suffix.lower()):
        return name
    else:
        return name + suffix


class RequestRedrawThread(threading.Thread):
    """
    This thread calls the redraw of the anamorphosis image when
    "things are quiet":

    Upon refresh requests, the GUI thread should post events in the
    queue to say "I would like a refresh". This thread reads the
    queue, and for each event, peeks if the queue is not empty
    (meaning "there are more requests after this one"). Then, it calls
    the GUI for actual redraw only when the queue is empty (meaning
    "last event in the series, things have become more quiet").
    """
    def __init__(self, queue, fn):
        threading.Thread.__init__(self)
        self.queue = queue
        self.fn = fn
        self.daemon = True

    def run(self):
        queue = self.queue
        while True:
            item = queue.get()
            if item is None:
                return  # end thread
            if queue.empty():
                # skip fast events
                time.sleep(constants.DEFERRED_REDRAW_DELAY)
            if queue.empty():
                wx.CallAfter(self.fn)
            queue.task_done()


def setDropTargets(target, frame, handler):
    if hasattr(target, "SetDropTarget"):
        dt = DropTarget(frame, handler)
        target.SetDropTarget(dt)
    if hasattr(target, "Children"):
        for child in target.Children:
            setDropTargets(child, frame, handler)


class MyApp(wx.App):
    """
    This class subclasses wx.App, mainly to:
    - create the frame in OnInit() with needed parameters,
    - get all system and OSX events.
    """

    def __init__(self, defaults, scene):
        self.defaults = defaults
        self.scene = scene

        wx.App.__init__(self, redirect=False)

        # This catches events when the app is asked to activate by some other
        # process
        self.Bind(wx.EVT_ACTIVATE_APP, self.OnActivate)

    def OnInit(self):
        print "> OnInit called"
        return True
    
    def initApp(self):
        # project file given as arg
        filename = None  # TODO: from args
        for f in  sys.argv[1:]:
            filename = f
            break

        # main frame
        frame = MainFrame(filename, self.defaults, self.scene)
        self.frame = frame
        self.SetTopWindow(frame)
        frame.Show()

        # drop target
        setDropTargets(frame, frame, frame.dropFiles)

        # done
        return True

    def BringWindowToFront(self):
        print "> BringWindowToFront called"
        try:  # it's possible for this event to come when the frame is
              # closed
            self.GetTopWindow().Raise()
        except:
            pass

    def OnActivate(self, event):
        print "> OnActivate called", event.GetActive()
        # if this is an activate event, rather than something else,
        # like iconize.
        if event.GetActive():
            #self.BringWindowToFront()
            pass
        event.Skip()

    def OpenFileMessage(self, filename):
        self.frame.openFile(filename)

    def message(self, message, title="Info"):
        dlg = wx.MessageDialog(None, message, title,
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def MacOpenFile(self, filename):
        """
        Called for files droped on dock icon, or opened via finders
        context menu
        """
        self.frame.openFile(filename)
        self.OpenFileMessage(filename)

    def MacReopenApp(self):
        """Called when the doc icon is clicked, and ???"""
        print "> MacReopenApp called"
        #self.message("<MacReopenApp>")
        self.BringWindowToFront()

    def MacNewFile(self):
        print "> MacNewFile called"
        self.frame.new()

    def MacPrintFile(self, file_path):
        print "> MacPrintFile called"
        self.frame.printProject()
        pass


def fixup_osx():
    # ***Hack***
    # On OSX, when launched by Finder, app starts, but instance remains
    # invisible. Re-launching the app will make the 1st instance visible.
    # argv[0] expected to be: 
    #   '/Applications/Anamorphy.app/Contents/Resources/Anamorphy.py'
    POSTFIX = "/Contents/Resources/Anamorphy.py"
    argv0 = sys.argv[0]
    if argv0.endswith(POSTFIX):
        osx_app_path = argv0[:-len(POSTFIX)]
        def deferred_run():
            subprocess.call(["open", osx_app_path])
        wx.FutureCall(2500, deferred_run)


# Create the dialog
def run_GUI(defaults, scene):
    gettext.install("app")  # replace with the appropriate catalog name

    app = MyApp(defaults, scene)
    app.initApp()    
    fixup_osx()

    # Go
    #  exception_handler.setHandler(app.frame.exception)
    #  with exception_handler(app.frame.exception):
    app.MainLoop()
    #  exception_handler.resetHandler()
