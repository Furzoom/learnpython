#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested
