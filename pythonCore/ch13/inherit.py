#!/usr/bin/env python
# -*- coding: utf-8 -*-


class P(object):
    """P class"""
    def __init__(self):
        print('created an instance of {}'.format(self.__class__.__name__))

    def say(self):
        self.sayHello()

    def sayHello(self):
        print('hello P')


class C(P):
    def sayHello(self):
        print('Hello C')


if __name__ == '__main__':
    p = P()
    c = C()
    c.say()
    print(c.__doc__)
    print(C.__doc__)
    print(C.__base__)
    print(C.__bases__)
    P.sayHello(c)

