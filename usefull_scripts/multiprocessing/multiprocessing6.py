import multiprocessing
import time

def worker(s, i):
    s.acquire()
    print("{0} acquire".format(multiprocessing.current_process().name))
    time.sleep(i)
    print("{0} release".format(multiprocessing.current_process().name))
    s.release()

if __name__ == "__main__":
    s = multiprocessing.Semaphore(1)
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(s, 1))
        p.start()


