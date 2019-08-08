#!/bin/python3
# Link : https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=false
# The logic here is to use the lexicographic ordering algorithm to check whether higher
# representation for the given string can be obtained or not and if possible, we return that
# arrangement, or else we return NO ANSWER.
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

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    w = list(w)
    lx = -1
    for i in range(len(w) - 1):
        if w[i] < w[i+1]:
            lx = i
    if lx == -1:
        return "no answer"
    ly = -1
    for i in range(len(w)):
        if w[i] > w[lx]:
            ly = i
    w[ly], w[lx] = w[lx], w[ly]
    return "".join(w[:lx + 1] + w[lx + 1:][::-1])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
