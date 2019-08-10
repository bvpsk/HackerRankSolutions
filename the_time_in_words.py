#!/bin/python3
#
#   Link : https://www.hackerrank.com/challenges/the-time-in-words/problem
#   The problem is Straight forward as we just have to convert time to text. The
#   logic I implemented is readable.
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

# Complete the timeInWords function below.
def timeInWords(h, m):
    d = {1 : "one", 2: "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine", 10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen", 17 : "seventeen", 18 : "eighteen", 19 : "nineteen"}

    d1 = {2 : "twenty", 3 : "thirty", 4 : "forty", 5 : "fifty"}

    if m == 0:
        return d[h] + " o' clock"
    if m == 15:
        return "quarter past " + d[h]
    elif m == 30:
        return "half past " + d[h]
    elif m == 45:
        return "quarter to " + d[h + 1]


    if m < 30:
        if m < 20:
            peg = d[m]
        else:
            peg = d1[int(m / 10)] + " " + d[int(m % 10)]
        if m != 1:
            peg += " minutes past "
        else:
            peg += " minute past "
        return peg + d[h]
    else:
        m = 60 - m
        if m < 20:
            peg = d[m]
        else:
            peg = d1[int(m / 10)] + " " + d[int(m % 10)]
        if m != 1:
            peg += " minutes to "
        else:
            peg += " minute to "
        if h == 12:
            return peg + d[1]
        else:
            return peg + d[h + 1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
