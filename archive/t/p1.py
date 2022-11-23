#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMinimumCost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
#problem definition:
#input:array of positive integers.
#the cost of an array is defined as :sum((arr[i]-arr[i-1])^2).
#we can insert any positive integer into the array to reduce the cost.
#find the minimum cost possible by inserting 1 element
def getMinimumCost(arr):
    n=len(arr)
    cost=0
    max_diff=-1
    for i in range(1,n-1+1):
        diff=arr[i]-arr[i-1]
        diff=abs(diff)
        max_diff=max(max_diff,diff)
        cost+=diff*diff
    cost-=max_diff*max_diff
    
    if max_diff%2==0:#even
        new_diff=max_diff//2
        cost+=new_diff*new_diff*2
    else:#odd
        new_diff_left=(max_diff-1)//2
        new_diff_right=new_diff_left+1
        cost+=new_diff_left*new_diff_left+new_diff_right*new_diff_right
    return cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getMinimumCost(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
