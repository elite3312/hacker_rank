#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    n=len(matrix[0])//2
    sum=0
    for r in range(0,n):
        for c in range(0,n):
            #to the right
            _cmp_r=r
            _cmp_c=2*n-1-c
            matrix[r][c]=max(matrix[r][c],matrix[_cmp_r][_cmp_c])
            #to the bottom
            _cmp_r=2*n-1-r
            _cmp_c=c
            matrix[r][c]=max(matrix[r][c],matrix[_cmp_r][_cmp_c])
            #to the bottom right
            _cmp_r=2*n-1-r
            _cmp_c=2*n-1-c
            matrix[r][c]=max(matrix[r][c],matrix[_cmp_r][_cmp_c])
            
            sum+=matrix[r][c]
    return sum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
