#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Mon Feb 16 00:05:36 2015
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class AutogeneratedMainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AutogeneratedMainFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        self.menu_new = wx.MenuItem(wxglade_tmp_menu, wx.ID_NEW, _("&New...\tCtrl+N"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_new)
        self.menu_open = wx.MenuItem(wxglade_tmp_menu, wx.ID_OPEN, _("&Open...\tCtrl+O"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_open)
        wxglade_tmp_menu.AppendSeparator()
        self.menu_save = wx.MenuItem(wxglade_tmp_menu, wx.ID_SAVE, _("&Save\tCtrl+S"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_save)
        self.menu_save_as = wx.MenuItem(wxglade_tmp_menu, wx.ID_SAVEAS, _("Save As..."), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_save_as)
        wxglade_tmp_menu.AppendSeparator()
        self.menu_print = wx.MenuItem(wxglade_tmp_menu, wx.ID_PRINT, _("&Print...\tCtrl+P"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_print)
        wxglade_tmp_menu.AppendSeparator()
        self.menu_quit = wx.MenuItem(wxglade_tmp_menu, wx.ID_EXIT, _("Quit"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_quit)
        self.frame_menubar.Append(wxglade_tmp_menu, _("&File"))
        wxglade_tmp_menu = wx.Menu()
        self.menu_undo = wx.MenuItem(wxglade_tmp_menu, wx.ID_UNDO, _("&Undo\tCtrl+Z"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_undo)
        self.menu_redo = wx.MenuItem(wxglade_tmp_menu, wx.ID_REDO, _("&Redo\tCtrl+Y"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_redo)
        self.frame_menubar.Append(wxglade_tmp_menu, _("&Edit"))
        wxglade_tmp_menu = wx.Menu()
        self.menu_help = wx.MenuItem(wxglade_tmp_menu, wx.ID_HELP, _("&Help\tF1"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_help)
        self.menu_about = wx.MenuItem(wxglade_tmp_menu, wx.ID_ABOUT, _("&About..."), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.menu_about)
        self.frame_menubar.Append(wxglade_tmp_menu, _("&Help"))
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end
        self.window_perspective = wx.Window(self, wx.ID_ANY)
        self.label_hint = wx.StaticText(self, wx.ID_ANY, _("hint"))
        self.sizer_11_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Perspective"))
        self.button_presets_wizard = wx.Button(self, wx.ID_ANY, _("Wizard..."))
        self.label_11 = wx.StaticText(self, wx.ID_ANY, _("Length"))
        self.choice_units_length = wx.Choice(self, wx.ID_ANY, choices=[_("mm"), _("inch")])
        self.sizer_111_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Units"))
        self.label_6_copy_1 = wx.StaticText(self, wx.ID_ANY, _("Format"))
        self.choice_card_format = wx.Choice(self, wx.ID_ANY, choices=[_("Set to:"), _("A3"), _("A3 landscape"), _("A4"), _("A4 landscape"), _("Letter"), _("Letter landscape")])
        self.label_9_copy_1 = wx.StaticText(self, wx.ID_ANY, _("Fold"), style=wx.ALIGN_RIGHT)
        self.choice_card_fold = wx.Choice(self, wx.ID_ANY, choices=[_("Horizontal valley"), _("Horizontal mountain"), _("Vertical valley"), _("Vertical mountain"), _("None")])
        self.label_7_copy_1 = wx.StaticText(self, wx.ID_ANY, _("Width"), style=wx.ALIGN_RIGHT)
        self.spin_ctrl_card_width = wx.SpinCtrl(self, wx.ID_ANY, "", min=100, max=1000, style=wx.SP_ARROW_KEYS | wx.SP_WRAP | wx.TE_RICH | wx.TE_RICH2 | wx.TE_AUTO_URL | wx.TE_NOHIDESEL | wx.TE_LINEWRAP)
        self.label_8_copy_1 = wx.StaticText(self, wx.ID_ANY, _("Height"), style=wx.ALIGN_RIGHT)
        self.spin_ctrl_card_height = wx.SpinCtrl(self, wx.ID_ANY, "", min=100, max=1000)
        self.label_10_copy_1 = wx.StaticText(self, wx.ID_ANY, _("Angle"), style=wx.ALIGN_RIGHT)
        self.spin_ctrl_card_angle = wx.SpinCtrl(self, wx.ID_ANY, "", min=0, max=180)
        self.label_4_copy_1 = wx.StaticText(self, wx.ID_ANY, _("Elevation"), style=wx.ALIGN_RIGHT)
        self.spin_ctrl_card_elevation = wx.SpinCtrl(self, wx.ID_ANY, "", min=-1000, max=1000)
        self.label_12 = wx.StaticText(self, wx.ID_ANY, _("Background"))
        self.checkbox_card_background = wx.CheckBox(self, wx.ID_ANY, "")
        self.text_ctrl_card_image = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_card_filename = wx.Button(self, wx.ID_ANY, _("..."))
        self.sizer_113_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Card"))
        self.label_2_copy = wx.StaticText(self, wx.ID_ANY, _("Azimuth"), style=wx.ALIGN_RIGHT)
        self.spin_ctrl_camera_azimuth = wx.SpinCtrl(self, wx.ID_ANY, "", min=0, max=180)
        self.label_3_copy = wx.StaticText(self, wx.ID_ANY, _("Altitude"), style=wx.ALIGN_RIGHT)
        self.spin_ctrl_camera_altitude = wx.SpinCtrl(self, wx.ID_ANY, "", min=0, max=90)
        self.label_4_copy = wx.StaticText(self, wx.ID_ANY, _("Distance"), style=wx.ALIGN_RIGHT)
        self.spin_ctrl_camera_distance = wx.SpinCtrl(self, wx.ID_ANY, "", min=200, max=10000)
        self.label_5_copy = wx.StaticText(self, wx.ID_ANY, _("FOV"), style=wx.ALIGN_RIGHT)
        self.spin_ctrl_camera_fov = wx.SpinCtrl(self, wx.ID_ANY, "", min=30, max=180)
        self.label_camera_pos = wx.StaticText(self, wx.ID_ANY, _("camera"), style=wx.ALIGN_RIGHT)
        self.sizer_112_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Camera"))
        self.text_ctrl_marquee_image = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_marquee_filename = wx.Button(self, wx.ID_ANY, _("..."))
        self.label_1_copy = wx.StaticText(self, wx.ID_ANY, _("Show"))
        self.checkbox_marquee_show = wx.CheckBox(self, wx.ID_ANY, "")
        self.label_6_copy = wx.StaticText(self, wx.ID_ANY, _("Width"), style=wx.ALIGN_RIGHT)
        self.spin_ctrl_marquee_width = wx.SpinCtrl(self, wx.ID_ANY, "", min=0, max=359)
        self.label_8 = wx.StaticText(self, wx.ID_ANY, _("Distance"), style=wx.ALIGN_RIGHT)
        self.spin_ctrl_marquee_distance = wx.SpinCtrl(self, wx.ID_ANY, "", min=200, max=10000)
        self.label_9 = wx.StaticText(self, wx.ID_ANY, _("Hor. offset"))
        self.spin_ctrl_marquee_hoff = wx.SpinCtrl(self, wx.ID_ANY, "", min=-1000, max=1000)
        self.label_10 = wx.StaticText(self, wx.ID_ANY, _("Ver. offset"))
        self.spin_ctrl_marquee_voff = wx.SpinCtrl(self, wx.ID_ANY, "", min=-1000, max=1000)
        self.label_2_copy_1 = wx.StaticText(self, wx.ID_ANY, _("Tiles"))
        self.spin_ctrl_marquee_tiles_m = wx.SpinCtrl(self, wx.ID_ANY, "", min=1, max=10)
        self.label_3_copy_1 = wx.StaticText(self, wx.ID_ANY, _("x"))
        self.spin_ctrl_marquee_tiles_n = wx.SpinCtrl(self, wx.ID_ANY, "", min=1, max=10)
        self.sizer_114_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Object"))
        self.window_anamorphosis = wx.Window(self, wx.ID_ANY)
        self.sizer_11_copy_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Anamorphosis Preview"))
        self.button_export_pdf = wx.Button(self, wx.ID_ANY, _("Export PDF..."))
        self.sizer_2_copy_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Document"))
        self.label_7 = wx.StaticText(self, wx.ID_ANY, _("Width"))
        self.spin_ctrl_export_bitmap_width = wx.SpinCtrl(self, wx.ID_ANY, "", min=10, max=100000)
        self.label_13 = wx.StaticText(self, wx.ID_ANY, _("Height"))
        self.spin_ctrl_export_bitmap_height = wx.SpinCtrl(self, wx.ID_ANY, "", min=10, max=100000)
        self.button_export_image = wx.Button(self, wx.ID_ANY, _("Export PNG..."))
        self.sizer_2_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Image"))
        self.button_export_fullscreen = wx.Button(self, wx.ID_ANY, _("Show"))
        self.sizer_2_copy_1_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Fullscreen"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.OnMenuNew, self.menu_new)
        self.Bind(wx.EVT_MENU, self.OnMenuOpen, self.menu_open)
        self.Bind(wx.EVT_MENU, self.OnMenuSave, self.menu_save)
        self.Bind(wx.EVT_MENU, self.OnMenuSaveAs, self.menu_save_as)
        self.Bind(wx.EVT_MENU, self.OnMenuPrint, self.menu_print)
        self.Bind(wx.EVT_MENU, self.OnMenuQuit, self.menu_quit)
        self.Bind(wx.EVT_MENU, self.OnMenuUndo, self.menu_undo)
        self.Bind(wx.EVT_MENU, self.OnMenuRedo, self.menu_redo)
        self.Bind(wx.EVT_MENU, self.OnMenuHelp, self.menu_help)
        self.Bind(wx.EVT_MENU, self.OnMenuAbout, self.menu_about)
        self.Bind(wx.EVT_BUTTON, self.OnPresetWizardClicked, self.button_presets_wizard)
        self.Bind(wx.EVT_CHOICE, self.OnUnitsLengthChoice, self.choice_units_length)
        self.Bind(wx.EVT_CHOICE, self.OnCardFormatChoice, self.choice_card_format)
        self.Bind(wx.EVT_CHOICE, self.OnCardFoldChoice, self.choice_card_fold)
        self.Bind(wx.EVT_SPINCTRL, self.OnCardWidthSpin, self.spin_ctrl_card_width)
        self.Bind(wx.EVT_SPINCTRL, self.OnCardHeightSpin, self.spin_ctrl_card_height)
        self.Bind(wx.EVT_SPINCTRL, self.OnCardAngleSpin, self.spin_ctrl_card_angle)
        self.Bind(wx.EVT_SPINCTRL, self.OnCardElevationSpin, self.spin_ctrl_card_elevation)
        self.Bind(wx.EVT_CHECKBOX, self.OnCardBackgroundCheck, self.checkbox_card_background)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnCardBackgroundImage, self.text_ctrl_card_image)
        self.Bind(wx.EVT_TEXT, self.OnCardBackgroundImage, self.text_ctrl_card_image)
        self.Bind(wx.EVT_BUTTON, self.OnCardBackgroundChoose, self.button_card_filename)
        self.Bind(wx.EVT_SPINCTRL, self.OnCameraAzimuthSpin, self.spin_ctrl_camera_azimuth)
        self.Bind(wx.EVT_SPINCTRL, self.OnCameraAltitudeSpin, self.spin_ctrl_camera_altitude)
        self.Bind(wx.EVT_SPINCTRL, self.OnCameraDistanceSpin, self.spin_ctrl_camera_distance)
        self.Bind(wx.EVT_SPINCTRL, self.OnCameraFovSpin, self.spin_ctrl_camera_fov)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnMarqueeImage, self.text_ctrl_marquee_image)
        self.Bind(wx.EVT_TEXT, self.OnMarqueeImage, self.text_ctrl_marquee_image)
        self.Bind(wx.EVT_BUTTON, self.OnMarqueeChoose, self.button_marquee_filename)
        self.Bind(wx.EVT_CHECKBOX, self.OnMarqueeShowCheck, self.checkbox_marquee_show)
        self.Bind(wx.EVT_SPINCTRL, self.OnMarqueeWidthSpin, self.spin_ctrl_marquee_width)
        self.Bind(wx.EVT_SPINCTRL, self.OnMarqueeDistanceSpin, self.spin_ctrl_marquee_distance)
        self.Bind(wx.EVT_SPINCTRL, self.OnMarqueeHOffSpin, self.spin_ctrl_marquee_hoff)
        self.Bind(wx.EVT_SPINCTRL, self.OnMarqueeVOffSpin, self.spin_ctrl_marquee_voff)
        self.Bind(wx.EVT_SPINCTRL, self.OnMarqueeTilesMSpin, self.spin_ctrl_marquee_tiles_m)
        self.Bind(wx.EVT_SPINCTRL, self.OnMarqueeTilesNSpin, self.spin_ctrl_marquee_tiles_n)
        self.Bind(wx.EVT_BUTTON, self.OnExportPdfClicked, self.button_export_pdf)
        self.Bind(wx.EVT_SPINCTRL, self.OnExportBitmapWidthSpin, self.spin_ctrl_export_bitmap_width)
        self.Bind(wx.EVT_SPINCTRL, self.OnExportBitmapHeightSpin, self.spin_ctrl_export_bitmap_height)
        self.Bind(wx.EVT_BUTTON, self.OnExportImageClicked, self.button_export_image)
        self.Bind(wx.EVT_BUTTON, self.OnShowFullscreenClicked, self.button_export_fullscreen)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AutogeneratedMainFrame.__set_properties
        self.SetTitle(_("Anamorphy"))
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("anamorphy.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.window_perspective.SetBackgroundColour(wx.Colour(225, 225, 225))
        self.label_hint.SetBackgroundColour(wx.Colour(225, 225, 225))
        self.choice_units_length.SetMinSize((80, 29))
        self.choice_units_length.SetSelection(0)
        self.choice_card_format.SetMinSize((80, 29))
        self.choice_card_format.SetSelection(0)
        self.choice_card_fold.SetMinSize((80, 29))
        self.choice_card_fold.SetSelection(0)
        self.spin_ctrl_card_width.SetMinSize((60, 25))
        self.spin_ctrl_card_height.SetMinSize((60, 25))
        self.spin_ctrl_card_angle.SetMinSize((60, 25))
        self.spin_ctrl_card_elevation.SetMinSize((60, 25))
        self.button_card_filename.SetMinSize((28, 28))
        self.spin_ctrl_camera_azimuth.SetMinSize((60, 25))
        self.spin_ctrl_camera_altitude.SetMinSize((60, 25))
        self.spin_ctrl_camera_distance.SetMinSize((60, 25))
        self.label_5_copy.Hide()
        self.spin_ctrl_camera_fov.SetMinSize((60, 25))
        self.spin_ctrl_camera_fov.Hide()
        self.button_marquee_filename.SetMinSize((28, 28))
        self.spin_ctrl_marquee_width.SetMinSize((60, 25))
        self.spin_ctrl_marquee_distance.SetMinSize((60, 25))
        self.spin_ctrl_marquee_hoff.SetMinSize((60, 25))
        self.spin_ctrl_marquee_voff.SetMinSize((60, 25))
        self.label_2_copy_1.Hide()
        self.spin_ctrl_marquee_tiles_m.SetMinSize((45, 25))
        self.spin_ctrl_marquee_tiles_m.Hide()
        self.label_3_copy_1.Hide()
        self.spin_ctrl_marquee_tiles_n.SetMinSize((45, 25))
        self.spin_ctrl_marquee_tiles_n.Hide()
        self.window_anamorphosis.SetBackgroundColour(wx.Colour(225, 225, 225))
        self.spin_ctrl_export_bitmap_width.SetMinSize((60, 25))
        self.spin_ctrl_export_bitmap_height.SetMinSize((60, 25))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AutogeneratedMainFrame.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_12 = wx.FlexGridSizer(3, 1, 0, 0)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_2_copy_1_staticbox.Lower()
        sizer_2_copy_1 = wx.StaticBoxSizer(self.sizer_2_copy_1_staticbox, wx.VERTICAL)
        sizer_3_copy_1 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_2_staticbox.Lower()
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_10 = wx.FlexGridSizer(2, 2, 0, 0)
        self.sizer_2_copy_staticbox.Lower()
        sizer_2_copy = wx.StaticBoxSizer(self.sizer_2_copy_staticbox, wx.VERTICAL)
        sizer_3_copy = wx.BoxSizer(wx.VERTICAL)
        self.sizer_11_copy_staticbox.Lower()
        sizer_11_copy = wx.StaticBoxSizer(self.sizer_11_copy_staticbox, wx.VERTICAL)
        grid_sizer_4_copy = wx.FlexGridSizer(1, 1, 0, 0)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_5 = wx.FlexGridSizer(2, 1, 0, 0)
        self.sizer_114_staticbox.Lower()
        sizer_114 = wx.StaticBoxSizer(self.sizer_114_staticbox, wx.VERTICAL)
        grid_sizer_3 = wx.FlexGridSizer(3, 1, 0, 0)
        grid_sizer_9 = wx.FlexGridSizer(1, 4, 0, 0)
        grid_sizer_1141 = wx.FlexGridSizer(5, 2, 0, 0)
        grid_sizer_2 = wx.FlexGridSizer(1, 2, 0, 0)
        self.sizer_112_staticbox.Lower()
        sizer_112 = wx.StaticBoxSizer(self.sizer_112_staticbox, wx.VERTICAL)
        grid_sizer_1121 = wx.FlexGridSizer(4, 2, 0, 0)
        grid_sizer_6 = wx.FlexGridSizer(4, 1, 0, 0)
        self.sizer_113_staticbox.Lower()
        sizer_113 = wx.StaticBoxSizer(self.sizer_113_staticbox, wx.VERTICAL)
        grid_sizer_8 = wx.FlexGridSizer(3, 1, 0, 0)
        grid_sizer_2_copy_1 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_1131 = wx.FlexGridSizer(5, 2, 0, 0)
        grid_sizer_7 = wx.FlexGridSizer(2, 2, 0, 0)
        self.sizer_111_staticbox.Lower()
        sizer_111 = wx.StaticBoxSizer(self.sizer_111_staticbox, wx.VERTICAL)
        grid_sizer_1111 = wx.FlexGridSizer(1, 2, 0, 10)
        self.sizer_11_staticbox.Lower()
        sizer_11 = wx.StaticBoxSizer(self.sizer_11_staticbox, wx.VERTICAL)
        grid_sizer_4 = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer_4.Add(self.window_perspective, 1, wx.EXPAND, 0)
        grid_sizer_4.Add(self.label_hint, 0, wx.EXPAND, 0)
        grid_sizer_4.AddGrowableRow(0)
        grid_sizer_4.AddGrowableCol(0)
        sizer_11.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(sizer_11, 1, wx.ALL | wx.EXPAND, 3)
        grid_sizer_6.Add(self.button_presets_wizard, 0, wx.ALL | wx.EXPAND | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 3)
        grid_sizer_1111.Add(self.label_11, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1111.Add(self.choice_units_length, 0, 0, 0)
        grid_sizer_1111.AddGrowableCol(0)
        sizer_111.Add(grid_sizer_1111, 1, wx.EXPAND, 0)
        grid_sizer_6.Add(sizer_111, 0, wx.ALL | wx.EXPAND, 3)
        grid_sizer_7.Add(self.label_6_copy_1, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_7.Add(self.choice_card_format, 0, 0, 0)
        grid_sizer_7.Add(self.label_9_copy_1, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_7.Add(self.choice_card_fold, 0, 0, 0)
        grid_sizer_7.AddGrowableCol(0)
        grid_sizer_8.Add(grid_sizer_7, 1, wx.EXPAND, 0)
        grid_sizer_1131.Add(self.label_7_copy_1, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1131.Add(self.spin_ctrl_card_width, 0, wx.ALIGN_RIGHT, 0)
        grid_sizer_1131.Add(self.label_8_copy_1, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1131.Add(self.spin_ctrl_card_height, 0, wx.ALIGN_RIGHT, 0)
        grid_sizer_1131.Add(self.label_10_copy_1, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1131.Add(self.spin_ctrl_card_angle, 0, wx.ALIGN_RIGHT, 0)
        grid_sizer_1131.Add(self.label_4_copy_1, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1131.Add(self.spin_ctrl_card_elevation, 0, 0, 0)
        grid_sizer_1131.Add(self.label_12, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1131.Add(self.checkbox_card_background, 0, 0, 0)
        grid_sizer_1131.AddGrowableCol(0)
        grid_sizer_8.Add(grid_sizer_1131, 1, wx.EXPAND, 0)
        grid_sizer_2_copy_1.Add(self.text_ctrl_card_image, 0, wx.LEFT | wx.EXPAND, 10)
        grid_sizer_2_copy_1.Add(self.button_card_filename, 0, 0, 0)
        grid_sizer_2_copy_1.AddGrowableCol(0)
        grid_sizer_8.Add(grid_sizer_2_copy_1, 1, wx.EXPAND, 0)
        grid_sizer_8.AddGrowableCol(0)
        sizer_113.Add(grid_sizer_8, 1, wx.EXPAND, 0)
        grid_sizer_6.Add(sizer_113, 1, wx.ALL | wx.EXPAND, 3)
        grid_sizer_6.AddGrowableCol(0)
        sizer_1.Add(grid_sizer_6, 1, wx.EXPAND, 0)
        grid_sizer_1121.Add(self.label_2_copy, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1121.Add(self.spin_ctrl_camera_azimuth, 0, 0, 0)
        grid_sizer_1121.Add(self.label_3_copy, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1121.Add(self.spin_ctrl_camera_altitude, 0, 0, 0)
        grid_sizer_1121.Add(self.label_4_copy, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1121.Add(self.spin_ctrl_camera_distance, 0, 0, 0)
        grid_sizer_1121.Add(self.label_5_copy, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1121.Add(self.spin_ctrl_camera_fov, 0, 0, 0)
        grid_sizer_1121.AddGrowableCol(0)
        sizer_112.Add(grid_sizer_1121, 1, wx.EXPAND, 0)
        sizer_112.Add(self.label_camera_pos, 0, wx.LEFT | wx.EXPAND | wx.ALIGN_RIGHT, 10)
        grid_sizer_5.Add(sizer_112, 1, wx.ALL | wx.EXPAND, 3)
        grid_sizer_2.Add(self.text_ctrl_marquee_image, 0, wx.LEFT | wx.EXPAND, 10)
        grid_sizer_2.Add(self.button_marquee_filename, 0, 0, 0)
        grid_sizer_2.AddGrowableCol(0)
        grid_sizer_3.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        grid_sizer_1141.Add(self.label_1_copy, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1141.Add(self.checkbox_marquee_show, 0, 0, 0)
        grid_sizer_1141.Add(self.label_6_copy, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1141.Add(self.spin_ctrl_marquee_width, 0, 0, 0)
        grid_sizer_1141.Add(self.label_8, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1141.Add(self.spin_ctrl_marquee_distance, 0, 0, 0)
        grid_sizer_1141.Add(self.label_9, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1141.Add(self.spin_ctrl_marquee_hoff, 0, 0, 0)
        grid_sizer_1141.Add(self.label_10, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1141.Add(self.spin_ctrl_marquee_voff, 0, 0, 0)
        grid_sizer_1141.AddGrowableCol(0)
        grid_sizer_3.Add(grid_sizer_1141, 1, wx.EXPAND, 0)
        grid_sizer_9.Add(self.label_2_copy_1, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_9.Add(self.spin_ctrl_marquee_tiles_m, 0, 0, 0)
        grid_sizer_9.Add(self.label_3_copy_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_9.Add(self.spin_ctrl_marquee_tiles_n, 0, 0, 0)
        grid_sizer_9.AddGrowableCol(0)
        grid_sizer_3.Add(grid_sizer_9, 1, wx.EXPAND, 0)
        grid_sizer_3.AddGrowableCol(0)
        sizer_114.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        grid_sizer_5.Add(sizer_114, 1, wx.ALL | wx.EXPAND, 3)
        grid_sizer_5.AddGrowableRow(0)
        grid_sizer_5.AddGrowableRow(1)
        grid_sizer_5.AddGrowableCol(0)
        sizer_1.Add(grid_sizer_5, 1, wx.EXPAND, 0)
        grid_sizer_12.Add(sizer_1, 1, wx.EXPAND, 0)
        grid_sizer_4_copy.Add(self.window_anamorphosis, 1, wx.EXPAND, 0)
        grid_sizer_4_copy.AddGrowableRow(0)
        grid_sizer_4_copy.AddGrowableCol(0)
        sizer_11_copy.Add(grid_sizer_4_copy, 1, wx.EXPAND, 0)
        grid_sizer_12.Add(sizer_11_copy, 1, wx.ALL | wx.EXPAND, 3)
        sizer_3_copy.Add((20, 25), 0, 0, 0)
        sizer_3_copy.Add((20, 25), 0, 0, 0)
        sizer_3_copy.Add(self.button_export_pdf, 0, wx.EXPAND | wx.ALIGN_BOTTOM, 0)
        sizer_2_copy.Add(sizer_3_copy, 1, wx.EXPAND | wx.ALIGN_BOTTOM, 0)
        sizer_4.Add(sizer_2_copy, 1, wx.ALL | wx.EXPAND, 3)
        grid_sizer_10.Add(self.label_7, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_10.Add(self.spin_ctrl_export_bitmap_width, 0, 0, 0)
        grid_sizer_10.Add(self.label_13, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_10.Add(self.spin_ctrl_export_bitmap_height, 0, 0, 0)
        sizer_3.Add(grid_sizer_10, 1, wx.EXPAND, 0)
        sizer_3.Add(self.button_export_image, 0, wx.EXPAND | wx.ALIGN_BOTTOM, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_4.Add(sizer_2, 1, wx.ALL | wx.EXPAND, 3)
        sizer_3_copy_1.Add((20, 25), 0, 0, 0)
        sizer_3_copy_1.Add((20, 25), 0, 0, 0)
        sizer_3_copy_1.Add(self.button_export_fullscreen, 0, wx.EXPAND | wx.ALIGN_BOTTOM, 0)
        sizer_2_copy_1.Add(sizer_3_copy_1, 1, wx.EXPAND | wx.ALIGN_BOTTOM, 0)
        sizer_4.Add(sizer_2_copy_1, 1, wx.ALL | wx.EXPAND, 3)
        grid_sizer_12.Add(sizer_4, 1, 0, 0)
        grid_sizer_12.AddGrowableRow(1)
        grid_sizer_1.Add(grid_sizer_12, 1, wx.EXPAND, 0)
        grid_sizer_1.AddGrowableRow(0)
        grid_sizer_1.AddGrowableCol(0)
        sizer.Add(grid_sizer_1, 1, wx.ALL | wx.EXPAND, 8)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()
        # end wxGlade

    def OnMenuNew(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuNew' not implemented!"
        event.Skip()

    def OnMenuOpen(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuOpen' not implemented!"
        event.Skip()

    def OnMenuSave(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuSave' not implemented!"
        event.Skip()

    def OnMenuSaveAs(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuSaveAs' not implemented!"
        event.Skip()

    def OnMenuPrint(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuPrint' not implemented!"
        event.Skip()

    def OnMenuQuit(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuQuit' not implemented!"
        event.Skip()

    def OnMenuUndo(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuUndo' not implemented!"
        event.Skip()

    def OnMenuRedo(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuRedo' not implemented!"
        event.Skip()

    def OnMenuHelp(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuHelp' not implemented!"
        event.Skip()

    def OnMenuAbout(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMenuAbout' not implemented!"
        event.Skip()

    def OnPresetWizardClicked(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnPresetWizardClicked' not implemented!"
        event.Skip()

    def OnUnitsLengthChoice(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnUnitsLengthChoice' not implemented!"
        event.Skip()

    def OnCardFormatChoice(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnCardFormatChoice' not implemented!"
        event.Skip()

    def OnCardFoldChoice(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnCardFoldChoice' not implemented!"
        event.Skip()

    def OnCardWidthSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnCardWidthSpin' not implemented!"
        event.Skip()

    def OnCardHeightSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnCardHeightSpin' not implemented!"
        event.Skip()

    def OnCardAngleSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnCardAngleSpin' not implemented!"
        event.Skip()

    def OnCardElevationSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnCardElevationSpin' not implemented!"
        event.Skip()

    def OnCardBackgroundCheck(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnCardBackgroundCheck' not implemented!"
        event.Skip()

    def OnCardBackgroundImage(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnCardBackgroundImage' not implemented!"
        event.Skip()

    def OnCardBackgroundChoose(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnCardBackgroundChoose' not implemented!"
        event.Skip()

    def OnCameraAzimuthSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnCameraAzimuthSpin' not implemented!"
        event.Skip()

    def OnCameraAltitudeSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnCameraAltitudeSpin' not implemented!"
        event.Skip()

    def OnCameraDistanceSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnCameraDistanceSpin' not implemented!"
        event.Skip()

    def OnCameraFovSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnCameraFovSpin' not implemented!"
        event.Skip()

    def OnMarqueeImage(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMarqueeImage' not implemented!"
        event.Skip()

    def OnMarqueeChoose(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMarqueeChoose' not implemented!"
        event.Skip()

    def OnMarqueeShowCheck(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMarqueeShowCheck' not implemented!"
        event.Skip()

    def OnMarqueeWidthSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMarqueeWidthSpin' not implemented!"
        event.Skip()

    def OnMarqueeDistanceSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMarqueeDistanceSpin' not implemented!"
        event.Skip()

    def OnMarqueeHOffSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMarqueeHOffSpin' not implemented!"
        event.Skip()

    def OnMarqueeVOffSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMarqueeVOffSpin' not implemented!"
        event.Skip()

    def OnMarqueeTilesMSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMarqueeTilesMSpin' not implemented!"
        event.Skip()

    def OnMarqueeTilesNSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnMarqueeTilesNSpin' not implemented!"
        event.Skip()

    def OnExportPdfClicked(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnExportPdfClicked' not implemented!"
        event.Skip()

    def OnExportBitmapWidthSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnExportBitmapWidthSpin' not implemented!"
        event.Skip()

    def OnExportBitmapHeightSpin(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnExportBitmapHeightSpin' not implemented!"
        event.Skip()

    def OnExportImageClicked(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnExportImageClicked' not implemented!"
        event.Skip()

    def OnShowFullscreenClicked(self, event):  # wxGlade: AutogeneratedMainFrame.<event_handler>
        print "Event handler 'OnShowFullscreenClicked' not implemented!"
        event.Skip()

# end of class AutogeneratedMainFrame

class AutogeneratedWizardDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AutogeneratedWizardDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.radio_box_affect = wx.RadioBox(self, wx.ID_ANY, _("Affect"), choices=[_("Camera, and placements   "), _("and card size   "), _("and marquee image")], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.wizard_button_1 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("wizard-card-flat.png", wx.BITMAP_TYPE_ANY))
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Simple card\n\nLaying flat"))
        self.wizard_button_4 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("wizard-box-h.png", wx.BITMAP_TYPE_ANY))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, _("Horizontal box\n\nSeen from slightly above"))
        self.wizard_button_2 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("wizard-card-h.png", wx.BITMAP_TYPE_ANY))
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("Folded card\n\nLaying on the back half"))
        self.wizard_button_5 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("wizard-box-v.png", wx.BITMAP_TYPE_ANY))
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _("Vertical box\n\nSeen from the sides"))
        self.wizard_button_3 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("wizard-card-v.png", wx.BITMAP_TYPE_ANY))
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _("Folded card\n\nStanding on the edge"))
        self.wizard_button_6 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("wizard-building.png", wx.BITMAP_TYPE_ANY))
        self.label_6 = wx.StaticText(self, wx.ID_ANY, _("Building\n\nSeen from the floor\n(elevation must be half the height)"))
        self.wizard_button_close = wx.Button(self, wx.ID_CANCEL, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnWizardChoice1Clicked, self.wizard_button_1)
        self.Bind(wx.EVT_BUTTON, self.OnWizardChoice4Clicked, self.wizard_button_4)
        self.Bind(wx.EVT_BUTTON, self.OnWizardChoice2Clicked, self.wizard_button_2)
        self.Bind(wx.EVT_BUTTON, self.OnWizardChoice5Clicked, self.wizard_button_5)
        self.Bind(wx.EVT_BUTTON, self.OnWizardChoice3Clicked, self.wizard_button_3)
        self.Bind(wx.EVT_BUTTON, self.OnWizardChoice6Clicked, self.wizard_button_6)
        self.Bind(wx.EVT_BUTTON, self.OnWizardCloseClicked, self.wizard_button_close)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AutogeneratedWizardDialog.__set_properties
        self.SetTitle(_("Presets Wizard"))
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("anamorphy.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.radio_box_affect.SetSelection(0)
        self.wizard_button_1.SetFocus()
        self.wizard_button_1.SetSize(self.wizard_button_1.GetBestSize())
        self.wizard_button_4.SetSize(self.wizard_button_4.GetBestSize())
        self.wizard_button_2.SetSize(self.wizard_button_2.GetBestSize())
        self.wizard_button_5.SetSize(self.wizard_button_5.GetBestSize())
        self.wizard_button_3.SetSize(self.wizard_button_3.GetBestSize())
        self.wizard_button_6.SetSize(self.wizard_button_6.GetBestSize())
        self.wizard_button_close.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AutogeneratedWizardDialog.__do_layout
        sizer_main = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_11 = wx.FlexGridSizer(3, 1, 0, 0)
        grid_sizer_13 = wx.FlexGridSizer(0, 5, 5, 5)
        grid_sizer_11.Add(self.radio_box_affect, 0, wx.BOTTOM | wx.EXPAND, 20)
        grid_sizer_13.Add(self.wizard_button_1, 0, 0, 0)
        grid_sizer_13.Add(self.label_1, 0, 0, 0)
        grid_sizer_13.Add((30, 20), 0, 0, 0)
        grid_sizer_13.Add(self.wizard_button_4, 0, 0, 0)
        grid_sizer_13.Add(self.label_4, 0, 0, 0)
        grid_sizer_13.Add(self.wizard_button_2, 0, 0, 0)
        grid_sizer_13.Add(self.label_2, 0, 0, 0)
        grid_sizer_13.Add((30, 20), 0, 0, 0)
        grid_sizer_13.Add(self.wizard_button_5, 0, 0, 0)
        grid_sizer_13.Add(self.label_5, 0, 0, 0)
        grid_sizer_13.Add(self.wizard_button_3, 0, 0, 0)
        grid_sizer_13.Add(self.label_3, 0, 0, 0)
        grid_sizer_13.Add((30, 20), 0, 0, 0)
        grid_sizer_13.Add(self.wizard_button_6, 0, 0, 0)
        grid_sizer_13.Add(self.label_6, 0, 0, 0)
        grid_sizer_11.Add(grid_sizer_13, 1, wx.EXPAND, 0)
        grid_sizer_11.Add(self.wizard_button_close, 0, wx.TOP | wx.ALIGN_RIGHT, 10)
        grid_sizer_11.AddGrowableRow(1)
        grid_sizer_11.AddGrowableCol(0)
        sizer_main.Add(grid_sizer_11, 1, wx.ALL | wx.EXPAND, 10)
        self.SetSizer(sizer_main)
        sizer_main.Fit(self)
        self.Layout()
        # end wxGlade

    def OnWizardChoice1Clicked(self, event):  # wxGlade: AutogeneratedWizardDialog.<event_handler>
        print "Event handler 'OnWizardChoice1Clicked' not implemented!"
        event.Skip()

    def OnWizardChoice4Clicked(self, event):  # wxGlade: AutogeneratedWizardDialog.<event_handler>
        print "Event handler 'OnWizardChoice4Clicked' not implemented!"
        event.Skip()

    def OnWizardChoice2Clicked(self, event):  # wxGlade: AutogeneratedWizardDialog.<event_handler>
        print "Event handler 'OnWizardChoice2Clicked' not implemented!"
        event.Skip()

    def OnWizardChoice5Clicked(self, event):  # wxGlade: AutogeneratedWizardDialog.<event_handler>
        print "Event handler 'OnWizardChoice5Clicked' not implemented!"
        event.Skip()

    def OnWizardChoice3Clicked(self, event):  # wxGlade: AutogeneratedWizardDialog.<event_handler>
        print "Event handler 'OnWizardChoice3Clicked' not implemented!"
        event.Skip()

    def OnWizardChoice6Clicked(self, event):  # wxGlade: AutogeneratedWizardDialog.<event_handler>
        print "Event handler 'OnWizardChoice6Clicked' not implemented!"
        event.Skip()

    def OnWizardCloseClicked(self, event):  # wxGlade: AutogeneratedWizardDialog.<event_handler>
        print "Event handler 'OnWizardCloseClicked' not implemented!"
        event.Skip()

# end of class AutogeneratedWizardDialog
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    MainFrame = (None, wx.ID_ANY, "")
    app.SetTopWindow(MainFrame)
    MainFrame.Show()
    app.MainLoop()
