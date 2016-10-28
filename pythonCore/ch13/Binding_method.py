#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Foo(object):
    def say(self):
        print('hello')


if __name__ == '__main__':
    print(Foo.__dict__)
    f = Foo()
    print(f.__dict__)
