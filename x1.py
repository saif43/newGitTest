#!/bin/python

import sys

def theLoveLetterMystery(s):
    # Complete this function
    y = list(s)
    length = len(y)
    count = 0

    while length > 1 or length > 0:
        count += abs(ord(y[0])-ord(y[length-1]))
        # ord for getting ascci value
        if length >= 2:
            y.pop(length-1)
            y.pop(0)
        else:
            y.pop(0)
        length-=2
    return count

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = theLoveLetterMystery(s)
    print(result)


# Example:

# Sample Input

# 4
# abc
# abcba
# abcd
# cba
# Sample Output

# 2
# 0
# 4
# 2    

