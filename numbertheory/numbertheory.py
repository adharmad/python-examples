# print all primes between 1 and n
import sys

def getPrimes(n):
    """Returns a list of all primes between 2 and n."""
    lst = []
    lst.append(2)
    lst.append(3)

    for i in range(4, n):
        isnotprime = 0
        for p in lst:
            if i % p == 0:
                isnotprime = 1
                break
        if not isnotprime:
            lst.append(i)

    return lst

def getPrimePairs(n):
    """Returns a tuple of prime numbers separated by 2."""
    plst = getPrimes(n)

    pairLst = []

    for i in range(1, len(plst)):
        if plst[i] - plst[i-1] == 2:
            pairLst.append((plst[i-1], plst[i]))

    return pairLst

def getPrimeDiff(n):
    """Returns a list of numbers that represent difference between
    consecutive prime numbers."""
    plst = getPrimes(n)
    
    diffLst = []
    
    for i in range(1, len(plst)):
        diffLst.append(plst[i] - plst[i-1])

    return diffLst
        
