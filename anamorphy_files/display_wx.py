"""
Implements display operations, for a WX display, as (loosely) defined
by display.py.
"""
import wx
from display import DisplayBase
import geometry


class PaintDisplay(DisplayBase):
    """
    This class implements the display primitives for WX.

    Callers of DrawSometing() should expect a ValueError or OverflowError
    """
    def __init__(self, dc, w, h):
        super(PaintDisplay, self).__init__(w, h)
        self.dc = dc
        self.font = wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                            wx.FONTWEIGHT_NORMAL, False)

    def DrawCircle(self, x, y, r, color, show=True):
        x, y = self.Rescale(x, y)
        if show:
            self.dc.SetPen(wx.Pen(color))
            self.dc.DrawCircle(x, y, r)
        return (x, y)

    def DrawPoint(self, x, y, color, show=True):
        x, y = self.Rescale(x, y)
        if show:
            self.dc.SetPen(wx.Pen(color))
            self.dc.DrawPoint(x, y)
        return (x, y)

    def DrawCross(self, x, y, size, color, show=True):
        x, y = self.Rescale(x, y)
        s = (size - 1) / 2
        if show:
            self.dc.SetPen(wx.Pen(color))
            self.dc.DrawLine(x, y - s, x, y + s)
            self.dc.DrawLine(x - s, y, x + s, y)
        return (x, y)

    def DrawLine(self, x1, y1, x2, y2, color, show=True):
        x1, y1 = self.Rescale(x1, y1)
        x2, y2 = self.Rescale(x2, y2)
        if show:
            self.dc.SetPen(wx.Pen(color))
            self.dc.DrawLine(x1, y1, x2, y2)
        return (x1, y1), (x2, y2)

    def DrawText(self, text, x, y, color="BLACK"):
        x, y = self.Rescale(x, y)
        self.dc.SetFont(self.font)
        self.dc.SetTextForeground(color)
        self.dc.DrawText(text, x, y - self.dc.GetCharHeight() / 2)
        return (x, y)

    def DrawPolygon(self, points, fillColor, lineColor, show=True):
        wx_points = []
        ret = []
        for point in points:
            x, y = point
            x, y = self.Rescale(x, y)
            ret.append((x, y))
            wx_points.append(wx.Point(x, y))
        if show:
            if isinstance(fillColor, basestring):
                colour = fillColor
            elif fillColor is None:
                colour = 'WHITE'
            else:
                colour = wx.Colour(*fillColor)

            brush = wx.Brush(colour)
            if fillColor is None:
                brush.SetStyle(wx.TRANSPARENT)

            if lineColor is None:
                self.dc.SetPen(wx.TRANSPARENT_PEN)
            else:
                self.dc.SetPen(wx.Pen(lineColor))

            self.dc.SetBrush(brush)
            self.dc.DrawPolygon(wx_points)
        return ret

    def DrawBitmap(self, cbmp, x, y):
        bmp = cbmp.getWx()
        self.dc.DrawBitmap(bmp, x, y)

    def SetClip(self, points):
        self.dc.DestroyClippingRegion()
        if points is not None:
            (x, y), w, h = geometry.boundingRect(self.Rescales(points))
            self.dc.SetClippingRegion(x, y, w, h)
