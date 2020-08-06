# print differences between prime numbers between 1 and n. remove the first
# difference between 2 and 3, divide all differences by 2 (all are even) and
# print the list

import sys
from numbertheory import *

if __name__ == '__main__':
    n = int(sys.argv[1])

    lst = getPrimeDiff(n)

    for p in lst:
        if p == 1: continue
        print p/2
        
