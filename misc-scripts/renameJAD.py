#!c:/Python25/python.exe -w
# Renames files *.jad to *.java recursively

import os, os.path, sys, string, shutil

def renameJAD(folder):
    if not os.path.isdir(folder):
        return

    files = os.listdir(folder)

    for f in files:
        f1 = os.path.join(folder, f)

        if os.path.isfile(f1) and f1.endswith('.jad'):
            newf = f1.replace('.jad', '.java')
            print 'Ranaming ', f1
            os.rename(f1, newf)
            #shutil.rmtree(f1)
        else:
            renameJAD(f1)

def main(argv):
    folder = sys.argv[1]
    renameJAD(folder)

if __name__ == '__main__':
    main(sys.argv)
