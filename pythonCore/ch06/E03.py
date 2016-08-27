#!/usr/bin/env python
# -*- coding: utf-8 -*-

inp = []
input_s = []

while True:
    a = raw_input("Input a number(<ENTER> to stop): ")
    if len(a.strip()) == 0:
        break
    inp.append(int(a))
    input_s.append(a)

inp.sort()
input_s.sort()
for x in inp:
    print x,
print ''

for x in input_s:
    print x,
print ''



