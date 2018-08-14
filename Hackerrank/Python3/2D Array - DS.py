#!/bin/python3

import sys


arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
biggestsum=None

def hourglas_sum(i,j):
    return arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]+ arr[i][j]+  arr[i+1][j-1] +arr[i+1][j] +arr[i+1][j+1]

for i in range(1,len(arr)-1):
    for j in range(1,len(arr[i])-1):
        hsum = hourglas_sum(i,j)
        if biggestsum==None:
            biggestsum=hsum
        if hsum>biggestsum:
            biggestsum=hsum

print(biggestsum)

