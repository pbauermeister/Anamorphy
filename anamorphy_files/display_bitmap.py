"""
Implements display operations, for a WX display, as (loosely) defined
by display.py.
"""
from display import DisplayBase
import geometry
from PIL import Image
from PIL import ImageDraw
import bitmap


class BitmapDisplay(DisplayBase):
    """
    This class implements the display primitives for WX.

    Callers of DrawSometing() should expect a ValueError or OverflowError
    """
    def __init__(self, w, h):
        super(BitmapDisplay, self).__init__(w, h)
        #self.scale = float(min(w, h)) / float(scale)
        self.image = Image.new("RGBA", (w, h), 0x00ffffff * 0)
        self.draw = ImageDraw.Draw(self.image)

    def DrawBitmap(self, cbmp, x, y):
        pil_img = cbmp.getPil()
        self.image.paste(pil_img, (x, y), pil_img)

    def GetBitmap(self):
        return bitmap.Bitmap(pil=self.image)

    def DrawPolygon(self, points, fillColor, lineColor, show=True):
        ret = []
        for point in points:
            x, y = point
            x, y = self.Rescale(x, y)
            ret.append((x, y))
        if show:
            self.draw.polygon(ret, outline=(0, 0, 0))
        return ret
