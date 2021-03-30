#!/bin/python3

import math
import os
import random
import re
import sys
import copy
# Complete the crosswordPuzzle function below.
global ans
ans = ""
def crosswordPuzzle(crossword, words):
    n = len(crossword)
    m = len(crossword[0])
    for i in range(n):
        crossword[i] = list(crossword[i]) 
    words = words.split(';')
    crossword = fill(crossword,words,n,m)
    return ans
def check_pos(crossword,word,i,j,v,n,m): 
    if v == True:
        col = j
        nw = len(word) - 1
        if i + nw >= n:
            return False
        idx = 0
        for row in range(i,i + nw + 1):
            if crossword[row][col] == '+':
                return False
            elif crossword[row][col] == '-':
                pass
            else:
                if crossword[row][col] != word[idx]:
                    return False
            idx += 1
        return True
    else: 
        row = i
        nw = len(word) - 1
        if j + nw >= m:
            return False
        idx = 0 
        for col in range(j,j + nw + 1): 
            if crossword[row][col] == '+':
                return False
            elif crossword[row][col] == '-':
                pass
            else:
                if crossword[row][col] != word[idx]:
                    return False
            idx += 1
        return True
    
def fill(crossword,words,n,m): 
    global ans
    if len(words) == 0:
        for i in range(n):
            crossword[i] = "".join(crossword[i])  
        ans = crossword
    else: 
        if ans != "":
            return
        put = words[0]
        putn = len(put)
        for i in range(0,n):
            for j in range(0,m):
                ansv = check_pos(crossword,put,i,j,True,n,m)
                if ansv == True:
                    col = j
                    ncr = copy.deepcopy(crossword)
                    idx = 0
                    for row in range(i,i + putn):
                        ncr[row][col] = put[idx]
                        idx += 1 
                    fill(ncr,words[1:],n,m)
                ansh = check_pos(crossword,put,i,j,False,n,m) 
                if ansh == True:
                    row = i
                    ncr = copy.deepcopy(crossword)
                    idx = 0
                    for col in range(j,j + putn):
                        ncr[row][col] = put[idx]
                        idx += 1 
                    fill(ncr,words[1:],n,m) 
                
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
