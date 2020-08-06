#!/usr/bin/env python

class Dataset:
    def __init__(self, bytes, rep, min, max, avg):
        self.bytes = bytes
        self.rep = rep
        self.min = min
        self.max = max
        self.avg = avg

class Dataset1:
    def __init__(self, bytes, rep, usec, bw):
        self.bytes = bytes
        self.rep = rep
        self.usec = usec
        self.bw = bw

class Jgraph:
    def __init__(self):
        pass

    def generate_jgraph(self, lst):
        size = len(lst)
        filename = 'test-data' + '.jgr'
        print 'Generating ', filename

        maxx = lst[size-1].bytes
        maxy = lst[size-1].usec

        buf = []

        buf.append('(* Jgraph for testing *)\n')

        buf.append('newgraph\n\n')
        
        buf.append('yaxis size 5.0 min 0 max ' + str(maxy) + '\n')
        buf.append('hash_labels fontsize 14\n')
        buf.append('label : Window size\n')
        buf.append('fontsize 14\n\n')
        
        buf.append('xaxis size 10.0 min 0 max ' + str(maxx) + '\n')
            
        buf.append('legend off\n')
 
        bufstr = 'newcurve pts '

        for elem in lst:
            bufstr = bufstr + str(elem.bytes) + ' ' + str(elem.usec) + ' ' 

        bufstr = bufstr + ' marktype diamond\n'
        buf.append(bufstr)

        buf.append('title : MPI')
        
        # Write the generated script to the file
        try:
            file = open(filename, 'w')
            file.writelines(buf)
            file.close()
        except IOError:
            msg = 'Cannot open ' + filename + '\n'
            errorandexit(msg)

        # Convert it from jgr to eps
        self.__jgrtoeps__(filename)

    # Convert the file from jgr to eps
    def __jgrtoeps__(self, filename):
        patt = re.compile("(.*).jgr")
        mobj = patt.match(filename)
        if mobj:
            prefix= mobj.group(1)
            cmd = 'jgraph ' + filename + ' > ' + prefix + '.eps'
            print 'Running ', cmd
            os.system(cmd)        


if __name__ == '__main__':
    import os, sys, string, re
    
    lines = []
    plines = []
    
    # Read lines from the file
    try:
        file = open('test-mpich-s.txt', 'r')
        lines = file.readlines()
        file.close()
    except IOError:
        print 'File not found'
        sys.exit(0)

    for line in lines:
        if line[0] != '#':
            plines.append(line)

    #for line in plines:
    #    print line

    idx = 0
    lst = []
    for line in plines:
        if idx == 30:
            break

        tok = string.split(line)

        if len(tok) != 0 and tok[0] != '#bytes':
            ds = Dataset1(int(tok[0]), int(tok[1]), float(tok[2]), float(tok[3]))
            lst.append(ds)
            pass
        
        idx = idx + 1


    for elem in lst:
        print elem.bytes, elem.rep, elem.usec, elem.bw

    jgraph = Jgraph()
    jgraph.generate_jgraph(lst)


