#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)

    def __neg__(self):
        return Number(- self.data)

    def __str__(self):
        return '[Number: {0}]'.format(self.data)


if __name__ == '__main__':
    def test():
        numA = Number(5)
        numB = Number(15)
        print(numA - 1)
        print(10 - numA)


    test()
