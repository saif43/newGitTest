#!/bin/python

import sys


s = raw_input().strip()

if s != '':
      print sum(map(str.isupper, s))
      print sum(map(str.islower, s))

