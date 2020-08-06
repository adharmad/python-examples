# Fetch web page information

import sys, urllib2

if __name__ == '__main__':
    req = urllib2.Request(sys.argv[1])
    fd = urllib2.urlopen(req)

    print 'Retrieved', fd.geturl()
    info = fd.info()
    for key, value in info.items():
        print '%s = %s' % (key, value)

