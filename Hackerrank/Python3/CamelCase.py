#!/bin/python3

import sys


s = input().strip()

if len(s) == 0:
    count=0
else:
    count=1
    for c in s:
        if c.isupper():
            count += 1

print (count)

