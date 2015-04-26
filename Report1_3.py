__author__ = 'seokhui_lee'

from scipy.linalg import lu

A1 = [[2, 4, -2], [4, 9, -3], [-2, -3, 7]]
b1 = [[2], [8], [10]]

A2 = [[1, 2], [4, 9]]
b2 = [[5], [9]]

print("1.3 - (1) output by A=LU :")
L, U = lu(A1, True)
print("L =\n", L)
print("U =\n", U, "\n")
print("1.3 - (2) output by A=LU :")
L, U = lu(A2, True)
print("L =\n", L)
print("U =\n", U, "\n")