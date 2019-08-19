#!/bin/python3
# Link : https://www.hackerrank.com/challenges/two-pluses/problem
#
# My Idea here is to find all plusses and then finding all possible pair areas and then returning the max of them.
#
#
#
#
#
#
#


import math
import os
import random
import re
import sys

def checkVicinity(grid, i, j, r, c, k):
    if j + k < c:
        if grid[i][j + k] != "G":
            return 0
    else:
        return 0

    if j - k >= 0:
        if grid[i][j - k] != "G":
            return 0
    else:
        return 0

    if i - k >= 0:
        if grid[i - k][j] != "G":
            return 0
    else:
        return 0

    if i + k < r:
        if grid[i + k][j] != "G":
            return 0
    else:
        return 0
    return 1

def isOverlapped(grid, a, b):
    x = a[0][0]
    y = a[0][1]
    a_s = [[x, y]]
    peg = a[1]
    for i in range(1, peg + 1):
        a_s.append([x, y + i])
        a_s.append([x, y - i])
        a_s.append([x + i, y])
        a_s.append([x - i, y])
    if b[0][0] == x and b[0][1] == y:
        return 1
    x = b[0][0]
    y = b[0][1]
    peg = b[1]
    # print(a_s, "from a")
    for i in range(1, peg + 1):
        if [x, y + i] in a_s or [x, y - i] in a_s or [x + i, y] in a_s or [x - i, y] in a_s:
            # print([x, y + i], [x, y - i], [x + i, y], [x - i, y], "from b")
            return 1
    return 0





# Complete the twoPluses function below.
def twoPluses(grid):
    track = []
    r = len(grid)
    c = len(grid[0])
    for i in range(r):
        for j in range(c):
            if grid[i][j] == "G":
                k = 1
                while checkVicinity(grid, i, j, r, c, k):
                    k += 1
                # track.append(((i, j), 4*(k-1) + 1))
                track.append(((i, j), k-1))
    track = sorted(track, key = lambda x : x[1])[::-1]
    print(track)
    t = len(track)
    ans = []
    for i in range(t):
        a = track[i]
        for j in range(i+1, t):
            b = track[j]
            if not isOverlapped(grid, a, b):
                # print(a, b, i, j, (4 * a[1] + 1)*(4 * b[1] + 1), "from loop")
                ans.append((4 * a[1] + 1)*(4 * b[1] + 1))
    # print("normally")
    # return 1
    return max(ans)
    # return track[0][1] * track[1][1]




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
