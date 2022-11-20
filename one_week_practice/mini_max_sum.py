

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    _min=min(arr)
    _max=max(arr)
    _sum=sum(arr)
    _min_sum=_sum-_max
    _max_sum=_sum-_min
    print("%ld %ld"%(_min_sum, _max_sum))
if __name__ == '__main__':

    #arr = list(map(int, input().rstrip().split()))
    arr=[1,3,5,7,9]
    miniMaxSum(arr)
