#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing
import time

def func(num):
    print("message {0}".format(num))
    time.sleep(3)
    print("{0} end".format(num))

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 3)
    for i in xrange(30):
        pool.apply_async(func, (i,))

    print("apply done")
    pool.close() # close for apply
    pool.join()
    print("All done")

