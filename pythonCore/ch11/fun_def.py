#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Function definition sample."""


def foo(bar):
    """foo() - Output a string.
    Args:
        bar: A string to be printed
    Returns:
        None
    Raises:
        No exceptions
    """
    print('in foo({})'.format(bar))


if __name__ == '__main__':
    foo('yes')
    print(foo.__doc__)
