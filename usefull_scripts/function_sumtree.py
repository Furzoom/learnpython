#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def sumtree(L):
    sum = 0
    for x in L:
        if isinstance(x, list):
            sum += sumtree(x)
        else:
            sum += x
    return sum

print(sumtree([1,[2,[3,[4, 5]]]]))
print(sumtree([[[[[1], 2], 3], 4], 5]))
