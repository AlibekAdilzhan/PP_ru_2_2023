# pip install numpy
import numpy as np

A = np.array([
    [1, 2],
    [4, 1],
    # [1, 0, 7],
])

B = np.array([
    [1, 0],
    [0, 1],
    # [2, 0, 1],
])

C = np.dot(A, B)
print(C)
