"""
This module subclasses AutogeneratedWizardDialog from the
autogenerated_GUI.py module.

It implements a wizard letting choose among several typical presets
for projections on various objects (card, box, buildings).
"""

import wx
from autogenerated_GUI import AutogeneratedWizardDialog


class WizardFrame(AutogeneratedWizardDialog):

    def __init__(self, parent, full):
        super(WizardFrame, self).__init__(parent)
        # need to ask labels to wrap (wxglade does not do it for us)
        self.label_1.Wrap(150)
        self.label_2.Wrap(150)
        self.label_3.Wrap(150)
        self.label_4.Wrap(150)
        self.label_5.Wrap(150)
        self.label_6.Wrap(150)
        self.settings = None
        self.full = full
        if full:
            # remove radio choice for params levels
            self.radio_box_affect.Destroy()
            sizer = self.GetSizer()
            sizer.Fit(self)
            self.SetTitle("New Project Template")

    def OnWizardCloseClicked(self, event):
        self.EndModal(retCode=0)

    def submit(self, settings):
        # the radio button defines various levels of parameters that
        # we will force
        if self.full:
            choice = 99
        else:
            choice = self.radio_box_affect.GetSelection()
        keys = []
        if choice >= 0:
            keys += [
                "camera_azimuth",
                "camera_altitude",
                "camera_distance",
                "camera_fov",
                "card_angle",
                "card_fold",
                "marquee_width",
                "marquee_distance",
                "marquee_hoff",
                "marquee_voff",
                ]
        if choice >= 1:
            keys += [
                "card_width",
                "card_height",
                "card_elevation",
                ]
        if choice >= 2:
            keys += [
                "marquee_image",
                "marquee_show",
                ]

        # filter out the parameters that we do not want affected
        for k in settings.keys():
            if k not in keys:
                del settings[k]

        # remember the parameters and close wizard
        self.settings = settings
        self.EndModal(retCode=0)

    def OnWizardChoice1Clicked(self, event):
        self.submit({
            "camera_azimuth": 90,
            "camera_altitude": 46,
            "camera_distance": 760,
            "camera_fov": 80,
            "card_width": 210,
            "card_height": 297,
            "card_angle": 0,
            "card_fold": 4,
            "card_elevation": 0,
            "marquee_image": "sample_pics/rubiks.png",
            "marquee_show": True,
            "marquee_width": 100,
            "marquee_distance": 260,
            "marquee_hoff": 0,
            "marquee_voff": 0,
            })

    def OnWizardChoice2Clicked(self, event):
        self.submit({
            "camera_azimuth": 67,
            "camera_altitude": 34,
            "camera_distance": 760,
            "camera_fov": 80,
            "card_width": 210,
            "card_height": 297,
            "card_angle": 90,
            "card_fold": 0,
            "card_elevation": 0,
            "marquee_image": "sample_pics/rubiks.png",
            "marquee_show": True,
            "marquee_width": 100,
            "marquee_distance": 260,
            "marquee_hoff": 0,
            "marquee_voff": 0,
            })

    def OnWizardChoice3Clicked(self, event):
        self.submit({
            "camera_azimuth": 45,
            "camera_altitude": 0,
            "camera_distance": 760,
            "camera_fov": 80,
            "card_width": 297,
            "card_height": 210,
            "card_angle": 90,
            "card_fold": 2,
            "card_elevation": 0,
            "marquee_image": "sample_pics/rubiks.png",
            "marquee_show": True,
            "marquee_width": 100,
            "marquee_distance": 260,
            "marquee_hoff": 0,
            "marquee_voff": 0,
            })

    def OnWizardChoice4Clicked(self, event):
        self.submit({
            "camera_azimuth": 72,
            "camera_altitude": 29,
            "camera_distance": 760,
            "camera_fov": 80,
            "card_width": 210,
            "card_height": 297,
            "card_angle": 90,
            "card_fold": 1,
            "card_elevation": 0,
            "marquee_image": "sample_pics/rubiks.png",
            "marquee_show": True,
            "marquee_width": 100,
            "marquee_distance": 290,
            "marquee_hoff": -8,
            "marquee_voff": -12,
            })

    def OnWizardChoice5Clicked(self, event):
        self.submit({
            "camera_azimuth": 45,
            "camera_altitude": 18,
            "camera_distance": 760,
            "camera_fov": 80,
            "card_width": 297,
            "card_height": 210,
            "card_angle": 90,
            "card_fold": 3,
            "card_elevation": 0,
            "marquee_image": "sample_pics/rubiks.png",
            "marquee_show": True,
            "marquee_width": 100,
            "marquee_distance": 320,
            "marquee_hoff": -4,
            "marquee_voff": 0,
            })

    def OnWizardChoice6Clicked(self, event):
        self.submit({
            "camera_azimuth": 45,
            "camera_altitude": 0,
            "camera_distance": 860,
            "camera_fov": 80,
            "card_width": 297,
            "card_height": 210,
            "card_angle": 90,
            "card_fold": 3,
            "card_elevation": 105,
            "marquee_image": "sample_pics/rubiks.png",
            "marquee_show": True,
            "marquee_width": 100,
            "marquee_distance": 320,
            "marquee_hoff": -5,
            "marquee_voff": 35,
            })
