# Link :  https://www.hackerrank.com/challenges/most-distant/problem?isFullScreen=false

#!/bin/python3

import os
import sys
import math
# Complete the solve function below.
def distance(a, b):
    a = list(map(float, a))
    b = list(map(float, b))
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
def solve(coordinates):
    y_s = []
    x_s = []
    for coordinate in coordinates:
        if coordinate[0] == 0:
            y_s.append(coordinate[1])
        else:
            x_s.append(coordinate[0])
    y_s.sort()
    x_s.sort()
    distances = []
    distances.append(distance([x_s[0] ,0], [x_s[-1], 0]))
    distances.append(distance([0, y_s[-1]], [0, y_s[0]]))
    distances.append(distance([x_s[0], 0], [0, y_s[-1]]))
    distances.append(distance([x_s[0], 0], [0, y_s[0]]))
    distances.append(distance([0, y_s[0]], [x_s[-1] ,0]))
    distances.append(distance([x_s[-1], 0], [0, y_s[-1]]))
    return round(max(distances), 6)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)

    fptr.write(str(result) + '\n')

    fptr.close()
