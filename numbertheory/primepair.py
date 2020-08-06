# print all pairs of primes between 1 and n that differ by 2
import sys
from numbertheory import *

if __name__ == '__main__':
    n = int(sys.argv[1])

    lst = getPrimePairs(n)

    for p in lst:
        print p

                    
        
