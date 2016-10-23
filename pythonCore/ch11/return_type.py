#!/usr/bin/env python
# -*- coding: utf-8 -*-


def foo():
    return ['xyz', 100000, -98.6]


def bar():
    return 'abc', [42, 'python'], "Guido"


if __name__ == '__main__':
    print(foo())
    print(bar())
    x, y, z = bar()
    print(x, y, z)
    print(type(foo()))
