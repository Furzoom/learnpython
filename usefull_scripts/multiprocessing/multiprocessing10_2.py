#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing
import time

def func(num):
    print("message {0}".format(num))
    time.sleep(3)
    print("{0} end".format(num))
    return num

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 3)
    result = []
    for i in xrange(30):
        result.append(pool.apply_async(func, (i,)))

    print("apply done")
    pool.close() # close for apply
    pool.join()

    for res in result:
        print(":::{0}".format(res.get()))
    print("All done")

