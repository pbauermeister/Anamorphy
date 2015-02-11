#!/usr/bin/env python

"""
This application uses WxPython for:
- control widgets to define the camera (perspective)
- and to manipulate the scene (3D shapes),
- a Paint display for the 2D rendering.
"""

import sys
import os

import scene
import myapp
import config

defaults = {
    "units_length": "cm",
    "camera_azimuth": 70,
    "camera_altitude": 32,
    "camera_distance": 800,
    "camera_fov": 80,
    "card_width": 210,
    "card_height": 297,
    "card_angle": 90,
    "card_fold": 0,
    "card_elevation": 0,
    "card_background": "",
    "card_background_show": False,
    "marquee_image": "sample_pics/rubiks.png",
    "marquee_show": True,
    "marquee_width": 100,
    "marquee_distance": 300,
    "marquee_hoff": -6,
    "marquee_voff": 4,
    "export_bitmap_width": 1600,
    "export_bitmap_height": 2262,
    "export_bitmap": None,
    "export_pdf": None,
}

scene = scene.Scene()

# go to the dir representing the current module
my_dir = os.path.split(__file__)[0]
os.chdir(my_dir)

# start app
myapp.run_GUI(defaults, scene)
