#!/usr/bin/env python
# -*- coding: utf-8 -*-


def method_a(s):
    l = len(s)
    half_l = l / 2
    i = 0
    while i < half_l:
        print s[i], s[l - 1 - i]
        i += 1
    if l % 2 != 0:
        print s[i],
    print ''


def method_b(s):
    l = len(s)
    string = 'furzoom'
    if s in string and string in s:
        return True
    else:
        return False


def method_c(s):
    l = len(s)
    half_l = l / 2
    i = 0
    while i < half_l:
        if s[i] != s[-i - 1]:
            return False
        i += 1
    else:
        return True


def method_d(s):
    l = list(s)
    l.reverse()
    return s + ''.join(l)


def main():
    s = raw_input("Input a string: ")
    method_a(s)
    print method_b(s)
    print method_c(s)
    print method_d(s)


if __name__ == '__main__':
    main()
