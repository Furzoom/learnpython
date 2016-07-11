#!/usr/bin/env python
# -*- coding: utf-8 -*-

n1 = int(raw_input('No.1: '))
n2 = int(raw_input('No.2: '))
n3 = int(raw_input('No.3: '))

if n1 < n2:
    if n1 < n3:
        pass
    else:
        n1, n3 = n3, n1
elif n2 < n3:
    n2, n1 = n1, n2
else:
    n1, n3 = n3, n1

if n2 > n3:
    n2, n3 = n3, n2
print n1, n2, n3


