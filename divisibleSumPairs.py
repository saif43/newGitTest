#!/bin/python

import sys

def divisibleSumPairs(n, k, ar):
    # Complete this function

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
result = divisibleSumPairs(n, k, ar)
print(result)
