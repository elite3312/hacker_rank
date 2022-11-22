#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    #n: number of towers, m: each tower's height
    #each player can reduce the height of a tower to some number that evenly divides the height at start of turn
    if m==1:return 2#in this case player has no moves at start
    if n==1 and m>1:#in this case, player 1 reduces the tower to 1
        return 1
    if n %2==1:return 1#player 1 gets to make the 1st move on the last tower and reduce it to 1
    else:return 2#player 2 gets to make the 1st move on the last tower and reduce it to 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
