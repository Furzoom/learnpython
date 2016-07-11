#!/usr/bin/env python
# -*- coding: utf-8 -*-


def even(n):
    for i in range(n+1):
        if i % 2 == 0:
            print i,
    print


def odd(n):
    for i in range(n+1):
        if i % 2 == 1:
            print i,
    print


def can_divided(m, n):
    if n == 0 or m == 0 or m % n == 0 or n % m == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    even(20)
    odd(20)
    m = int(raw_input('Number 1: '))
    n = int(raw_input('Number 2: '))
    print can_divided(m, n)