#!/usr/bin/env python

import sys, math

if __name__ == '__main__':
    p = int(sys.argv[1])
    d = {}
    for i in range(p):
        d[i] = []
        d[i].append(i)
        
    print 'p = ', p

    for i in d.keys():
        print d[i]
    

    stages = []
    stages.append(1)
    n = math.floor(math.log(float(p))/math.log(2.0))
    print 'n = ', n
    for i in range(n):
        stages.append(1 + pow(2, i))

    print stages

    idx = 0
    for s in stages:
        print 'stage =', idx
        e = {}
        for i in range(p):
            rec = (i + stages[idx])%p
            print 'processor ', i, 'sends to ', rec
            e[rec] = d[rec] + d[i]
        d = e
        for i in range(p):
            print 'processor ', i, 'has data ', d[i]

        idx = idx + 1
            
