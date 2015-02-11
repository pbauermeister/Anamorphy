"""
This is a setup.py script originally generated by py2applet but
maintained manually

Usage:
    python setup.py py2app
"""

from setuptools import setup
from glob import glob
import version

NAME = "Anamorphy"
VERSION = version.getVersionFromScm()

APP = ['Anamorphy.py']
DATA_FILES = \
    glob('*.png') \
    + glob('*.ico') \
    + glob('*.html') \
    + glob('*.ini') \
    + glob('sample_pics/*') \


EXT_PACKAGES = ['PIL', 'reportlab', #'simplejson',
                'wx']

# A custom plist for letting it associate with all files.
PLIST = dict(
    CFBundleDocumentTypes=[
        dict(CFBundleTypeExtensions=["anamorphy"],
             CFBundleTypeName="Anamorphy Document",
             CFBundleTypeRole="Editor"),
        ],
#    CFBundleGetInfoString="The text shown by Finder's Get Info panel."
#    CFBundleIconFile=NAME,
    CFBundleName=NAME,
    CFBundleShortVersionString=VERSION,
    CFBundleGetInfoString=' '.join([NAME, VERSION]),
    CFBundleExecutable=NAME,
    CFBundleIdentifier='net.homelinux.ten.anamorphy',
    )

PY2APP_OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'anamorphy.icns',
    'plist': PLIST,
    'includes': EXT_PACKAGES,
    'optimize': 0, # >0 will crash the app :-(
    }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': PY2APP_OPTIONS},
    setup_requires=['py2app'],
)
