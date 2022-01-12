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
import ctypes
import os
import random
from multiprocessing import Process, Pipe, Value, Lock
from threading import Thread


def do_some_process(value=None):
    print("doing some task")

    print("echo: {} ".format(value))


def multi_process():
    """
    multi_process
    """

    # pools
    from lib.thumbnail import ThumbnailMakerService, IMG_URLS, TB_SIZES
    tn_maker = ThumbnailMakerService(tb_sizes=TB_SIZES)
    tn_maker.mp_make_thumbnails(IMG_URLS)
    pass


def async_map():
    """
    map_async => func
        iterable
            chunk_size
                callback_func

    returns Async Result

    AsyncResult.get =>
        timeout

    returns when result available.

    apply => func
        args
            kwargs

    async_apply => func
        args
            kwargs
                callback
                    error_callback


    """


def inter_process_communication():
    """
    Pipe (duplex (default) /unidirectional)
    Queue

    Intercommunication mechanism among process
    """

    def make_number(conn):
        num = random.randint(1, 10)
        conn.send(('Hi', num))
        print(conn.recv())
        pass

    def make_text(conn):
        num = conn.recv()[1]  # wait for msg
        result = "{} * {} = {}".format(num, num, num * num)

        conn.send(result)

    connA, connB = Pipe(duplex=True)  # returns both ends of pipe
    """
    Race condition will corrupt data
    """
    """
    Queue ensure data consistency
    
    
    threading.Queue -> 
        qsize
        put
        get
        empty
        full
        task_done
        join
    multiprocessing.Queue -> 
        qsize
        put
        get
        empty
        full
    multiprocessing.JoinableQueue -> # 100% api compatibility 
        qsize
        put
        get
        empty
        full
        task_done
        join
    
    
    """
    if os.environ.get('DEBUG', False):
        p1 = Thread(target=make_text, args=(connA,))
        p2 = Thread(target=make_number, args=(connB,))
    else:
        p1 = Process(target=make_text, args=(connA,))
        p2 = Process(target=make_number, args=(connB,))
    p1.start()
    p2.start()
    pass


def sharing_states_between_process():
    # error-prone hard to maintain.
    """

    ctypes:
        - c > char
        - u -> string
        - i -> int
        - l -> long
        - f -> fload

    Shared State:
        - Shared Memory
            - multiprocessing.Value ->
                    typecode_or_type
                        -> *args
                            -> kw,
                            -> lock Default type
            - multiprocessing.Array ->

        - Manager Process
            is a shared process containing the mechanisms to arbitrate resources
            - allow sharing across network (each client with proxy) - nameko

            multiprocessing.Manager() # spins up a new process
                - when this terminates, the child process will be garbage collected
                data structures
                    value
                    array
                    list
                    dict
                    namespace
                    queue
                sync mechanism
                    lock
                    rlock
                    bounded semaphore
                    event
                    condition
                    barrier

    """

    """
    when use threads and when use process
    THE Major difference are:-
        1. Threads share address space of process that created it;processes have their own address
        
        2.Threads can directly communicate with other threads of its process;processes must use INTERPROCESS COMMUNICATE to talk with sibling processes.
        
        3.New threads are easily created;new processes require DUPLICATION of parent process
        
        4.Threads can exercise control over threads of same process;processes can only exercise control over child processes.
        
        5.Changes to the main thread(cancellation,priority change,etc)may affect
        the behaviour of other threads of process;changes to parent process does not affect child processes
    
    """

    counter = Value('i')  # counter
    is_running = Value(ctypes.c_bool, False, lock=False)  # shared obj type boolean, defaulting false, un-synchronized
    my_lock = Lock()
    size_counter = Value('l', 0, lock=my_lock)  # shared object of type long, with a lock specified, default 0

    pass


if __name__ == "__main__":
    value = "this is a value"
    t = Process(target=do_some_process, args=(value,))
    t.start()
    t.join()
    # monolith()
    # sample_class_thread()
    # multi_process()
    inter_process_communication()

    pass
