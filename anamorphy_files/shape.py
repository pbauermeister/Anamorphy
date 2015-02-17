"""
This module defines:
 * the basis Shape class, containing its list of vertices,
 * complexer shapes, with their specific attributes and display calls.

Final rendering is not done here. The computed 2D points reside in the
projective plane, and need to be rescaled to fit the size and
orientation of the display device (graphical canvas). Hence, the final
rendering is done by the display, which is passed as argument to each
render() method.
"""
import perspective
import vector
import copy
import numpy
import bitmap
import geometry

shapes = {}


def getShape(name):
    return shapes.get(name, None)


def copyShape(src):
    """
    Deep copies a shape. Only the bg member cannot copied, so copy as
    reference.
    """
    if src is None:
        return None
    else:
        bg, src.bg = src.bg, None
        dest = copy.deepcopy(src)
        src.bg = dest.bg = bg
        return dest


def clearShapes():
    shapes.clear()


class Shape(object):
    """
    Basis abstract class for all shapes.
    """
    def __init__(self, children, name=None, extra=None):
        self.children = children
        self.name = name
        self.extra = extra
        if name is not None:
            shapes[name] = self
        self.rpoints = None
        self.bg = None

    def render(self, display, perspective, show=True, fast=False):
        assert()

    def getVertices(self):
        vertices = []
        for c in self.getLeafComponents():
            vertices.append(c.getVertex())
        return vertices

    def getLeafComponents(self):
        if not self.children:
            return [self]
        else:
            return [c for c in self.getChildComponents() if not c.children]

    def getChildComponents(self):
        if not self.children:
            return [self]
        else:
            comps = []
            for c in self.children:
                comps += c.getChildComponents()
            return comps

    def getPerspectivePoints(self, perspective):
        v = self.getVertices()
        return perspective.computePoints(v)

    def get2dPoints(self):
        return self.rpoints

    def applyTranslation(self, vector):
        for c in self.getLeafComponents():
            p2 = c.getVertex() + vector
            c.setVertex(p2)

    def applyLinearTransform(self, matrix):
        for c in self.getLeafComponents():
            p2 = vector.linearTransform(c.getVertex(), matrix)
            c.setVertex(p2)

    def applyAffineTransform(self, matrix):
        for c in self.getLeafComponents():
            p2 = vector.affineTransform(c.getVertex(), matrix)
            c.setVertex(p2)


class Vertex(Shape):
    """
    Basis vertex. Solely intended to hold one vertex, and be subject
    to transforms.
    """
    def __init__(self, at,
                 name=None):
        self.vertex = at
        super(Vertex, self).__init__([], name=name)

    def getVertex(self):
        return self.vertex

    def setVertex(self, v):
        self.vertex = v


class Point(Vertex):
    """
    Point shape: may have an associated label; can be rendered.
    """
    def __init__(self, at, label=None,
                 name=None,
                 lineColor='BLUE',
                 textColor='BLUE'):
        self.lineColor = lineColor
        self.textColor = textColor
        self.label = label
        super(Point, self).__init__(at, name=name)

    def render(self, display, perspective, show=True, fast=False):
        points = self.getPerspectivePoints(perspective)
        (x, y), = points
        self.rpoints = display.DrawPoint(x, y, self.lineColor, show)
        if show:
            if self.label:
                display.DrawText(" " + self.label, x, y, self.textColor)


class Label(Vertex):
    """
    Label shape: just a text.
    """
    def __init__(self, at, label,
                 name=None,
                 textColor='BLUE'):
        self.textColor = textColor
        self.label = label
        super(Label, self).__init__(at, name=name)

    def render(self, display, perspective, show=True, fast=False):
        points = self.getPerspectivePoints(perspective)
        if show:
            (x, y), = points
            display.DrawText(self.label, x, y, self.textColor)


class Axis(Shape):
    """
    Axis shape: segment and label.
    """
    def __init__(self, fro, to, label,
                 lineColor='BLUE',
                 textColor='BLUE'):

        f = Point(fro, lineColor=lineColor, textColor=textColor)
        t = Point(to, lineColor=lineColor, textColor=textColor)
        super(Axis, self).__init__([f, t])
        self.label = label
        self.lineColor = lineColor
        self.textColor = textColor

    def render(self, display, perspective, show=True, fast=False):
        points = self.getPerspectivePoints(perspective)
        (x1, y1), (x2, y2) = points
        self.rpoints = display.DrawLine(x1, y1, x2, y2, self.lineColor, show)
        if show:
            display.DrawText(self.label, x2, y2, self.textColor)


class Face(Shape):
    """
    Face shape: any number of vertices, defining a colored surface.

    If the face is not flat, erronous rendering may occur.
    """
    def __init__(self, vertices,
                 fillColor=(255, 255, 255, 192),
                 lineColor='BLACK',
                 name=None,
                 extra=None,
                 bg=None):
        points = [Point(v) for v in vertices]
        self.fillColor = fillColor
        self.lineColor = lineColor
        super(Face, self).__init__(points, name, extra=extra)
        self.bg = bg

    def render(self, display, perspective, show=True, fast=False):
        points = self.getPerspectivePoints(perspective)
        if self.bg and not fast:
            self.rpoints = display.DrawPolygon(points, self.fillColor,
                                               None, show)
            if show:
                cc = self.get2dPoints()
                img_corners = (cc[1], cc[0], cc[2], cc[3])
                img_corners, x0, y0 = geometry.shiftToOrigin(img_corners)

                try:
                    img, dest_x, dest_y, pts = bitmap.makeFromPerspective(
                        self.bg,
                        1000, 1000,  # display_w, display_h,
                        img_corners,
                        None,
                        use_thumbnail=True, fast=fast)
                    display.DrawBitmap(img, x0, y0)
                except Exception, e:
                    import traceback
                    traceback.print_exc()
                    print e

                self.rpoints = display.DrawPolygon(points, None,
                                                   self.lineColor, show)
        else:
            self.rpoints = display.DrawPolygon(points, self.fillColor,
                                               self.lineColor, show)


class Array(Shape):
    """
    Array shape: it packs a series of Points that are can be accessed
    by two indices.
    """
    def __init__(self, points,
                 nodes1, nodes2,
                 name=None):
        self.nodes1 = nodes1
        self.nodes2 = nodes2
        self.points = points
        super(Array, self).__init__(self.points, name)

    def render(self, display, perspective, show=True, fast=False):
        for each in self.points:
            each.render(display, perspective, show, fast)

    def _index(self, u, v):
        return u * self.nodes2 + v

    def getVertexAt(self, u, v):
        return self.points[self._index(u, v)].getVertex()


class Grid(Array):
    """
    Grid shape: based on its four corners and number of subdivisions,
    it generates an array of Points packed as an Array.

    corners:
      a  b
      c  d
    """
    def __init__(self, a, b, c, d,
                 edges1, edges2,
                 lineColor='BLUE',
                 textColor='BLUE',
                 name=None):
        points = []
        names = []
        labels = []
        a, b, c, d = [numpy.array(x) for x in (a, b, c, d)]
        ac = (c - a) / edges1
        bd = (d - b) / edges1
        nodes1 = edges1 + 1
        nodes2 = edges2 + 1
        for u in range(nodes1):
            p = a + ac * u
            q = b + bd * u
            for v in range(nodes2):
                pq = (q - p) / edges2
                at = p + pq * v
                pt = Point(at, "%s(%d,%d)" % (name, u, v),
                           lineColor=lineColor, textColor=textColor)
                points.append(pt)
                names.append("%s(%d,%d)" % (name, u, v))
                labels.append("(%d,%d)" % (u, v))
        super(Grid, self).__init__(points, nodes1, nodes2,
                                   name=name)
