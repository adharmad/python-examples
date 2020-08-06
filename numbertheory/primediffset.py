# print differences between prime numbers between 1 and n. remove the first
# difference between 2 and 3, divide all differences by 2 (all are even) and
# print the list
# print the list with sets starting from 1

import sys
from numbertheory import *

if __name__ == '__main__':
    n = int(sys.argv[1])

    lst = getPrimeDiff(n)
    lst2 = []

    for p in lst:
        if p == 1: continue
        lst2.append(p/2)

    set = []

    d = len(lst2)
    i = 0
    while 1:
        tmplst = []
        if lst2[i] == 1:
            while 1:
                tmplst.append(lst2[i])
                i = i + 1
                if i >= d: break
                if lst2[i] == 1:
                    break
        set.append(tmplst)
        if i>= d: break
    
    for s in set:
        print s
            
        
