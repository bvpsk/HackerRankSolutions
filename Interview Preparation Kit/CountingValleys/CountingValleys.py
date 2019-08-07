#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    i = 0
    while i < n:
        if s[i] == "D":
            c = 0
            while c + i < n and s[c + i] == "D":
                c += 1
            if s[i+c: i+2*c] == "U" * c:
                valleys += 1
                i += 2*c
            else:
                i += c
                while i < n and s[i] == "U":
                    i+=1
        else:
            i += 1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
