#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing
import time

def write_proc(q):
    for i in xrange(10000):
        try:
            q.put(i, block=False)
        except Exception, e:
            print e
            pass
        time.sleep(1)


def read_proc1(q):
    while True:
        try:
            print("proc1: {0}".format(q.get()))
        except Exception, e:
            print e
            pass

def read_proc2(q):
    while True:
        try:
            print("proc2: {0}".format(q.get()))
        except Exception, e:
            print e
            pass

if __name__ == "__main__":
    q = multiprocessing.Queue()
    writer = multiprocessing.Process(target=write_proc, args=(q,))
    reader1 = multiprocessing.Process(target=read_proc1, args=(q,))
    reader2 = multiprocessing.Process(target=read_proc2, args=(q,))
    writer.start()
    reader1.start()
    reader2.start()

    writer.join()
    reader1.join()
    reader2.join()

