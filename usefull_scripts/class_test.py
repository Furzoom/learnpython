#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[ThirdClass: %s]' % self.data
    def mul(self, other):
        self.data *= other

if __name__ == '__main__':
    a = ThirdClass('abc')
    a.display()
    print(a)
    b = a + 'xyz'
    b.display()
    print(b)
    a.mul(3)
    print(a)
    b = '123' + a
    b.display()
