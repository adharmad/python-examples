# try decorator

class myDecorator(object):

    def __init__(self, f):
        print "inside myDecorator.__init__()"
        f()

    def __call__(self):
        print "inside myDecorator.__call__()"

@myDecorator
def aFunction():
    print "inside aFunction()"

aFunction()
print "done!
