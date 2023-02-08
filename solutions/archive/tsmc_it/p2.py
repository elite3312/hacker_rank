
import math
import os
import random
import re
import sys



#
# Complete the 'countDistinctIntegers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
#problem definition:
#In the beginning, only one number is on the board.
#while there are number(s) on the board that haven;t been checked:
    #check the number

#check(number x):
    #for i in [1,x]:
        #if x mod i==1:
            #add 'x-i' onto the board
#return the number of distinct numbers on the board in the end.
def countDistinctIntegers(n):
    _on_board=dict()
   
    for i in range(1,n):
        _on_board[i]=[False,False] #(onboard,checked)
    _on_board[n]=[True,False]

    def inner(x):
        _on_board[x][1]=True
        for i in range(1,x):
            if x % i==1 :
                _on_board[x-i][0]=True#add 2 board
                if not _on_board[x-i][1]:#if it is not checked
                    inner(x-i)
    inner(n)
    res=0
    for k in _on_board:
        if _on_board[k][0]:
            res+=1
    return res



if __name__ == '__main__':
    n=49*7
    print(countDistinctIntegers(n))
    #7->5