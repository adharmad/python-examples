#!/usr/bin/env python
# Sorts words in a file by length
# Usage ./sort-words.py <infilename> <outfilename>

import os, os.path, sys, string, shutil

def sort(inFile, outFile):
    try:
        infh = open(inFile, 'r+')
        outfh = open(outFile, 'w+')

        words = infh.readlines()

        for i in range(len(words)):
            words[i] = string.strip(words[i])

        words.sort(len_compare)

        for w in words:
            outfh.write(w + '\n')

        infh.close()
        outfh.close()


    except IOError, e:
        print 'Error while opening ', inFile, ' or ', outFile
        sys.exit(0)

def len_compare(x, y):
    if len(x) > len(y):
        return 1
    elif len(x) == len(y):
        return 0
    else:
        return -1

def main(argv):
    inFile = sys.argv[1]
    outFile = sys.argv[2]
    sort(inFile, outFile)

if __name__ == '__main__':
    main(sys.argv)
