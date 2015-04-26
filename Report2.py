__author__ = 'seokhui'

from numpy import matrix

A1 = [[2, 4, -2], [4, 9, -3], [-2, -3, 7]]
b1 = [[2], [8], [10]]

A2 = [[1, 2], [4, 9]]
b2 = [[5], [9]]


def slu(A):   # http://pygments.org/demo/83380/
    L = [[0.0 for i in range(len(A))] for j in range(len(A))]
    U = [[0.0 for i in range(len(A))] for j in range(len(A))]
    try:
        for i in range(0, len(A)):
            L[i][0] = A[i][0]      # L:deside 1 column.
            U[0][i] = A[0][i]/A[0][0]   # U:deside 1 row.
        for k in range(1, len(A)):
            for i in range(0, k):
                L[i][k] = U[k][i] = 0.0    # initialize the element to be updated.
            for i in range(k, len(A)):
                L[i][k] = A[i][k]
                for m in range(0, k):
                    L[i][k] -= L[i][m] * U[m][k]
            U[k][k] = 1.0				# U:diagonal element is 1
            for i in range(k + 1, len(A)):
                U[k][i] = A[k][i]
                for m in range(0, k):
                    U[k][i] -= L[k][m] * U[m][i]
                U[k][i] /= L[k][k]
    except ZeroDivisionError:
        print("This matrix can't do LU-0 Decomposition.")
    return L, U


def slv(L, U, b):
    x = matrix(U).I * matrix(L).I * b
    return x

print("2 - (1) output by slu, slv :")
L, U = slu(A1)
x = slv(L, U, b1)
print(x, "\n")

print("2 - (2) output by slu, slv :")
L, U = slu(A2)
x = slv(L, U, b2)
print(x)