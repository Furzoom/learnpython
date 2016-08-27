#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def main():
    filename = raw_input("Enter file name: ")
    fobj = open(filename, 'w')
    while True:
        aLine = raw_input("Enter a line('.' to quit): ")
        if aLine == '.':
            break
        else:
            fobj.write('%s%s' % (aLine, os.linesep))
    fobj.close()


if __name__ == '__main__':
    main()
