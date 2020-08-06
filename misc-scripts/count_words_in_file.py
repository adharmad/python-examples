import sys, string

if __name__ == '__main__':
    fileName = sys.argv[1]
    fd = None
    wordDict = {}
    
    try:
        fd = open(fileName, 'r+')

        lines = fd.readlines()

        for line in lines:
            words = string.split(line)

            for word in words:
                cnt = 0
                try:
                    cnt = wordDict[word]
                    cnt += 1
                    wordDict[word] = cnt
                except KeyError, e:
                    wordDict[word] = 1
        fd.close()
    except IOError, e:
        print 'Cannot open file', fileName
        sys.exit(1)

    for key in wordDict.keys():
        print key, ' => ', wordDict[key]
