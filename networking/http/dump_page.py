# Fetch web pages

import sys, urllib2, string

if __name__ == '__main__':
    siteName = string.strip(sys.argv[1])
    fileName = siteName + '.html'
    url = 'http://www.' + siteName + '.com'
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req)

    f = None 
    try:
        f = open(fileName, 'w+')
    except IOError, e:
        print 'Cannot open file to write web page'
        sys.exit(1)

    while 1:
        data = fd.read(1024)
        if not len(data):
            break
        
        sys.stdout.write(data)
        f.write(data)

    f.close()

