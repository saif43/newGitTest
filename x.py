#!/bin/python

import sys

def minSteps(n, B):
    # Complete this function
    x = B.count("010")
    return x

n = int(raw_input().strip())
B = raw_input().strip()
result = minSteps(n, B)
print(result)



# Sample Input 0

# 7
# 0101010
# Sample Output 0

# 2
# Sample Input 1

# 5
# 01100
# Sample Output 1

# 0
# Sample Input 2

# 10
# 0100101010
# Sample Output 2

# 3