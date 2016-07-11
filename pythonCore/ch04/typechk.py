#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" typechk.py -- check object number type"""


def display_num_type(num):
    print num, 'is',
    if isinstance(num, (int, long, float, complex)):
        print 'a number of type:', type(num).__name__
    else:
        print 'not a number at all!!'


display_num_type(1)
display_num_type(9999999999999999999999)
display_num_type(1.2)
display_num_type(1+1j)
display_num_type('furzoom')
