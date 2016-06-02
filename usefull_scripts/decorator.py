#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)

@tracer
def spam(a, b, c):
    print(a, b, c)
@tracer
def ham(a, b):
    print(a, b)

spam(1, 2, 3)
spam('a', 'b', 'c')
spam(4, 5, 6)
ham(7, 8)
spam(7, 8, 9)
