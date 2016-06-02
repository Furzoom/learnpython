#!/usr/bin/env python
#-*- coding: utf-8 -*-

f = open('data.txt', 'w')
size = f.write('Hello\n')
f.write('World\n')
f.close()

f = open('data.txt')
text = f.read()
print(text)
f.close()
