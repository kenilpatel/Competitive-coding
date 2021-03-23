#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
global inv
inv = 0

def sort(arr,low,high):   
    if high - low <= 1:
        return arr
    elif high - low == 2: 
        if arr[0] <= arr[1]:
            return arr
        else:
            arr[0],arr[1] = arr[1],arr[0]
            global inv
            inv += 1
            return arr
    mid = int((low + high) / 2) 
    left = arr[low:mid]
    right = arr[mid:high] 
    return merge(sort(left,0,mid - low),sort(right,0,high - mid),mid - low,high - mid)

def merge(arr1,arr2,n1,n2):
    i = 0
    j = 0 
    result = []
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            result.append(arr1[i]) 
            i += 1
        else:
            global inv 
            inv += n1 - i 
            result.append(arr2[j])
            j += 1
    while i < n1:
        result.append(arr1[i])
        i += 1
    while j < n2:
        result.append(arr2[j])
        j += 1
    return result

def countInversions(arr):
    global inv
    inv = 0
    sort(arr,0,len(arr))
    return inv

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
