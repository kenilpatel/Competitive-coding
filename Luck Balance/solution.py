#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    important = []
    luck_balance = 0
    for luck,imp in contests:
        if imp > 0:
            important.append([luck,imp])
        else:
            luck_balance += luck
    important = sorted(important,reverse = True)
    while k > 0 and important:
        luck_balance += important.pop(0)[0]
        k -= 1 
    for luck,imp in important:
        luck_balance -= luck
    return luck_balance
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
