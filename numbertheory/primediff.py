# print differences between prime numbers between 1 and n
import sys
from numbertheory import *

if __name__ == '__main__':
    n = int(sys.argv[1])

    lst = getPrimeDiff(n)

    for p in lst:
        print p
        
