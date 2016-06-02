#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class FormatError(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file

def parser():
    raise FormatError(42, file='test.py')

class FormatError2(Exception):
    pass

def parser2():
    raise FormatError2(42, 'test.py')

if __name__ == '__main__':
    def test():
        try:
            parser()
        except FormatError as x:
            print("Error at", x.file, x.line)

        try:
            parser2()
        except FormatError2 as x:
            print("Error at", x.args[0], x.args[1])

    test()

