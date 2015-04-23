__author__ = 'seokhui_lee'

from numpy import matrix

A1 = [[2, 4, -2], [4, 9, -3], [-2, -3, 7]]
b1 = [[2], [8], [10]]

A2 = [[1, 2], [4, 9]]
b2 = [[5], [9]]


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
            multiplier = a[r][p]/pivots[p]
            b[r][0] = b[r][0] - multiplier*b[p][0]
            for temp in range(row):
                a[r][temp] = a[r][temp] - multiplier*a[p][temp]

        j += 1
        j = int(j % row)

    print(A1)
    print(b1)

by_gaussian_elimination(A1, b1)


def gausselim1(themat):
   for i in range(len(themat[0])):
      for j in range(i+1,len(themat)):
         m = themat[j][i]/themat[i][i]   # Ratio of (i,j) elt by (i,i) (diagonal) elt
         themat[j] = [themat[j][k]-m*themat[i][k] for k in range(len(themat[0]))]
