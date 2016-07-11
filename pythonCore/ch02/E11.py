#!/usr/bin/env python
# -*- coding: utf-8 -*-

item = ''
while item != 'x' and item != 'X':
    print '(1) Calculate sum'
    print '(2) Calculate average'
    print '(x) quit'

    item = raw_input('> ')
    if item == 'x' and item == 'X':
        break

    l = []
    for i in range(1, 6):
        s = raw_input('No.%s: ' % i)
        l.append(int(s))

    if item == '1':
        result = 0
        for i in l:
            result += i
        print result
    elif item == '2':
        result = 0
        for i in l:
            result += i
        result /= float(len(l))
        print result
