#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def cube(l, w, h):
    area = 2 * (l * w + w * h + h * l)
    volume = l * w * h
    return area, volume


def circle(r):
    return math.pi * r ** 2


def sphere(r):
    pi = math.pi
    area = 4 * pi * r ** 2
    volume = float(4) / 3 * pi * r ** 3
    return area, volume


if __name__ == '__main__':
    print cube(1, 2, 3)
    print circle(10)
    print sphere(15)
