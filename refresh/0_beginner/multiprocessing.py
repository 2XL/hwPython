"""
PROCESS VS THREADS

P
    side steps GIL
    less needed for sync
    can be paused  and terminated
    more resilient
T
    higher memory footprint
    expensive context switches



"""

import multiprocessing


def do_some_process(value=None):
    print("doing some task")

    print("echo: {} ".format(value))


if __name__ == "__main__":
    value = "this is a value"
    t = multiprocessing.Process(target=do_some_process, args=(value,))
    t.start()
    t.join()
