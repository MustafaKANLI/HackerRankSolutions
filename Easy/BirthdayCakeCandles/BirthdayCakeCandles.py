#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
   
    count = 0
    maxVal = max(candles)
    
    for item in candles:     
        if maxVal == item:
            count = count+1
            

    #in Hackerrank, use return instead of print
    print(count) 
    

if __name__ == '__main__':

    candles = [4,1,2,4]

    birthdayCakeCandles(candles)

