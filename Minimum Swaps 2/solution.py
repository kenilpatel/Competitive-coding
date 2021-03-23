#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the minimumSwaps function below.

def minimumSwaps(arr): 
    swap = 0
    n = len(arr) 
    for i in range(0,n):
        print(i,arr[i])
        if arr[i] > 0:
            cur = 0
            nexti = abs(arr[i]) - 1
            while arr[nexti] > 0:
                arr[nexti] *= -1
                nexti = abs(arr[nexti]) - 1
                cur += 1 
            swap += cur - 1
    return swap 
            
        
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
