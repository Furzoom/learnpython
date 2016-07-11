#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = raw_input('Input a number: ')
i = int(s)
while i > 100 or i < 0:
    s = raw_input('Input a number: ')
    i = int(s)
print i
