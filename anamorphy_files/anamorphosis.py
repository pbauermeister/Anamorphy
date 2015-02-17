"""
This module does the anamorphic tasks:

- Creation of the marquee in the 3D space, which is a rectangle
  representing the wanted image, placed in the camera axis.

- Computation of the marquee points projected on teh card objects.

- Rendering of the projected image on the card which is unfolded and
  laid flat.
"""
import wx

from display_wx import PaintDisplay
from display_bitmap import BitmapDisplay
import shape
import geometry
import numpy
import math
import render_fullscreen
import bitmap
import traceback
from gui_utils import eraseBackground
import constants

DEBUG = False


class Anamorphosis(object):

    def __init__(self, show_image, bitmap):
        self.show_image = show_image
        self.bitmap = bitmap
        self.bg_bmp_render = wx.Bitmap("bg_2.jpg")

    def renderCanvas(self, canvas, preview=True):
        pdc = wx.PaintDC(canvas)  # simple device context
        dc = wx.GCDC(pdc)  # device context with alpha and anti-alias
        if constants.WITH_TEXTURE_CANVAS:
            eraseBackground(canvas, dc, self.bg_bmp_render)

        canvas_w, canvas_h = canvas.GetClientSize()
        canvas_w -= 1
        canvas_h -= 1
        display = PaintDisplay(dc, canvas_w, canvas_h)
        return self.renderDisplay(display, canvas_w, canvas_h,
                                  preview=preview, box=False)

    def renderDisplay(self, display, display_w, display_h, preview, box,
                      progressPcentFn=lambda x: None):
        progressPcentFn(0)

        prec = 1
        final_image = None

        cb_array = shape.copyShape(shape.getShape("CBP"))
        cf_array = shape.copyShape(shape.getShape("CFP"))

        cb = shape.copyShape(shape.getShape("card_back"))
        cf = shape.copyShape(shape.getShape("card_front"))

        # transform cards to be back into the floor
        def getMatrix(c):
            return c and c.extra and c.extra.get('flatten', None)
        cb_matrix = getMatrix(cb)
        cf_matrix = getMatrix(cf)

        def getVector(c):
            return c and c.extra and c.extra.get('flatten_move', None)
        cb_vector = getVector(cb)
        cf_vector = getVector(cf)

        # revert elevation translation
        if cf_vector is not None:
            cf_array.applyTranslation(cf_vector)
            cf.applyTranslation(cf_vector)
        if cb_vector is not None:
            cb_array.applyTranslation(cb_vector)
            cb.applyTranslation(cb_vector)

        # flatten shape back into floor
        if cf_matrix is not None:
            cf_array.applyLinearTransform(cf_matrix)
            cf.applyLinearTransform(cf_matrix)
        if cb_matrix is not None:
            cb_array.applyLinearTransform(cb_matrix)
            cb.applyLinearTransform(cb_matrix)

        # determine clip rectange
        to2d = lambda p: (p[2], p[0])
        coords = []
        for card in (cf, cb):
            if card is None:
                continue
            vertices = card.getVertices()
            coords += [to2d(v) for v in vertices]
        origin, w, h = geometry.boundingRect(coords)
        display.setScale(w, h)
        bounds = (
            (origin[0],         origin[1]),
            (origin[0] + w,     origin[1]),
            (origin[0] + w, h + origin[1]),
            (origin[0],     h + origin[1])
            )

        # draw cards
        progressPcentFn(20)
        for card, color in (
            (cf, 'RED'),
            (cb, 'BLUE'),
            ):
            if card is None:
                continue
            vertices = card.getVertices()
            coords = [to2d(v) for v in vertices]

            # borders
            if preview:
                display.DrawPolygon(coords, 'WHITE', color)

            # bg
            if card.bg is not None:
                points = display.Rescales(coords)
                (x0, y0), w, h = geometry.boundingRect(points)
                bmp = card.bg.getScaled(w, h, preview)
                display.DrawBitmap(bmp, x0, y0)
                progressPcentFn(40)

        # display marquee images
        progressPcentFn(60)
        failed = False
        if self.show_image or not preview:
            images = []
            images_x = []
            images_y = []
            for card, array, color in (
                (cf, cf_array, 'RED'),
                (cb, cb_array, 'BLUE')
                ):
                if card is None:
                    continue

                ###corners = [to2d(v) for v in card.getVertices()]
                img_corners = []
                card_corners = []
                i = 0
                for u in 0, array.nodes1 - 1:
                    for v in 0, array.nodes2 - 1:
                        x, y = to2d(array.getVertexAt(u, v))
                        x, y = display.Rescale(x, y)
                        img_corners.append((x, y))

                vertices = card.getVertices()
                card_coords = [to2d(v) for v in vertices]
                card_coords = [display.Rescale(x, y) for x, y in card_coords]

                try:
                    img, dest_x, dest_y, pts = bitmap.makeFromPerspective(
                        self.bitmap,
                        display_w, display_h,
                        img_corners,
                        card_coords,
                        name=card.name,
                        use_thumbnail=preview, fast=preview)
                    if img is not None:
                        display.DrawBitmap(img, dest_x, dest_y)
                        images.append(img)
                    else:
                        failed = True
                except Exception, e:
                    traceback.print_exc()
                    print e
                    failed = True
                    pass


        # display marquee grid
        progressPcentFn(80)
        if (preview and not self.show_image) or failed:
            # draw marquee grids, clipped by cards
            for card, array, debug_color in (
                (cb, cb_array, 'BLUE'),
                (cf, cf_array, 'RED')
                ):
                if card is None:
                    continue

                color = debug_color if DEBUG else 'GRAY'
                i = 0
                corners = [to2d(v) for v in card.getVertices()]
                display.SetClip(corners)
                for u in range(array.nodes1 - 1):
                    for v in range(array.nodes2 - 1):
                        vertices = (
                            array.getVertexAt(u,         v),
                            array.getVertexAt(u + 1,     v),
                            array.getVertexAt(u + 1, v + 1),
                            array.getVertexAt(u,     v + 1))

                        corners = [to2d(v) for v in vertices]
                        display.DrawPolygon(corners,
                                            (255, 255, 255, 64),
                                            color)

                        if DEBUG:
                            mid = to2d(sum(vertices) / 4)
                            display.DrawText(str(i), mid[0], mid[1], color)
                            i += 1
            display.SetClip(None)

        if box:
            display.DrawPolygon(bounds, None, 'BLACK')

        progressPcentFn(99)

        return

    def renderCanvasHiQ(self, canvas):
        self.renderCanvas(canvas, preview=False)

    def renderScreen(self, frame):
        render_fullscreen.render(frame, self.renderCanvasHiQ)

    def renderImage(self, width, height, progressPcentFn=None):
        display = BitmapDisplay(width, height)
        self.renderDisplay(display, width, height, preview=False, box=True,
                           progressPcentFn=progressPcentFn)
        bmp = display.GetBitmap()
        return bmp


def createProjectionPoints(camera, card_back, card_front,
                           marquee, grid_m, grid_n):
    """
    Compute the anamorphosis projection points:
    Intersection points between lines thrown from the camera through
    the marquee divided as a grid, and the cards planes.
    """

    m_point1, m_point2, m_point3, m_point4 = marquee.getVertices()
    marquee_grid = shape.Grid(m_point1, m_point4, m_point2, m_point3,
                              grid_n, grid_m, name="M")
    a = camera
    shapes = []
    for card_name, card, color in (("CBP", card_back, "BLUE"),
                                   ("CFP", card_front, "RED")):
        if card is None:
            continue

        points = []
        card_plane = geometry.pointsToPlane(card.getVertices()[:3])
        p1, p2, p3 = [numpy.array(p) for p in card.getVertices()[:3]]

        for u in range(grid_n + 1):
            for v in range(grid_m + 1):
                b = marquee_grid.getVertexAt(u, v)
                point = geometry.lineIntersectsPlane(a, b, p1, p2, p3)

                name = "%d %d" % (u, v)
                #label = "(%d,%d)" % (u, v)
                label = None
                points.append(shape.Point(point, name=name, label=label))
        array = shape.Array(points, grid_n + 1, grid_m + 1, name=card_name)
        shapes.append(array)

    return shapes
