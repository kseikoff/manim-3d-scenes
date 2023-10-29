import numpy as np
from math import cos, sin, degrees, pi

default_vertices = np.array([
        [-1, 1, 1],
        [1, 1, 1],
        [1, -1, 1],
        [-1, -1, 1],
        [-1, 1, -1],
        [1, 1, -1],
        [1, -1, -1],
        [-1, -1, -1]
])

scale_matrix_A = np.array([
    [0.5, 0, 0, 0],
    [0, 0.5, 0, 0],
    [0, 0, 0.5, 0],
    [0, 0, 0, 0.5]
])

scale_matrix_B = np.array([
    [2, 0, 0, 0],
    [0, 2, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 2]
])

scale_matrix_C = np.array([
    [1.5, 0, 0, 0],
    [0, 1.5, 0, 0],
    [0, 0, 0.7, 0],
    [0, 0, 0, 0.7]
])

move_matrix_A = np.array([
    [1, 0, 0, 2],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

move_matrix_B = np.array([
    [1, 0, 0, -1.5],
    [0, 1, 0, -2],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

move_matrix_C = np.array([
    [1, 0, 0, -1.5],
    [0, 1, 0, 1],
    [0, 0, 1, 1.5],
    [0, 0, 0, 1]
])

move_matrix_D = np.array([
    [1, 0, 0, -1.5],
    [0, 1, 0, 1.5],
    [0, 0, 1, -1],
    [0, 0, 0, 1]
])

move_matrix_E = np.array([
    [1, 0, 0, 3.5],
    [0, 1, 0, 0.5],
    [0, 0, 1, -1.5],
    [0, 0, 0, 1]
])

rotate_matrix_X_axis = np.array([
    [1, 0, 0, 0],
    [0, cos(degrees(2*pi)), -sin(degrees(2*pi)), 0],
    [0, sin(degrees(2*pi)), cos(degrees(2*pi)), 0],
    [0, 0, 0, 1]
])

rotate_matrix_Y_axis = np.array([
    [cos(degrees(pi/2)), 0, sin(degrees(pi/2)), 0],
    [0, 1, 0, 0],
    [-sin(degrees(pi/2)), 0, cos(degrees(pi/2)), 0],
    [0, 0, 0, 1]
])

rotate_matrix_Z_axis = np.array([
    [cos(degrees(pi)), -sin(degrees(pi)), 0, 0],
    [sin(degrees(pi)), cos(degrees(pi)), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])