#!/usr/bin/env python

if __name__ == '__main__':
    import os, re
    patt = re.compile("(.*).jgr")

    filelst = os.listdir(os.curdir)

    for file in filelst:
        mobj = patt.match(file)
        if mobj:
            prefix= mobj.group(1)
            cmd = 'jgraph ' + file + ' > ' + prefix + '.eps'
            print 'Running ', cmd
            os.system(cmd)
    
