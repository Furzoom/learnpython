#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cal(expr):
    a, op, b = expr.split()
    a = float(a)
    b = float(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b:
            return a / b
        else:
            return 'error'
    elif op == '%':
        return a % b
    elif op == '**':
        return a ** b
    else:
        return 'error'


if __name__ == '__main__':
    s = raw_input('input a expression: ')
    print cal(s)
