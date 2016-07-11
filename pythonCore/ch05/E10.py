#!/usr/bin/env python
# -*- coding: utf-8 -*-


def transform(f):
    return (f - 32) * float(5) / 9


if __name__ == '__main__':
    for i in range(0, 300, 10):
        print transform(i)
