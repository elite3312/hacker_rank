

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos_cnt=0
    neg_cnt=0
    zero_cnt=0
    for elem in arr:
        if elem>0:
            pos_cnt+=1
        elif elem<0:
            neg_cnt+=1
        else:zero_cnt+=1
    sum=len(arr)
    pos_ratio=pos_cnt/ sum
    neg_ratio=neg_cnt/ sum
    zero_ratio=zero_cnt/ sum
    print("%6f"%pos_ratio)
    print("%6f"%neg_ratio)
    print("%6f"%zero_ratio)
    pass
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    #arr=[1,1,0,-1,-1]
    plusMinus(arr)
