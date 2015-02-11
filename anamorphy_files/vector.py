"""
This module implements vectors transforms by matrices.
"""
import numpy
import math


def norm(vector):
    return vector / math.sqrt(numpy.dot(vector, vector.conj()))


def _extend4(vector):
    vx, vy, vz = vector
    return numpy.array([vx, vy, vz, 1])


def _reduce3(vector):
    vx, vy, vz, vw = vector
    return numpy.array([vx, vy, vz])


def linearTransform(vector, matrix):
    return numpy.dot(matrix, vector)


def affineTransform(vector, matrix):
    vector = _extend4(vector)
    vector = numpy.dot(matrix, vector)
    return _reduce3(vector)


def affineTransform4(vector, matrix):
    vector = _extend4(vector)
    vector = numpy.dot(matrix, vector)
    return vector


def affineTransforms(vectors, matrix):
    new_vectors = []
    for vector in vectors:
        new_vector = transform(vector, matrix)
        new_vectors.append(new_vector)
    return new_vectors
