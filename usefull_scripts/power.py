#!/usr/bin/env python3
#-*- coding: utf-8 -*-

L = list(map(lambda x: 2 **x, range(7)))
X = 5
obj = 2 ** X

if obj in L:
    print('at index', L.index(obj))
else:
    print(X, 'not found')

