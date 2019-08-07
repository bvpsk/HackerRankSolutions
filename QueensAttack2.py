#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    left = [r_q, 0]
    right = [r_q, n + 1]
    up = [n + 1, c_q]
    down = [0, c_q]
    # nl = [n + 1, 0]
    # nr = [n+1, n+1]
    # sl = [0, 0]
    # sr = [0, n+1]
    l = c_q - 1
    r = n - c_q
    u = n - r_q
    d = r_q - 1
    if l < u:
        nl = [r_q + l + 1, c_q - l - 1]
    else:
        nl = [r_q + u + 1, c_q - u - 1]
    if u < r:
        nr = [r_q + u + 1, c_q + u + 1]
    else:
        nr = [r_q + r + 1, c_q + r + 1]
    if l < d:
        sl = [r_q - l - 1, c_q - l - 1]
    else:
        sl = [r_q - d - 1, c_q - d - 1]
    if d < r:
        sr = [r_q - d - 1, c_q + d + 1]
    else:
        sr = [r_q - r - 1, c_q + d + 1]


    for obstacle in obstacles:
        if obstacle[0] == r_q:
            if obstacle[1] > c_q:
                if obstacle[1] < right[1]:
                    right[1] = obstacle[1]
            else:
                if obstacle[1] > left[1]:
                    left[1] = obstacle[1]
        elif obstacle[1] == c_q:
            if obstacle[0] > r_q:
                if obstacle[0] < up[0]:
                    up[0] = obstacle[0]
            else:
                if obstacle[0] > down[0]:
                    down[0] = obstacle[0]
        else:
            rs = r_q - obstacle[0]
            cs = c_q - obstacle[1]
            if abs(rs) == abs(cs):
                if rs < 0:
                    if cs > 0:
                        if obstacle[0] < nl[0] and obstacle[1] > nl[1]:
                            nl[0] = obstacle[0]
                            nl[1] = obstacle[1]
                    else:
                        if obstacle[0] < nr[0] and obstacle[1] < nr[1]:
                            nr[0] = obstacle[0]
                            nr[1] = obstacle[1]
                else:
                    if cs > 0:
                        if obstacle[0] > sl[0] and obstacle[1] > sl[0]:
                            sl[0] = obstacle[0]
                            sl[1] = obstacle[1]
                    else:
                        if obstacle[0] > sr[0] and obstacle[1] < sr[1]:
                            sr[0] = obstacle[0]
                            sr[1] = obstacle[1]



    # print(left)
    # print(right)
    # print(up)
    # print(down)
    # print(nl)
    # print(nr)
    # print(sl)
    # print(sr)



    moves = 0
    # print(moves)
    moves += c_q - left[1] - 1
    # print(moves)
    moves += right[1] - c_q - 1
    # print(moves)
    moves += up[0] - r_q - 1
    # print(moves)
    moves += r_q - down[0] - 1
    # print(moves)
    moves += abs(r_q - nl[0]) - 1
    # print(moves)
    moves += abs(r_q - nr[0]) - 1
    # print(moves)
    moves += abs(r_q - sl[0]) - 1
    # print(moves)
    moves += abs(r_q - sr[0]) - 1
    # print(moves)
    return moves





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
