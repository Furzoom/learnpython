#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps

def use_logging(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('{} is running'.format(func.__name__))
        return func(*args, **kwargs)

    return wrapper


@use_logging
def foo():
    print('I am foo')


@use_logging
def bar():
    print('I am bar')


if __name__ == '__main__':
    foo()
    bar()
    print(foo.__name__)
