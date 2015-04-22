__author__ = 'seokhui'

from numpy import matrix
from numpy import linalg

A1 = matrix([[2, 4, -2], [4, 9, -3], [-2, -3, 7]])
b1 = matrix([[2], [8], [10]])

A2 = matrix([[1, 2], [4, 9]])
b2 = matrix([[5], [9]])


pivots1 = range(A1.size)


def by_inverse_matrix(a, b):
    # (Matrix variable).I means (Matrix variable)'s Inverse matrix
    inverse = a.I
    x = inverse*b
    print(x)

print("1.2 - (1) output by Inverse Matrix :")
by_inverse_matrix(A1, b1)

print("1.2 - (2) output by Inverse Matrix :")
by_inverse_matrix(A2, b2)