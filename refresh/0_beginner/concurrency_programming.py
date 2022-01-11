"""
concurrency in python (1.*, 2.*, 3.* )

3.2+ concurrent.futures
    1.5+ threading
    2.6+ multiprocessing

3.4+ asyncio
"""
import threading
from threading import Thread

"""
Moore's law -> end of moore's law?
from single to -> multitask -> multicore
1. monolith
2. one guy doing everything
3. teamwork
"""

"""
Concepts:
    - order of execution does not affect the eventual outcome
    - shared resources, as much as possible require coordination (keep a threshold) 
    - design patterns: 
        parallel / (same time same task) 
        async program / (same time, chunk of task, subtask)
        map - reduce
"""


def monolith():
    """
    code is single threaded / process
    the execution context of a running program
    a running instance of a computer program

    thread:> the smallest sequence of instructions that can be managed by the operating system
    thread pool:> context managers of coworkers
    run
    ```pytest```
    """
    # import pytest
    # pytest.main(['-s', './lib/thumbnail.test.py'])
    from lib.thumbnail import ThumbnailMakerService, IMG_URLS
    tn_maker = ThumbnailMakerService()
    tn_maker.make_thumbnails(IMG_URLS)
    pass


def multitask():
    """
    multithreading
    """
    from lib.thumbnail import ThumbnailMakerService, IMG_URLS
    tn_maker = ThumbnailMakerService()
    tn_maker.make_thumbnails(IMG_URLS)
    pass


def do_task(input):
    print("doing: ", input)
    return


def sample_thread():
    """
    thread invoke
    """
    text = "text"
    arguments = (None,)
    t = threading.Thread(
        target=do_task,
        args=arguments,  # argument can be (tuple) positional or kw {dict}
        # daemon= # parent pid watchdog
    )
    t.start()  # none blocking
    t.join()


class FibonacciThread(threading.Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self) -> None:
        fib = [0] * (self.num + 1)
        fib[0] = 0
        fib[1] = 1
        for i in range(2, self.num + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
            print(self.num, fib[self.num], i)
        pass


def sample_class_thread():
    fib = FibonacciThread(5)
    fib2 = FibonacciThread(12)

    fib.start()
    fib2.start()

    fib.join()
    fib2.join()


def download():
    pass


def rescale():
    pass


if __name__ == "__main__":
    # monolith()
    # sample_class_thread()
    multitask()
    pass
