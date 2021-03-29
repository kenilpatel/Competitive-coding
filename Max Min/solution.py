#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    n = len(arr)
    arr = sorted(arr) 
    l = 0
    r = k - 1
    ans = arr[r] - arr[l]
    for i in range(0,n - k + 1):
        ans = min(ans,arr[r] - arr[l])
        r += 1
        l += 1
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
