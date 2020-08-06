# try decorator

class entryExit(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print "Entering ", self.f.__name__
        self.f()
        print "Exiting ", self.f.__name__

@entryExit
def func1():
    print "inside func1()"

func1()
