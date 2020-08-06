#!/usr/bin/env python

if __name__ == '__main__':
    import sys, os, string

    infile = sys.argv[1]
    lines = int(sys.argv[2])
    outfile = 'tmp.txt'
    i = 0
    
    try:
        file1 = open(infile, 'r')
        file2 = open(outfile, 'w')

        while i < lines:
            str = file1.readline()
            file2.write(str)
            i = i + 1

        file1.close()
        file2.close()        
    except IOError:
        print 'File not found'
        sys.exit(0)


    

    








