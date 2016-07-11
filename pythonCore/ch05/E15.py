#!/usr/bin/env python
# -*- coding: utf-8 -*-


def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m


def lcm(m, n):
    return m * n / gcd(m, n)


if __name__ == '__main__':
    print gcd(12, 20)
    print gcd(20, 12)
    print lcm(12, 20)
    print lcm(20, 12)
