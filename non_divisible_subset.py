#!/bin/python3
#Link : https://www.hackerrank.com/challenges/non-divisible-subset/problem

#The Logic here is that, we traverse through all the elements and store their remainders
#when divided by the K, and since remainder(a/k) + remainder(b/k) = k, when we store the
#maximum value of such pairs of remainders, then we can obviate the given condition of
#not getting a pair of numbers whose sum is divisible by K.
#




import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    n = len(s)
    count = [0] * k
    for i in s:
        count[int(i % k)] += 1
    c = min(1, count[0])
    for i in range(1, k//2 + 1):
        if i != k - i:
            c += max(count[i], count[k - i])
        else:
            c += min(1, count[i])
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
