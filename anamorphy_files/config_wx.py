"""
This module cares for saving/restoring the windows size and position.
"""

import wx
import os.path
import ConfigParser
import constants


class Config(object):
    """This class handles the program's configuration. It is stored into the
    user directory, as a plain old good INI file ;-)"""

    PATH = constants.APP_CONFIG_PATH

    def _getint(self, section, var, default):
        try:
            return self._config.getint(section, var)
        except:
            return default

    def _getstr(self, section, var, default):
        try:
            return self._config.get(section, var)
        except:
            return default

    def __init__(self):
        self._config = ConfigParser.RawConfigParser()
        self._config.read(self.PATH)

        # main frame
        self.pos_x = self._getint('position', 'x', 50)
        self.pos_y = self._getint('position', 'y', 50)
        self.pos_w = self._getint('position', 'w', 800)
        self.pos_h = self._getint('position', 'h', 700)

        # last saved
        self.last_saved = self._getstr('history', 'last', None)

    def checkGeometry(self):
        rect = wx.Rect(self.pos_x, self.pos_y, self.pos_w, self.pos_h)
        return checkGeometry(rect)

    def save(self):
        config = ConfigParser.RawConfigParser()

        # main frame
        config.add_section('position')
        config.set('position', 'x', self.pos_x)
        config.set('position', 'y', self.pos_y)
        config.set('position', 'w', self.pos_w)
        config.set('position', 'h', self.pos_h)
        config.add_section('history')
        if self.last_saved is not None:
            config.set('history', 'last', self.last_saved)

        configfile = open(self.PATH, 'w')
        config.write(configfile)


def checkGeometry(rect):
    """Checks if the given rect is "sufficiently" visible, i.e.
    - has some minimum overlap with any of the displays,
    - is not too small
    - is not too big (i.e. twice as the display)
    May not be called before the wx App has been created."""

    MINIMUM_OVERLAP = 20
    MINIMUM_SIZE = 50

    # check big enough
    if rect.width < MINIMUM_SIZE or rect.height < MINIMUM_SIZE:
        return False

    nb_displays = wx.Display.GetCount()
    for i in range(nb_displays):
        disp = wx.Display(i)
        disp_rect = disp.GetGeometry()

        # check size
        if rect.width > disp_rect.width * 2:
            continue
        if rect.height > disp_rect.height * 2:
            continue

        # check sufficient overlap
        inter = disp_rect.Intersect(rect)  # !!! modifies disp_rect
        if inter.width > MINIMUM_OVERLAP and inter.height > MINIMUM_OVERLAP:
            return True
    return False
