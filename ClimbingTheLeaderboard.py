def binary_search(li, val):
    start = 0
    end = len(li) - 1
    close_idx = 0
    while start <= end:
        idx = start + (end - start)/2
        if(abs(li[idx] - val) < abs(li[close_idx] - val)):
            close_idx = idx
        if li[idx] == val:
            return True, idx
        elif li[idx] < val:
            start = idx + 1
        else:
            end = idx - 1
    return False, close_idx

n = 10
from random import randint as r
li = [r(0,100) for i in range(n)]
li = sorted(li)
print(li)
val = r(0,100)
print(val)
print(binary_search(li, val))
