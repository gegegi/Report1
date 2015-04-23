__author__ = 'seokhui'

from numpy import matrix

A1 = [[2, 4, -2], [4, 9, -3], [-2, -3, 7]]
b1 = [[2], [8], [10]]

A2 = [[1, 2], [4, 9]]
b2 = [[5], [9]]

# 1-(2)
def by_inverse_matrix(l, b):
    a = matrix(l)
    # (Matrix variable).I means (Matrix variable)'s Inverse matrix - numpy.matrix
    inverse = a.I
    x = inverse * b
    print(x)


print("1.2 - (1) output by Inverse Matrix :")
by_inverse_matrix(A1, b1)

print("1.2 - (2) output by Inverse Matrix :")
by_inverse_matrix(A2, b2)
