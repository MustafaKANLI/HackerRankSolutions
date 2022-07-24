#!/bin/python3

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
    # Write your code here
    positive = 0
    negative = 0
    zero = 0
    
    for item in arr:
        if item > 0:
            positive = positive + 1
        elif item == 0:
            zero = zero + 1
        else:
            negative = negative + 1
    
    sum  = positive + negative + zero
    
    print(positive / sum)
    print(negative / sum)
    print(zero / sum)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
