__author__ = 'MN'

from time import ctime
from time import sleep

def tsfunc(func):
    def wrapperFunc():
        print('[{}] {}() called'.format(ctime(), func.__name__))
        return func
    return wrapperFunc


@tsfunc
def foo():
    pass


def main():
    for i in range(4):
        sleep(1)
        foo()


if '__main__' == __name__:
    main()
