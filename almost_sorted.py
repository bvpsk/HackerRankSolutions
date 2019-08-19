#!/bin/python3
#
#   Link : https://www.hackerrank.com/challenges/almost-sorted/problem?isFullScreen=false
#
#   save the given array in new variable and sort it. If it is same as the given array, then print YES
#   or else, find all those indices with different values in ariginal and sorted arrays.
#   the first and last are the pivots. If swapping them is sufficient, then swap them. or else, reverse the
#   entire sub array and check if the resultant array is sorted. If yes, print accordingly, or else print NO.
#





import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
    nums = arr
    arr = sorted(nums)
    if nums == arr:
        print("yes")
    else:
        ans = []
        for i, j in zip(range(len(nums)), range(len(nums))):
            if arr[i] != nums[j]:
                ans.append(i)
        if len(ans) == 2:
            if arr[ans[0]] == nums[ans[1]]:
                print("yes")
                print("swap %d %d" % (ans[0] + 1, ans[1] + 1))
            else:
                print("no")
        else:
            if [arr[i] for i in ans] == [nums[i] for i in ans[::-1]]:
                print("yes")
                print("reverse %d %d" % (ans[0] + 1, ans[-1] + 1))
            else:
                print("no")
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
