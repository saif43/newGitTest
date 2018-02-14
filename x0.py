#!/bin/python

import sys

x = "     Hello World       "

x = x.strip()

print x

x = x.strip("Hld")
print x

x = x.replace("o","M")
print x
