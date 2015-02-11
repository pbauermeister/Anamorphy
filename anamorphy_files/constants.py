"""
Constants of the app.
"""
import os
import sys
import glob

#DEFAULT_PATH = os.path.expanduser("~/.Anamorphy.cnf")

if os.name == 'nt':
    print "System is Windows"
    parent = '%(APPDATA)s' % os.environ
    APP_CONFIG_PATH = os.path.join(parent, "Anamorphy.ini")
elif sys.platform.startswith('darwin'):
    print "System is Mac"
    APP_CONFIG_PATH = os.path.expanduser("~/.Anamorphy.ini")
elif os.name == 'posix':
    print "System is Linux/Unix"
    APP_CONFIG_PATH = os.path.expanduser("~/.Anamorphy.ini")

print "Program config file is", APP_CONFIG_PATH

EXTENSION                   = ".anamorphy"
DEFERRED_REDRAW_DELAY       = 0.2

BITMAP_THUMBNAIL_SIZE       = 300
BITMAP_THUMB_TRANSPARENCY   = 0.75
MAX_REASONABLE_COORD_FACTOR = 10
