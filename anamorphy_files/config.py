"""
This module cares for persistance of user-defined parameters.

They are formatted in JSON as a dict object.
"""
import os.path
import simplejson
import config_wx


def load(filename):
    print "load", filename
    try:
        with file(filename) as f:
            return simplejson.load(f)
    except Exception:
        return {}


def save(filename, values):
    print "save", filename
    if "marquee_image" in values:
        values["marquee_image"] = os.path.abspath(values["marquee_image"])
    with file(filename, "w") as f:
        simplejson.dump(values, f, indent="  ")
