#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    cnt = len(s)
    for i in range(1,n - 1):
        j = i - 1
        k = i + 1 
        print(s[j],s[k])
        if s[j] == s[k]:
            compare = s[j]
            while j >= 0 and k < n and s[j] == s[k] and s[j] == compare:
                cnt += 1
                j -= 1 
                k += 1
    for i in range(0,n - 1):
        j = i
        k = i + 1
        # print(s[j],s[k])
        if s[j] == s[k]:
            compare = s[j]
            while j >= 0 and k < n and s[j] == s[k] and s[j] == compare:
                cnt += 1
                j -= 1 
                k += 1 
    return cnt
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
