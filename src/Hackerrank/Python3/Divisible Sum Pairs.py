#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
count = 0

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if (a[i] + a[j]) % k == 0:
            count += 1

print(count)