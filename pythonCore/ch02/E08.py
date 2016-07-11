#!/usr/bin/env python
# -*- coding: utf-8 -*-

l = []
for i in range(5):
    s = raw_input('input a number: ')
    l.append(int(s))

sum = 0
for i in l:
    sum += i
print sum

i = 0
sum = 0
while i < len(l):
    sum += l[i]
    i += 1
print sum

