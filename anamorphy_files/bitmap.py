"""
This module provides a Bitmap that can be loaded from file, and
pseudo(*) perspective-transformed.

It is implemented by a WX or PIL bitmap.

(*) "Pseudo" is meant to distinguish from real 3D->2D perspective
projection; instead of which, we proceed to 2D->2D perspective
transform here.
"""
import wx
from PIL import Image
from PIL import ImageDraw

import geometry
import numpy
import pil2wx
import constants

THUMBNAIL_SIZE = constants.BITMAP_THUMBNAIL_SIZE
THUMB_TRANSPARENCY = constants.BITMAP_THUMB_TRANSPARENCY
MAX_REASONABLE_COORD_FACTOR = constants.MAX_REASONABLE_COORD_FACTOR


def makeFromPerspective(bitmap,
                        canvas_w, canvas_h,
                        img_corners,
                        bound_corners,
                        name="?",
                        use_thumbnail=True,
                        fast=False):
        """
        Does perspective-transformed of the bitmap represented by this
        object, with a perspective defined by four img corners, and
        with a clipping area defined by the bound corners.

        Returns a wxBitmap, and its offset position in the canvas.

        img_corners are in this order:
        +------> y
        | 1  3
        | 0  2
        V
        x
        """
        img = bitmap.getPilThumb() if use_thumbnail else bitmap.getPil()
        src_w, src_h = img.size
        (dst_x, dst_y), dst_w, dst_h = geometry.boundingRect(img_corners)

        src_pts = [(0, src_h), (0, 0), (src_w, src_h), (src_w, 0)]
        dst_pts = [(x, y) for x, y in img_corners]

        # check that all coordinates are "reasonable"
        # Todo: check versus card size
        values = [abs(item) for sublist in dst_pts for item in sublist]
        maxi = max(bitmap.getWidth(), bitmap.getHeight())
        max_coord = maxi * MAX_REASONABLE_COORD_FACTOR
        if fast and True in [v > max_coord for v in values]:
                return None, 0, 0, None

        # do persp transform
        pts8 = src_pts + dst_pts
        data = get_transform_data(pts8)
        persp_img = img.transform((canvas_w, canvas_h),
                                  Image.PERSPECTIVE, data, Image.BILINEAR)

        # clip
        (bound_x, bound_y), bound_w, bound_h = geometry.boundingRect(
            bound_corners or dst_pts)

        crop_w = bound_w + bound_x - dst_x
        crop_h = bound_y + bound_h - dst_y
        box = [int(v) for v in (bound_x, bound_y,
                                bound_x + bound_w,
                                bound_y + bound_h)]
        pil_img = persp_img.crop(box)

        #pil_img.save("result-%s.png" % name)

        # done
        return Bitmap(pil=pil_img, progress_fn=bitmap.progress_fn), \
            bound_x, bound_y, dst_pts


def progress(fn, msg):
    if fn is not None:
        fn(msg)
    else:
        print msg


def makeFromFile(file_name, progress_fn=None):
    if not file_name:
        raise RuntimeError("Invalid file name")
    progress(progress_fn, "Opening image")
    pil_img = Image.open(file_name).convert("RGBA")
    bmp = Bitmap(pil=pil_img, progress_fn=progress_fn)
    return bmp


class Bitmap(object):
    def __init__(self, pil=None, wx=None, progress_fn=None):
        assert(pil is not None)
        self.pil = pil
        self.pil_thumb = None

        self.wx = wx
        self.wx_thumb = None

        self.portion_top = None
        self.portion_bottom = None
        self.portion_left = None
        self.portion_right = None

        self.wx_scaled = None
        self.pil_scaled = None
        self.scaled_w = None
        self.scaled_h = None

        self.progress_fn = progress_fn

    def resetProgressFn(self):
        self.progress_fn = None

    def getPil(self):
        if not self.pil:
            self.pil = pil2wx.WxBitmapToPilImage(self.wx)
        return self.pil

    def getPilOpaque(self, color):
        """
        Return a PIL copy without alpha, as if original image with
        alpha was laid on a background of the given color.
        """
        img = self.getPil()
        backimg = Image.new("RGB", img.size, color)
        newimg = Image.composite(img.convert("RGB"), backimg, img)
        return newimg

    def getWx(self):
        if not self.wx:
            self.wx = pil2wx.PilImageToWxBitmap(self.pil)
        return self.wx

    def getWidth(self):
        if self.pil is not None:
            width, height = self.pil.size
            return width
        else:
            return self.wx.GetWidth()

    def getHeight(self):
        if self.pil is not None:
            width, height = self.pil.size
            return height
        else:
            return self.wx.GetHeight()

    def progress(self, msg):
        progress(self.progress_fn, msg)

    def getPilThumb(self):
        if self.pil_thumb is None:
            self.progress("Making PIL thumb...")
            thumb = self.getPil().copy()
            thumb.thumbnail((THUMBNAIL_SIZE, THUMBNAIL_SIZE),
                            Image.ANTIALIAS)
            self.pil_thumb = thumb
        return self.pil_thumb

    def getWxThumb(self):
        if self.wx_thumb is None:
            self.progress("Making WX thumb...")
            pil_thumb = self.getPilThumb()
            pil_thumb_trans = makeTransluscent(pil_thumb, THUMB_TRANSPARENCY)
            self.wx_thumb = pil2wx.PilImageToWxBitmap(pil_thumb_trans)
        return self.wx_thumb

    def getPortion(self, box_rel, name=None):
        pil = self.getPil()
        w, h = pil.size
        a, b, c, d = box_rel
        box = w * a, h * b, w * c - 1, h * d - 1
        box = [int(x + 0.5) for x in box]
        pil = pil.crop(box)
        pil.load()
        #pil = makeTransluscent(pil, THUMB_TRANSPARENCY)
        return Bitmap(pil=pil, progress_fn=self.progress_fn)

    def getTop(self):
        if self.portion_top is None:
            self.portion_top = self.getPortion((0, 0, 1, 0.5), "top")
        return self.portion_top

    def getBottom(self):
        if self.portion_bottom is None:
            self.portion_bottom = self.getPortion((0, 0.5, 1, 1), "bot")
        return self.portion_bottom

    def getLeft(self):
        if self.portion_left is None:
            self.portion_left = self.getPortion((0, 0, 0.5, 1), "lft")
        return self.portion_left

    def getRight(self):
        if self.portion_right is None:
            self.portion_right = self.getPortion((0.5, 0, 1, 1), "rgt")
        return self.portion_right

    def getScaled(self, w, h, use_thumb=True):
        if None in (self.scaled_w, self.scaled_h) or \
                abs(self.scaled_w - w) > 1 or \
                abs(self.scaled_h - h) > 1:
            self.progress("Rescaling image...")

            self.progress("Making WX rescaled...")
            img = self.getWxThumb() if use_thumb else self.getWx()
            img = wx.ImageFromBitmap(img)
            img = img.Scale(w, h, wx.IMAGE_QUALITY_HIGH)
            self.wx_scaled = wx.BitmapFromImage(img)

            self.progress("Making PIL rescaled...")
            img = self.getPilThumb() if use_thumb else self.getPil()
            img = img.resize((w, h), Image.ANTIALIAS)
            self.pil_scaled = img

            self.scaled_w = w
            self.scaled_h = h
            self.scaled_bmp = Bitmap(wx=self.wx_scaled,
                                     pil=self.pil_scaled,
                                     progress_fn=self.progress_fn)
        return self.scaled_bmp


def makeTransluscent(img, factor):
        img = img.copy()
        alpha = img.split()[3]
        alpha = alpha.point(lambda p: p * factor)
        img.putalpha(alpha)
        return img

        transparent_area = [0, 0] + list(img.size)
        mask = Image.new('L', img.size, color=255)
        draw = ImageDraw.Draw(mask)
        draw.rectangle(transparent_area, fill=255 - 32)
        img.putalpha(mask)
        return img


def get_transform_data(pts8):
    # original four corners, (u0,v0) ... (u3,v3)
    # new positions (x0,y0) ... (x3,y3)
    #
    # http://mail.scipy.org/pipermail/scipy-user/2009-September/022590.html

    u0, v0 = pts8[4]
    u1, v1 = pts8[5]
    u2, v2 = pts8[6]
    u3, v3 = pts8[7]

    x0, y0 = pts8[0]
    x1, y1 = pts8[1]
    x2, y2 = pts8[2]
    x3, y3 = pts8[3]

    G = numpy.array([
            [u0, v0, 1,  0,  0, 0, -u0 * x0, -v0 * x0],
            [u1, v1, 1,  0,  0, 0, -u1 * x1, -v1 * x1],
            [u2, v2, 1,  0,  0, 0, -u2 * x2, -v2 * x2],
            [u3, v3, 1,  0,  0, 0, -u3 * x3, -v3 * x3],
            [0,   0, 0, u0, v0, 1, -u0 * y0, -v0 * y0],
            [0,   0, 0, u1, v1, 1, -u1 * y1, -v1 * y1],
            [0,   0, 0, u2, v2, 1, -u2 * y2, -v2 * y2],
            [0,   0, 0, u3, v3, 1, -u3 * y3, -v3 * y3]
            ])
    d = numpy.array([x0, x1, x2, x3, y0, y1, y2, y3]).transpose()
    m = numpy.linalg.solve(G, d)
    return m
