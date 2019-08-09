#!/bin/python3
#   Link : https://www.hackerrank.com/challenges/the-grid-search/problem
#
#   The logic here is to check the corresponding elements until they are matched
#   If all of the pattern elements are matched, then we return "YES".
#   We check this for all possible pattern submatrices in the Grid.
#   If anything matches, we return "YES". If nothing matches, we return "NO".
#
#
#

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):
    gr = len(G)
    gc = len(G[0])
    pr = len(P)
    pc = len(P[0])
    dr = gr - pr
    dc = gc - pc
    for i in range(dr + 1):
        for j in range(gc - pc + 1):
            k = 0
            l = 0
            d = i
            e = j
            while k < pr and G[d][e] == P[k][l]:
                e += 1
                l += 1
                if l == pc:
                    l = 0
                    k += 1
                    d += 1
                    e = j
            if k == pr:
                return "YES"
    return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
