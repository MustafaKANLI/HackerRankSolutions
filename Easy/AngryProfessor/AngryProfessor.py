#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    # Write your code here
    
    count = 0
    for item in a:
        if item <= 0:
            count += 1
        
    if k <= count:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
   
    k = 3
    a = [-2, -1, 0, 1, 2]

    result = angryProfessor(k, a)

    print(result)

