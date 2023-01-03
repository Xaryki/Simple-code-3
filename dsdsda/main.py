from multiprocessing import Process, Manager
import signal
import os
from random import randint
from datetime import datetime
from time import time, sleep


def create_process(n,mutexinproc):
    try:
        print(f"{'=' * 60}\nRunning:\n"
        f"Children #{n},PID {os.getpid()}, PPID { os.getppid()},"
        f"TIME {datetime.now().time().replace(microsecond=0)}\n{'='*60}\n")
        sleep(2)
        while True:
            mutexinproc.acquire()
            sleep(1)
            mutexinproc.release()
            print(f"{'=-' *23 + '='}\nRunning:\nChildren #{n}, PID {os.getpid()}, PPID { os.getppid()},"
            f"TIME {datetime.now().time().replace(microsecond=0)}\n{'=' * 60}\n"
            f"hold mutex for 1s")
            sleep(5)
    except KeyboardInterrupt:
        terminate_proc()

def terminate_proc():
    print(f"\nProcess {os.getpid()} exit interrupt SIGINT")
    exit(0)

if __name__ == "__main__":
    procs=[]
    manager=Manager()
    mutex=manager.Lock()
    print(f"{'='*60}\nRunning\n")
    print(f"Parent PID {os.getpid()}, PPID {os.getppid()},")
    print(f"TIME {datetime.now().time().replace(microsecond=0)}\n{'=' * 60}\n{'=' * 60}\n")

    for i in range(1,3):
        new_process= Process(target=create_process,args=(i,mutex,))
        procs.append(new_process)
        new_process.start()
        sleep(2)

    while True:
        try:
            timeout = randint(1,10)
            print(f"{'=-'*23+'='}\n Parent, PID {os.getpid()}, PPID {os.getppid()},"
            f"TIME {datetime.now().time().replace(microsecond=0)}\n{'=' * 60}\n{'=' * 60}\n holds mutex for {timeout} sec")
            mutex.acquire()
            sleep(timeout)
            mutex.release()
            sleep(5)
        except KeyboardInterrupt:
            terminate_proc()