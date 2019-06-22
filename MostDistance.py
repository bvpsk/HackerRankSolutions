# Link :  https://www.hackerrank.com/challenges/most-distant/problem?isFullScreen=false




                #                 *(0, y_max)
                #               /   \
                #              /     \
                #             /       \
                #            /         \
                # (x_min,0 )*-----------*(x_max, 0)
                #            \         /
                #             \       /
                #              \     /
                #               \   /
                #                 *(0, y_min)

                # The maximun distance lies in one of the below six combinations:
                #     1) (x_min, 0) to (x_max, 0)
                #     2) (0, y_max) to (0, y_min)
                #     3) (x_min, 0) to (0, y_max)
                #     4) (x_min, 0) to (0, y_min)
                #     5) (x_max, 0) to (0, y_max)
                #     6) (x_max, 0) to (0, y_min)

                # Hence, finding all those distances(euclidian) and then the maximum
                # of those is the required answer and is also the optimum solution,
                # which reduces the complexity of the problem.

                # See the solve function and distance function. The rest is trivial
                # HackerRank I/O code.



#!/bin/python3

import os
import sys
import math
# Complete the solve function below.
def distance(a, b): #function to solve euclidian distance
    a = list(map(float, a))
    b = list(map(float, b))
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
def solve(coordinates):
    y_s = [] # store all the y_coordinates here
    x_s = [] # store all the x-coordinates here
    for coordinate in coordinates:
        if coordinate[0] == 0:
            y_s.append(coordinate[1])
        else:
            x_s.append(coordinate[0])

    # find the min and max values of x-coordinates and y-coordinates.
    x_min = min(x_s)
    x_max = max(x_s)
    y_min = min(y_s)
    y_max = max(y_s)

    distances = []
    # Finding all six max possible cases.
    distances.append(distance([x_min ,0], [x_max, 0]))
    distances.append(distance([0, y_max], [0, y_min]))
    distances.append(distance([x_min, 0], [0, y_max]))
    distances.append(distance([x_min, 0], [0, y_min]))
    distances.append(distance([0, y_min], [x_max ,0]))
    distances.append(distance([x_max, 0], [0, y_max]))
    return round(max(distances), 6) # returning the maximum distance with precision upto 6 digits(decimal)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)

    fptr.write(str(result) + '\n')

    fptr.close()
