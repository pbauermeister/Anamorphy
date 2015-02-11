"""
This module does all the perspective computation, taking into account
the camera (with its location, target, field-of-view).

It computes the 2D projection of 3D points.

The computations closely follow the excellent article:
http://www.kmjn.org/notes/3d_rendering_intro.html

The computations use the numpy library, and in particular the arrays
(http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html) which
are providing matrix operations (vector and matrix products).
"""

import math
import numpy
import vector

# Coordinates:
#
#          +y (verical axis)
#          |
#          |
#          |_________+x
#         /
#  Cam   /   (floor plane)
#      +z
#
# The camera is typically located rather along the Z axis, aiming
# somewhat at the origin.


class Perspective(object):
    def __init__(self,
                 camera_azimuth,
                 camera_altitude,
                 camera_distance,
                 camera_fov):
        self.camera_azimuth = camera_azimuth
        self.camera_altitude = camera_altitude
        self.camera_distance = camera_distance
        self.camera_fov = camera_fov

        near = -30
        far = -60
        fov = math.radians(camera_fov)
        ratio = 1.333
        lookat = numpy.array([0, 0, 0])

        #
        # Camera
        #

        camera = vector.norm(numpy.array([0, 0, 1])) * camera_distance

        alti = math.radians(-camera_altitude)
        c = math.cos(alti)
        s = math.sin(alti)
        cameraRotateAroundX = numpy.array([
                [1, 0,  0, 0],
                [0, c, -s, 0],
                [0, s,  c, 0],
                [0, 0,  0, 1],
                ])

        azim = math.radians(camera_azimuth)
        c = math.cos(azim)
        s = math.sin(azim)
        cameraRotateAroundY = numpy.array([
                [ c, 0, s, 0],
                [ 0, 1, 0, 0],
                [-s, 0, c, 0],
                [ 0, 0, 0, 1],
                ])

        self.cameraRotate = numpy.dot(cameraRotateAroundY, cameraRotateAroundX)
        self.camera = vector.affineTransform(camera, self.cameraRotate)
        #print "Camera", camera
        #print "Lookat", lookat

        #
        # Perspective transform
        #

        self.width = width = -2 * near * math.tan(fov / 2)
        self.height = height = width / ratio
        #print "Width", width
        #print "Height", height
        m11 = 2 * near / width
        m22 = 2 * near / height
        m33 = -(far + near) / (far - near)
        m34 = -2 * far * near / (far - near)
        self.perspectiveTransform = numpy.array([
                [m11,   0,   0,   0],
                [  0, m22,   0,   0],
                [  0,   0, m33, m34],
                [  0,   0,  -1,   0],
                ])
        #print perspectiveTransform

        #
        # Camera look transform
        #

        up = numpy.array([0, 1, 0])
        n = vector.norm(lookat - self.camera)
        u = vector.norm(numpy.cross(up, n))
        v = numpy.cross(n, u)
        ux, uy, uz = u
        vx, vy, vz = v
        nx, ny, nz = n
        self.cameraLookTransform = numpy.array([
                [ux, uy, uz, 0],
                [vx, vy, vz, 0],
                [nx, ny, nz, 0],
                [ 0,  0,  0, 1],
                ])
        #print cameraLookTransform

        #
        # Camera translation transform
        #

        tx, ty, tz = -self.camera
        self.cameraLocationTransform = numpy.array([
                [1, 0, 0, tx],
                [0, 1, 0, ty],
                [0, 0, 1, tz],
                [0, 0, 0,  1],
                ])
        #print cameraLocationTransform

        #
        # Final transform
        #

        self.transform = numpy.dot(numpy.dot(self.perspectiveTransform,
                                             self.cameraLookTransform),
                                   self.cameraLocationTransform)
        #print "Transform", self.transform

    def computePoint(self, vertex, matrix):
        point = vector.affineTransform4(vertex, matrix)
        w = point[3]
        x, y, z, w = point / w
        sx = x * self.width / 2
        sy = -y * self.height / 2
        return sx, sy

    def computePoints(self, vertices):
        matrix = self.transform
        path2D = []
        for vertex in vertices:
            path2D.append(self.computePoint(vertex, matrix))
        return path2D

    def getCameraRotateMatrix(self):
        return self.cameraRotate

    def getCamera(self):
        return self.camera
