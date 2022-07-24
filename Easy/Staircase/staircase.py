#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    space = n-1
    

    for i in range(n):
        s = " "
        sharp = "#"
            
        for j in range(space-1):
            s += " "  
            

        for j in range(n-(space +1)):
            sharp += "#"
            

        if (space == 0):
            print(sharp)
            
        else:
            print(s + sharp)
            

        sharp = "#"
        s = " "
        space = space-1

            

if __name__ == '__main__':
    n = 6
    staircase(n)
