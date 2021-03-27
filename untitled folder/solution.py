#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the countTriplets function below.
def countTriplets(arr, r):
    after = defaultdict(lambda:0)
    before = defaultdict(lambda:0)
    for i in arr:
        after[i] += 1
    cnt = 0
    for i in arr:
        after[i] -= 1
        # print(i / r,r * i,before[i / r],after[r * i],before,after)
        cnt += before[i / r] * after[r * i]
        before[i] += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
