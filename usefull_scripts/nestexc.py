#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def action2():
    print(1 + [])

def action1():
    try:
        action2()
    except TypeError:
        print("inner try")

if __name__ == "__main__":
    def test():
        try:
            action1()
        except TypeError:
            print("outer try")

    test()
