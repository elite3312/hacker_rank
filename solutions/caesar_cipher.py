#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    #s:string
    #k:rotate
    _my_list=[]
    for c in s:
        _ascii=ord(c)
        if 90>=_ascii>=65 :
            base=65
        elif 122>=_ascii>=97 :
            base=97
        else:
            _my_list.append(c)
            continue
        _index=_ascii-base
        _index=(_index+k)%26
        _new_ascii=_index+base
        _my_list.append(chr(_new_ascii))
    #print(_my_list)
    return ''.join(_my_list)
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
