#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    s = 'Welcome furzoom'
    s1 = 'fur'
    s2 = 'mn'

    test(s1, s)
    test(s2, s)
    print s1 in s


def test(s1, s2):
    if s2.find(s1) != -1:
        print s1, 'is in', s2
    else:
        print s1, 'is not in', s2


if __name__ == '__main__':
    main()
