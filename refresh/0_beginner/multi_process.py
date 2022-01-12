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

Pickling
    is the process whereby a Python object hierarchy is converted into a byte stream.
    "unpickling" is the inverse operation

    serialization, un-serialization
Daemon process
    is a child process that does not prevent its parent process from exiting

Termination signals OS API
    p.is_alive()
    p.terminate() -> shared resources may be put in an inconsistent state, finally clauses and exit handlers will not be run
    p.join()
    p.start()

Multiprocessing Pools # allocate a pool of consumers ready to do tasks
    Pool[
    #worker_process, # default # cpu cores -> multiprocessing.cpu_count()
        [#func
            [#args # not required to be pickable -> serialization
                [#task_x_child # force to release the resources periodically
                ]
            ]
        ]
    ]


output = pool.map(function, arguments) # arguments must be pickable

pool.close() # no more tasks are accepted
pool.join() # wait for the workers process to exit


"""

# import multiprocessing
from multiprocessing import Process


def do_some_process(value=None):
    print("doing some task")

    print("echo: {} ".format(value))


if __name__ == "__main__":
    value = "this is a value"
    t = Process(target=do_some_process, args=(value,))
    t.start()
    t.join()
