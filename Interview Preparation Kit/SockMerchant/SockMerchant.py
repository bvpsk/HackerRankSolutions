#Link : https://www.hackerrank.com/challenges/sock-merchant/
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    set_ar = set(ar)
    d = {i: 0 for i in set_ar}
    for a in ar:
        d[a] += 1
    c = 0
    for key in d:
        c+= int(d[key]/2)
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
