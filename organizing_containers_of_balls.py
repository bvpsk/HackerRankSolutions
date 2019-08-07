#!/bin/python3
#Link to Problem : https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

#the logic here is simple. If we swap two balls in each run, then the total number of balls
#in each container in the end will be same. Hence, If we sort the list containing total no. of
#balls in each container at present and the list of balls that must be present after the completion
#of sort operation and if they are equal, then they are said to be POSSIBLE.

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    a = []
    b = []
    for i in range(len(container)):
        a.append(0)
        b.append(0)
        for j in range(len(container)):
            a[-1] += container[i][j]
            b[-1] += container[j][i]
    if sorted(a) == sorted(b):
        return "Possible"
    else:
        return "Impossible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
