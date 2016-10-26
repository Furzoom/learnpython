#!/usr/bin/env python
# -*- coding: utf-8 -*-


global_str = 'foo'


def foo():
    print('calling foo()...')
    bar = 200
    print('in foo(), bar is {}'.format(bar))


bar = 100
print('in __main__, bar is {}'.format(bar))
foo()
print('in __main__, bar is (still) {}'.format(bar))


if __name__ == '__main__':
    # print(foo())
    pass