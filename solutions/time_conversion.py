#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[-2]=='A':
        h=int(s[:2])
        if h==12:
            return "00"+s[2:8]
        else :return s[:8]
    else:
        h=int(s[:2])
        if h==12:
           return s[:8] 
        else :
            return str(h+12)+s[2:8]
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()#12:01:00PM

    result = timeConversion(s)

    #fptr.write(result + '\n')

    #fptr.close()
