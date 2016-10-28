#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Foo(object):
    """Foo class definition"""


if __name__ == '__main__':
    for x in dir(Foo):
        print(x)
    print(Foo.__name__)
    print(Foo.__doc__)
    print(Foo.__bases__)
    print(Foo.__dict__)
    print(Foo.__module__)
    print(Foo.__class__)
    print('-' * 30)
    f = Foo()
    print(f.__dict__)
    print(f.__class__)
    for x in dir(f):
        print(x)
