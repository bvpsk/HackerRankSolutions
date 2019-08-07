import numpy as np
import math
import re


def is_prime(n):
    return not re.match(r'^.?$|^(..+?)\1+$', '1'*n)

def prime_generator():
    p = 1
    while True:
        p+=1
        if is_prime(p):
            yield p

def factorize(n):
    nn = n
    gen = prime_generator()
    p = gen.next()
    factors = [p]
    while n > 1:
        n = n/p
        while n%p != 0 and n > 1:
            p = gen.next()
        if p not in factors:
            factors.append(p)
    if nn% factors[-1] != 0:
        return factors[:-1]
    else:
        return factors
