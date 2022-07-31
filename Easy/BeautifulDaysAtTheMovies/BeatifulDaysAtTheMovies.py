#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#


def beautifulDays(i, j, k):
    # Write your code here
    result = 0
    
    for item in range(i, j+1):
          
        string=str(item)
        reverseStr=string[::-1]
        reverseInt=int(reverseStr)
        
        sub = abs(item - reverseInt)
        
        if(sub % k == 0):
            result += 1
        
    return result

if __name__ == '__main__':

    i = 20
    j = 23
    k = 26

    result = beautifulDays(i, j, k)
    print(result)
