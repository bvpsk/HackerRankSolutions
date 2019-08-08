#!/bin/python3
#Link : https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=false

# The logic here is to actually find the no. of rows and no. of columns. The condition
# given here is to form the matrix using row and column values as r * c >= sizeof(given string)
# This can be achieved by continually increasing the no. of rows from initial value as by doing
# so, we are moving from lower product value to a higher product value. After finding the rows
# and columns, we simply create substrings and traverse them.
#


import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = list(s.split())
    ss = ""
    for i in s:
        ss += i
    s = ss
    l = len(s)
    r = math.ceil(math.sqrt(l))
    c = math.floor(math.sqrt(l))
    while c * r < l:
        if r + 1 <= c:
            r += 1
        else:
            break
    ss = []
    i = 0
    j = 0
    ss.append("")
    while i < l:
        ss[-1] += s[i]
        j += 1
        i += 1
        if j == c:
            j = 0
            ss.append("")
    sss = ""
    for j in range(c):
        for i in range(len(ss)):
            try:
                sss += ss[i][j]
            except:
                pass
        sss += " "
    return sss


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
