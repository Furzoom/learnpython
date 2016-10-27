#!/usr/bin/env python
# -*- coding: utf-8 -*-


class C(object):
    version = '1.1'

    def __init__(self):
        print(self)
        print(dir(self))


class C1(C):
    def __init__(self):
        C.__init__(self)
        print('initialized')

    def __del__(self):
        # C.__del__(self)
        print('deleted')


class TestStaticMethod:
    @staticmethod
    def foo():
        print('calling static method foo()')


class TestClassMethod:
    @classmethod
    def foo(cls):
        print('calling class method foo()')
        print('foo() is part of class:', cls.__name__)


def test1():
    c = C()


def test2():
    c1 = C1()
    c2 = c1
    c3 = c1
    print(hex(id(c1)), hex(id(c2)), hex(id(c3)))
    del c1
    del c2
    del c3


def test3():
    c1 = TestStaticMethod()
    TestStaticMethod.foo()
    c1.foo()


def test4():
    c1 = TestClassMethod()
    TestClassMethod.foo()
    c1.foo()


class SortedKeyDict(dict):
    def keys(self):
        return sorted(super(SortedKeyDict, self).keys())


def test5():
    d = SortedKeyDict((('zheng-cai', 67), ('hui-jun', 68), ('xin-yi', 2)))
    print('By iterator:'.ljust(12), [key for key in d])
    print('By keys():'.ljust(12), d.keys())


def main():
    #test1()
    test2()
    #test3()
    #test4()
    # test5()


if __name__ == '__main__':
    main()
