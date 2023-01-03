import os
from datetime import datetime

if __name__ == "__main__":
    r, w = os.pipe()
    print(f"Parent, PID {os.getpid()},PPID {os.getppid()}, TIME {datetime.now().time()}\n")

    pid = os.fork()

    #Parent
    if pid > 0:
        os.close(w)
        read = os.fdopen(r)
        for text in read.readline():
            print(f"{os.getpid()} {text} ")

    #Child
    else:
        os.close(r)
        for i in range(1, 101):
            text = bytes(f"{i} {os.getpid()} {datetime.now().time()}\n")
            os.write(w, text)
