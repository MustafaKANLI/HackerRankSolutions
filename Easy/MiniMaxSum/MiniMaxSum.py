#!/bin/python3

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
    minVal = min(arr)
    maxVal = max(arr)
    sum = 0
    
    for item in arr:     
        sum += item
      
    print((sum - maxVal) , (sum - minVal))
    
    
if __name__ == '__main__':

    arr = [3,1,5,7,9]

    miniMaxSum(arr)
    
