#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    
    height = 0
    

    for i in range(n+1):
        if i % 2 == 0:
            height += 1
            continue
        elif i % 2 == 1:
            height *= 2
            continue
    return height
        
    

if __name__ == '__main__':
    
    n = 3
    result = utopianTree(n)

    print(result)
