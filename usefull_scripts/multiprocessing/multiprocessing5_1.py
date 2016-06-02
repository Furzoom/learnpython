import multiprocessing
import sys
import time

def worker_with(f):
        fs = open(f, 'a+')
        n = 10
        while n > 1:
            fs.write("Locked acquired via with\n")
            time.sleep(1)
            n -= 1
        fs.close()

def worker_no_with(f):
        fs = open(f, 'a+')
        n = 10
        while n > 1:
            fs.write("Locked acquired via directly\n")
            n -= 1
            time.sleep(1)
        fs.close()


if __name__ == "__main__":
    lock = multiprocessing.Lock()
    f = 'file.txt'
    w = multiprocessing.Process(target=worker_with, args=(f,))
    nw = multiprocessing.Process(target=worker_no_with, args=(f,))
    w.start()
    nw.start()
    print('end')
