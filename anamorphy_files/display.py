class DisplayBase(object):
    """
    This class specifies what a concrete display shall provide, so
    that shapes can render themeselves.
    """

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.offX = w / 2
        self.offY = h / 2
        #self.scale = float(min(w, h)) / float(scale)

    def Rescale(self, x, y):
        # expect a ValueError
        return (
            int(self.offX - x * self.scale + 0.5),
            int(self.offY + y * self.scale + 0.5)
            )

    def Rescales(self, points):
        res = []
        for p in points:
            res.append(self.Rescale(p[0], p[1]))
        return res

    def setScale(self, w, h):
        sw = float(self.w) / float(w)
        sh = float(self.h) / float(h)
        self.scale = min(sw, sh)

    def DrawCircle(self, x, y, r, color, show=True):
        assert()

    def DrawPoint(self, x, y, color, show=True):
        assert()

    def DrawCross(self, x, y, size, color, show=True):
        assert()

    def DrawLine(self, x1, y1, x2, y2, color, show=True):
        assert()

    def DrawText(self, text, x, y, color="BLACK"):
        assert()

    def DrawPolygon(self, points, fillColor, lineColor, show=True):
        assert()

    def DrawBitmap(self, cbmp, x, y):
        assert()

    def SetClip(self, points):
        assert()
