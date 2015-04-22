__author__ = 'seokhui'

from numpy import matrix
from numpy import linalg

A1 = [[2, 4, -2], [4, 9, -3], [-2, -3, 7]]
b1 = [[2], [8], [10]]

A2 = [[1, 2], [4, 9]]
b2 = [[5], [9]]

# 1-(1)
def by_gaussian_elimination(a, b):
    row = int(len(a[0]))
    pivots = []

    j = 0
    for p in range(row):
        i = 0
        while True:
            if not(a[p][j] == 0):
                break
            temp = a[p]
            i += 1
            i = int((i+1) % row)
            a[p] = a[i]
            a[i] = temp

        pivots.append(a[p][j])

        for r in range(p+1, row):
            for temp in range(row):
                a[r][temp] = a[r][temp] - (a[r][p]/pivots[p])*a[p][temp]

        j += 1
        j = int(j % row)

    print("y = "+str(b[2][0]/a[2][2]))


by_gaussian_elimination(A1, b1)

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