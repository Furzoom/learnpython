#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def gen_list(n, num_range):
    l = []
    for i in range(n):
        l.append(random.randrange(num_range))

    print l
    l2 = []
    for i in range(n):
        l2.append(random.choice(l))
    return sorted(l2)

if __name__ == '__main__':
    print gen_list(10, 200)
