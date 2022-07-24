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
    arr = s.split(":")
    
    time = arr[2]
    time = time[2:]
    
    if time == "AM" and arr[0] == "12":
        print("00" + s[2:-2])
        return "00" + s[2:-2]
    elif time == "AM":
        print(s[:-2])
        return s[:-2]
        
    if time == "PM" and  arr[0] == "12":
        print(s[:-2])
        return s[:-2]
    
    elif time == "PM":
        arr[0] = int(arr[0]) + 12
        arr[0] = str(arr[0])
        
        s=''
        
        for item in arr:
            s += item + ':'
        
        s = s[:8]
        
        print(s)
        return s
    

if __name__ == '__main__':


    s = '11:05:45AM'

    timeConversion(s)

