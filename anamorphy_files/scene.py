"""
This module defines the scene, consisting of various objects.

The objects can be created or moved via object-specific functions
provided here.
"""
import math
import shape
import numpy
import geometry
import anamorphosis
import perspective
import traceback


class Scene(object):
    """
    The scene is essentially a list of shapes, that can be
    manipulated.
    """
    def __init__(self):
        self.card_width = None
        self.card_height = None
        self.card_fold = None
        self.card_angle = None
        self.camera_matrix = None
        self.tiles_div1 = None
        self.tiles_div2 = None
        self.card_bg_bmp = None

    def getShapes(self):
        shape.clearShapes()
        c = math.cos(self.card_angle)
        s = math.sin(self.card_angle)

        cb_bg = None
        cf_bg = None

        if self.card_fold == 0:
            h = self.card_width / 2
            w = self.card_height / 2

            cb = (
                ([0, 0,  h],
                 [w, 0,  h],
                 [w, 0, -h],
                 [0, 0, -h]),
                {})

            cf = (
                # face
                ([-w * c, w * s,  h],
                 [     0,     0,  h],
                 [     0,     0, -h],
                 [-w * c, w * s, -h]),
                {'flatten': numpy.array(([c, -s, 0],
                                         [s,  c, 0],
                                         [0,  0, 1]))
                  }
                )

            cb_bg = self.card_bg_bmp and self.card_bg_bmp.getBottom()
            cf_bg = self.card_bg_bmp and self.card_bg_bmp.getTop()

        if self.card_fold == 1:
            h = self.card_width / 2
            w = self.card_height / 2

            cf = (
                ([-w, 0,  h],
                 [ 0, 0,  h],
                 [ 0, 0, -h],
                 [-w, 0, -h]),
                {})

            cb = (
                ([    0,      0,  h],
                 [w * c, -w * s,  h],
                 [w * c, -w * s, -h],
                 [    0,      0, -h]),
                {'flatten': numpy.array(([c, -s, 0],
                                         [s,  c, 0],
                                         [0,  0, 1]))
                  }
                )

            cb_bg = self.card_bg_bmp and self.card_bg_bmp.getBottom()
            cf_bg = self.card_bg_bmp and self.card_bg_bmp.getTop()

        elif self.card_fold == 2:
            h = self.card_width / 2
            w = self.card_height / 2

            rot_along_y = numpy.array(([ c, 0, s],
                                       [ 0, 1, 0],
                                       [-s, 0, c]))

            cb = (
                ([0,  w, h],
                 [0, -w, h],
                 [0, -w, 0],
                 [0,  w, 0]),
                {'flatten': geometry.ROT90_ALONG_Z}
                )

            cf = (
                ([    0,  w,      0],
                 [    0, -w,      0],
                 [h * s, -w, -h * c],
                 [h * s,  w, -h * c]),
                {'flatten': numpy.dot(geometry.ROT90_ALONG_Z, rot_along_y)}
                )

            cb_bg = self.card_bg_bmp and self.card_bg_bmp.getLeft()
            cf_bg = self.card_bg_bmp and self.card_bg_bmp.getRight()

        elif self.card_fold == 3:
            h = self.card_width / 2
            w = self.card_height / 2

            rot_along_y = numpy.array(([ c, 0, s],
                                       [ 0, 1, 0],
                                       [-s, 0, c]))

            cf = (
                ([0,  w,  0],
                 [0, -w,  0],
                 [0, -w, -h],
                 [0,  w, -h]),
                {'flatten': geometry.ROT90_ALONG_Z}
                )

            cb = (
                ([-h * s,  w, h * c],
                 [-h * s, -w, h * c],
                 [0, -w, 0],
                 [0,  w, 0]),
                {'flatten': numpy.dot(geometry.ROT90_ALONG_Z, rot_along_y)}
                )

            cb_bg = self.card_bg_bmp and self.card_bg_bmp.getLeft()
            cf_bg = self.card_bg_bmp and self.card_bg_bmp.getRight()

        elif self.card_fold == 4:
            h = self.card_width / 2
            w = self.card_height / 2
            cb = None
            cf = (
                ([-w * c,  w * s,  h],
                 [ w * c, -w * s,  h],
                 [ w * c, -w * s, -h],
                 [-w * c,  w * s, -h]),
                {'flatten': numpy.array(([c, -s, 0],
                                         [s,  c, 0],
                                         [0,  0, 1]))
                  }
                )

            cb_bg = None
            cf_bg = self.card_bg_bmp and self.card_bg_bmp

        # move points
        def move(points, translation):
            new_points = []
            for point in points:
                new_points.append(point + translation)
            return new_points

        def add_dict(dic, more):
            res = {}
            res.update(dic)
            res.update(more)
            return res

        elevation = numpy.array(([0, self.card_elevation, 0]))
        move_back = {'flatten_move': -elevation}

        # create card shapes
        card_back = shape.Face(move(cb[0], elevation),
                               name="card_back",
                               lineColor='BLUE',
                               extra=add_dict(cb[1], move_back),
                               bg=cb_bg
                               ) if cb else None
        card_front = shape.Face(move(cf[0], elevation),
                                name="card_front",
                                lineColor='RED',
                                extra=add_dict(cf[1], move_back),
                                bg=cf_bg
                                ) if cf else None

        # create marquee shape
        mw = self.marquee_width / 2
        mh = self.marquee_height / 2
        md = self.camera_distance - self.marquee_distance
        mx = self.marquee_hoff
        my = self.marquee_voff
        marquee = shape.Face(
                ([-mw + mx, -mh + my, md],
                 [ mw + mx, -mh + my, md],
                 [ mw + mx,  mh + my, md],
                 [-mw + mx,  mh + my, md],
                 ),  # initial marquee position is perp along the Z axis
                fillColor=(255, 255, 255, 32), lineColor='GRAY',
                name="marquee")
        # rotate the marquee so that it exactly faces the camera
        marquee.applyAffineTransform(self.camera_matrix)

        # assemble scene
        scene = [
            card_back,
            card_front,
            # card_bg_back,
            # card_bg_front,
            shape.Axis([0, 0, 0], [ 0, 16,  0], "y"),
            shape.Axis([0, 0, 0], [16,  0,  0], "x"),
            shape.Axis([0, 0, 0], [ 0,  0, 16], "z"),
            marquee,
            ]

        #scene.append(shape.Point([200, 0, 0], "X"))
        #for z in range(-30, 5):
        #    scene.append(shape.Point([0, 0, z*50], ""))

        #
        # Intersects
        #

        # marquee pyramid
        shapes = anamorphosis.createProjectionPoints(
            self.camera_pos,
            card_back, card_front,
            marquee,
            self.tiles_div1, self.tiles_div2)
        for each in shapes:
            scene.append(each)

        return scene

    def setCard(self, width, height, fold, angle, elevation, card_bg_bmp):
        self.card_width = width
        self.card_height = height
        self.card_fold = fold
        self.card_angle = math.radians(angle)
        self.card_elevation = elevation
        self.card_bg_bmp = card_bg_bmp

    def setMarquee(self, camera_matrix, camera_distance,
                   marquee_width, marquee_height, marquee_distance,
                   marquee_hoff, marquee_voff):
        self.camera_matrix = camera_matrix
        self.camera_distance = camera_distance
        self.marquee_width = marquee_width
        self.marquee_height = marquee_height
        self.marquee_distance = marquee_distance
        self.marquee_hoff = marquee_hoff
        self.marquee_voff = marquee_voff

    def setCameraPos(self, camera_pos):
        self.camera_pos = camera_pos

    def setMarqueeTiles(self, m, n):
        self.tiles_div1 = m
        self.tiles_div2 = n

    def render(self, display, getValueFn,
               marquee_ratio, marquee_bmp, 
               card_bg_bmp, 
               setPosFn):
        # camera pos indication
        if setPosFn is not None:
            theta = math.radians(90 - getValueFn("camera_altitude"))
            phi = math.radians(90 - getValueFn("camera_azimuth"))
            r = getValueFn("camera_distance")
            y = r * math.cos(theta)
            x = r * math.cos(phi) * math.sin(theta)
            z = r * math.sin(phi) * math.sin(theta)
            pos = "x:%d  y:%d  z:%d" % (x, y, z)
            setPosFn(pos)
    
        # create perspective
        persp = perspective.Perspective(
            getValueFn("camera_azimuth"),
            getValueFn("camera_altitude"),
            getValueFn("camera_distance"),
            getValueFn("camera_fov"))
    
        # adjust scene (position objects)
        self.setCard(
            getValueFn("card_width"),
            getValueFn("card_height"),
            getValueFn("card_fold"),
            getValueFn("card_angle"),
            getValueFn("card_elevation"),
            card_bg_bmp if getValueFn("card_background_show") else None
        )
        self.setMarquee(
            persp.getCameraRotateMatrix(),
            getValueFn("camera_distance"),
            getValueFn("marquee_width"),
            getValueFn("marquee_width") * marquee_ratio,
            getValueFn("marquee_distance"),
            getValueFn("marquee_hoff"),
            getValueFn("marquee_voff")
        )
        self.setCameraPos(persp.getCamera())
        self.setMarqueeTiles(5, 5)
    
        # compute 3D -> 2D
        shapes = self.getShapes()
        marquee_show = getValueFn("marquee_show")
        for each in shapes:
            if each is None:
                continue
            if marquee_show:
                show = each.name not in ("marquee", "CBP", "CFP")
            else:
                show = True
            try:
                each.render(display, persp, show=show)
            except ValueError, e:
                traceback.print_exc()
                print e
                pass  # some point cannot be rendered
            except OverflowError, e:
                traceback.print_exc()
                print e
                pass  # some point cannot be rendered
    
        # render marquee image
        if getValueFn("marquee_show") and marquee_bmp is not None:
            marquee_2d_points = shape.getShape("marquee").get2dPoints()
            (x, y), w, h = geometry.boundingRect(marquee_2d_points)
    
            bmp = marquee_bmp.getScaled(w, h)
            display.DrawBitmap(bmp, x, y)
            
        return