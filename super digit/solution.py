#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    suma = 0
    for i in str(n):
        suma += int(i)
    suma = suma * k
    return sum(str(suma))
def sum(dig):
    if len(dig) == 1:
        return int(dig)
    else:
        suma = 0
        for i in dig:
            suma += int(i)
        return sum(str(suma))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
