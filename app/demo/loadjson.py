#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def test():
    s = '{"a": "b"}'
    # s = u'["a", "b"]'
    # s = '"\""'
    d = dict()
    try:
        d = json.loads(s)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    print(d)


if __name__ == '__main__':
    test()
