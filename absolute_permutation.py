#!/bin/python3
#
# Link : https://www.hackerrank.com/challenges/absolute-permutation/problem
#
# The logic here can be illustrated as below
#   if n = 12 and k = 3, then least possible absolute permutation is
#   4 5 6 1 2 3 10 11 12 7 8 9
#   if you see the pattern above, for every 2*k consecutive elements, the first k elements and the last k
#   elements are swapped. This arrangement is possible only if n % (2*k) == 0.
#   Hence, we check that condition and if it passes, then we can create an array using the above logic.
#
#
#






import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    if k > n:
        return [-1]
    if k == 0:
        return [i for i in range(1, n+1)]
    if k == n:
        return [i for i in range(1, n+1)][::-1]


    if n % (2*k) == 0:
        li = [0] * n
        for i in range(0, n, 2*k):
            li[i: i + k] = [j for j in range(i + k + 1, i + 2*k + 1)]
            li[i+k : i + 2*k] = [j for j in range(i + 1, i + k + 1)]
    else:
        return [-1]
    return li

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
