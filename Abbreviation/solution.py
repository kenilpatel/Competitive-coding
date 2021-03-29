#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the abbreviation function below.
def abbreviation(a, b):
    n = len(a)
    m = len(b)
    mat = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i].isupper():
                if a[i] == b[j]:
                    if i - 1 >= 0 and j - 1 >= 0:
                        mat[i][j] = mat[i - 1][j - 1] + 1 
                    else:
                        mat[i][j] = 1
            else:
                if a[i].upper() == b[j]:
                    if i - 1 >= 0 and j - 1 >= 0:
                        mat[i][j] = max(mat[i - 1][j - 1] + 1,mat[i - 1][j])
                    else:
                        mat[i][j] = max(1,mat[i - 1][j])
                else:
                    if i - 1 >= 0:
                        mat[i][j] = mat[i - 1][j]
    # print(mat)
    maxl = 0
    i = n - 1
    for j in range(m):
        maxl = max(maxl,mat[i][j])
    return 'YES' if maxl == m else 'NO'
                        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b) 
        fptr.write(result + '\n')

    fptr.close()
