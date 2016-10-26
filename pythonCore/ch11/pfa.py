#!/usr/bin/env python
# -*- coding: utf-8 -*-


from operator import add
from operator import mul
from functools import partial


def test():
    add1 = partial(add, 1)
    mul100 = partial(mul, 100)

    print(add1(10))
    print(mul100(2))


if __name__ == '__main__':
    test()
