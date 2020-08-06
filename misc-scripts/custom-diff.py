#!/usr/bin/env python

if __name__ == '__main__':
    import sys, string, os, difflib
    from pprint import pprint

    infile = sys.argv[1]
    outfile = sys.argv[2]
    begline = int(sys.argv[3])
    endline = int(sys.argv[4])

    numlines = endline - begline + 1

    difffile = 'difffile.txt'
    
    i = 0
    j = 0
    
    try:
        file1 = open(infile, 'r')
        file2 = open(outfile, 'r')

        while i < begline:
            file1.readline()
            file2.readline()
            i = i + 1

        while j < numlines:
            str1 = file1.readline()
            str2 = file2.readline()            

            if str1 != str2:
                print j, ' -> ', str1
                print j, ' <- ', str2                

            j = j + 1

        #d = difflib.Differ()
        #result = list(d.compare(buf1, buf2))
        #pprint(result)

        file1.close()
        file2.close()        
    except IOError:
        print 'File not found'
        sys.exit(0)
