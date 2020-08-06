#!/usr/bin/env python
# Removes files or folders recursively. The name of the file or folder
# to be deleted is passed as a command line argument
# eg - 
#   ./delete-fof.py CVS
#   ./delete-fof.py ".class"

import os, os.path, sys, string, shutil

def removeCVS(folder, what_to_delete):
    if not os.path.isdir(folder):
        return
    
    files = os.listdir(folder)

    for f in files:
        f1 = os.path.join(folder, f)

        if os.path.isdir(f1) and f == what_to_delete:
            print 'Removing ', f1
            shutil.rmtree(f1)
        else:
            removeCVS(f1)

def main(argv):
    folder = sys.argv[1]
    what_to_delete = sys.argv[2]
    removeCVS(folder, what_to_delete)

if __name__ == '__main__':
    main(sys.argv)
