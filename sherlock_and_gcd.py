#!/bin/python3

import os
import sys
import re
# Complete the solve function below.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
def is_prime(n):
    return not re.match(r'^.?$|^(..+?)\1+$', '1'*n)
def solve(a):
    set_a = list(set(a))
    primes = 0
    if 1 in set_a:
        return "YES"
    for i in range(len(set_a)):
        if is_prime(set_a[i]) and len(set_a) > 1:
            primes+=1
            if primes > 1:
                return "YES"
        for j in range(len(set_a)):
            if gcd(set_a[i], set_a[j]) == 1:
                return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a_count = int(input())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(result + '\n')

    fptr.close()
