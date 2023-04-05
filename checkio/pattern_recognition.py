import numpy as np


def get_submatrix(image, x, y, height, width):
    return np.matrix(image)[y:y+height, x:x+width]


def checkio(pattern, image):
    pattern_w = len(pattern[0])
    pattern_h = len(pattern)
    np_pattern = get_submatrix(pattern, 0, 0, pattern_h, pattern_w).tolist()
    for i in range(len(image)):
        for j in range(len(image[0])):
            submatrix = get_submatrix(image, j, i, pattern_h, pattern_w)
            if np_pattern == submatrix.tolist():
                for y, line in enumerate(pattern):
                    for x, el in enumerate(line):
                        image[y+i][x+j] = 3 if pattern[y][x] else 2
    return image

assert checkio([[1, 0], [1, 1]],
               [[0, 1, 0, 1, 0],
                [0, 1, 1, 0, 0],
                [1, 0, 1, 1, 0],
                [1, 1, 0, 1, 1],
                [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                                      [0, 3, 3, 0, 0],
                                      [3, 2, 1, 3, 2],
                                      [3, 3, 0, 3, 3],
                                      [0, 1, 1, 0, 0]]
assert checkio([[1, 1], [1, 1]],
               [[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]]) == [[3, 3, 1],
                                [3, 3, 1],
                                [1, 1, 1]]
assert checkio([[0, 1, 0], [1, 1, 1]],
               [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [[0, 2, 3, 2, 0, 0, 0, 2, 3, 2],
                                                     [0, 3, 3, 3, 0, 0, 0, 3, 3, 3],
                                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                     [0, 0, 0, 0, 2, 3, 2, 0, 0, 0],
                                                     [2, 3, 2, 0, 3, 3, 3, 0, 1, 0],
                                                     [3, 3, 3, 0, 0, 0, 0, 0, 1, 1],
                                                     [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                                                     [0, 0, 1, 0, 0, 0, 2, 3, 2, 0],
                                                     [0, 1, 1, 0, 0, 0, 3, 3, 3, 0],
                                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


"""
def checkio(N, H, R=range, L=len):
    for i in R(L(H)):
        for j in R(L(H[i])):
            I, J = i + L(N), j + L(N[0])
            if [r[j:J] for r in H[i:I]] == N:
                for k in R(i, I):
                    for l in R(j, J):
                        H[k][l] += 2
    return H
"""

"""
def checkio( A, B) :
    for i in range(len(B)) :
        for j in range(len(B[0])) :
            try :
                if all( A[k][l] == B[i+k][j+l] for k in range(len(A)) for l in range(len(A[0]))) :
                    for k in range(len(A)) :
                        for l in range(len(A[0])) :
                            B[i+k][j+l] += 2
            except :
                pass
    return B
"""

"""
from itertools import product

def checkio(pattern, image):
    N1, N2 = len(image), len(image[0])
    M1, M2 = len(pattern), len(pattern[0])
    for i, j in product(range(N1-M1+1), range(N2-M2+1)):
        if all(image[i+k][j+l] == pattern[k][l]
               for k, l in product(range(M1), range(M2))):
            for k, l in product(range(M1), range(M2)):
                image[i+k][j+l] = 2 + pattern[k][l]
    return image
"""