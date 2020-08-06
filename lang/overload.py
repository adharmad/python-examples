# operator overloading
class Foo:
    def __init__(self):
        pass

    def __lt__(self, other):
        print "We are here\n"
        return 1

if __name__ == '__main__':
    f1 = Foo()
    f2 = Foo()

    i = f1 < f2
