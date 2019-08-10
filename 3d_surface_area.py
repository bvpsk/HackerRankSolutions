#!/bin/python3
# Link : https://www.hackerrank.com/challenges/3d-surface-area/problem
#
#
#   The logic here is that, at any given location, the surface area of that grid location depends on the number of
#   blocks present at that location as,    count = 6 + (n - 1)*4 where n is no. of blocks.
#   we first calculate the total surface area and then reduce the surface area depending on no. of blocks
#   present in its neighboring locations.
#


import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.


def surfaceArea(A):

    cl = 0
    r = len(A)
    c = len(A[0])
    for i in range(r):
        for j in range(c):
            cnt = 6 + 4 * (A[i][j] - 1)
            if i - 1 >= 0:
                # print("i-1")
                # cnt -= abs(A[i - 1][j] - A[i][j])
                cnt -= min(A[i - 1][j] , A[i][j])

            if i + 1 < r:
                # print("i+1")
                cnt -= min(A[i + 1][j] , A[i][j])
                # cnt -= abs(A[i + 1][j] - A[i][j])
            if j - 1 >= 0:
                # print("j-1")
                cnt -= min(A[i][j - 1] , A[i][j])
                # cnt -= abs(A[i][j - 1] - A[i][j])
            if j + 1 < c:
                # print("j+1")
                cnt -= min(A[i][j + 1] , A[i][j])
                # cnt -= abs(A[i][j + 1] - A[i][j])
            # print(cnt)
            cl += cnt
    return cl






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
