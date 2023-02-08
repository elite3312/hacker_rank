

import math
import os
import random
import re
import sys

def _binomial_coeff(n, k):
    _res = 1
    if (k > n - k):k = n - k
    for i in range(k):
        _res =_res* (n - i)
        _res=_res// (i + 1)
    return _res


def _catalan_number(n):
    c = _binomial_coeff(2 * n, n)
    return c // (n + 1)


def numBST(nodeValues):
    res=[]
    for elem in nodeValues:
        res.append(_catalan_number(elem)%(100000007))
    return res


if __name__ == '__main__':
    n_s = [5]#for n in n_s, find the catalan number(n)
    #the catalan number(n) is equal to the possible number of distinct n node BSTs
    print(numBST(n_s))
