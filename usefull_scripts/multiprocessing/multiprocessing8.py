#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing

def write_proc(q):
    try:
        q.put(1, block=False)
    except Exception, e:
        print e
        pass

def read_proc(q):
    try:
        print(q.get())
    except Exception, e:
        print e
        pass

if __name__ == "__main__":
    q = multiprocessing.Queue()
    writer = multiprocessing.Process(target=write_proc, args=(q,))
    reader = multiprocessing.Process(target=read_proc, args=(q,))
    writer.start()
    reader.start()
    writer.join()
    reader.join()

