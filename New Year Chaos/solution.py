#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.


def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1, 0, -1):
        if q[i] != i + 1:
            if i - 1 >= 0 and q[i - 1] == i + 1:
                bribes = bribes + 1
                temp = q[i]
                q[i] = q[i-1]
                q[i-1] = temp
            elif i - 2 >= 0 and q[i - 2] == i + 1:
                temp = q[i-1]
                q[i-1] = q[i-2]
                q[i-2] = temp
                temp = q[i]
                q[i] = q[i-1]
                q[i-1] = temp
                bribes = bribes + 2
            else:
                return "Too chaotic"
    return bribes


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        x = minimumBribes(q)
        print(x)
