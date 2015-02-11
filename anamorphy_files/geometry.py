"""
This module provides various functions for 3D and 2D geometry.
"""
import numpy

#
# 3D GEOMETRY CONSTANTS
#

ROT90_ALONG_Z = numpy.array((
        [0, -1,  0],
        [1,  0,  0],
        [0,  0,  1]))


#
# 3D GEOMETRY FUNCTIONS
#

def norm(v):
    return v / numpy.linalg.norm(v)


def pointsToPlane(three_points):
    p1, p2, p3 = three_points
    # http://easycalculation.com/analytical/cartesian-plane-equation.php
    ax, ay, az = p1
    bx, by, bz = p2
    cx, cy, cz = p3
    a = (by - ay) * (cz - az) - (cy - ay) * (bz - az)
    b = (bz - az) * (cx - ax) - (cz - az) * (bx - ax)
    c = (bx - ax) * (cy - ay) - (cx - ax) * (by - ay)
    d = -(a * ax + b * ay + c * az)
    return a, b, c, d


def planesIntersect(p1, p2, p3):
    # solve (x,y,z) for:
    #   | a1 b1 c1 |   |x|   |d1|
    #   | a2 b2 c2 | * |y| = |d2|
    #   | a3 b3 c3 |   |z|   |d3|
    # where a,b,c,d are the cartesian coefficient of plane p.
    #
    # In other words, solve M * p = D

    # load coefficients and form M
    a1, b1, c1, d1 = p1
    a2, b2, c2, d2 = p2
    a3, b3, c3, d3 = p3
    m = numpy.array([
            [a1,  b1,  c1],
            [a2,  b2,  c2],
            [a3,  b3,  c3]
            ])
    # form D
    d = numpy.array([-d1, -d2, -d3])

    # find point
    result = numpy.linalg.solve(m, d)
    return result


def lineIntersectsPlane(a, b, p1, p2, p3):
    # http://mathworld.wolfram.com/Line-PlaneIntersection.html
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    x3, y3, z3 = p3
    x4, y4, z4 = a
    x5, y5, z5 = b

    m1 = numpy.array([
            [ 1,  1,  1,  1],
            [x1, x2, x3, x4],
            [y1, y2, y3, y4],
            [z1, z2, z3, z4]
            ])
    m2 = numpy.array([
            [ 1,  1,  1,       0],
            [x1, x2, x3, x5 - x4],
            [y1, y2, y3, y5 - y4],
            [z1, z2, z3, z5 - z4]
            ])

    d1 = numpy.linalg.det(m1)
    d2 = numpy.linalg.det(m2)
    t = -d1 / d2
    result = a + (b - a) * t
    return result


#
# 2D GEOMETRY
#

def boundingBox(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    x0, x1 = min(xs), max(xs)
    y0, y1 = min(ys), max(ys)
    return (x0, y0), (x1, y1)


def boundingRect(points):
    (x0, y0), (x1, y1) = boundingBox(points)

    origin = (x0, y0)
    w, h = x1 - x0, y1 - y0
    return origin, w, h


def shiftToOrigin(points):
    (x0, y0), (x1, y1) = boundingBox(points)
    points = [(x - x0, y - y0) for x, y in points]
    return points, x0, y0
