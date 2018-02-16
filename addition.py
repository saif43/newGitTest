#!/bin/python

import sys


input= int(raw_input().strip())
sum=0
for i in range(input+1):
    if i != input +1:
        print i
        print "+"
    

print sum
