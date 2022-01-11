# thumbnail.py
import threading
import time
import os
import logging
from urllib.parse import urlparse
from urllib.request import urlretrieve

import PIL
from PIL import Image
from queue import Queue
from threading import Thread

FORMAT = "[%(threadName)10s, %(asctime)s, %(levelname)s] %(message)s]"

logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format=FORMAT)
IMG_URLS = \
    ['https://images.unsplash.com/photo-1641821330404-765069b99aa2',
     'https://images.unsplash.com/photo-1641735123812-2c82e2d7b691',
     'https://images.unsplash.com/photo-1634544205365-ff8a96e06879',
     'https://images.unsplash.com/photo-1639972997539-ce6fd166fac4',
     'https://images.unsplash.com/photo-1582026416561-32c1a90e832f',
     'https://images.unsplash.com/photo-1639864191241-c3ba360d8c5f',
     'https://images.unsplash.com/photo-1576777486781-4fc7184eb4f8',
     'https://images.unsplash.com/photo-1640098178528-27bf4b399da3',
     'https://images.unsplash.com/photo-1630643596685-d9117d5f68ed',
     'https://images.unsplash.com/photo-1641170254514-0298cc8314aa',
     'https://images.unsplash.com/photo-1641236709013-3e1583f4a53d',
     'https://images.unsplash.com/photo-1624005355480-1ad6131cff7d',
     'https://images.unsplash.com/photo-1622424114500-24202766581f',
     'https://images.unsplash.com/photo-1641558995768-8d857b3ba1a8',
     ]


class ThumbnailMakerService(object):
    def __init__(self, home_dir='.', max_threads=4):
        self.threads_running = 0
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'
        self.downloaded_bytes_counter = 0
        self.downloaded_images_counter = 0
        self.dl_lock = threading.Lock()
        self.max_threads = max_threads  # run & check no more than max_threads are running at the same time
        self.dl_sem = threading.Semaphore(self.max_threads)

        """
        # thread level mechanism for concurrency
        if lock.acquire(False):
            lock acquired, do stuff with lock
        else:
            could not acquire lock, do other stuff
            
        if lock.locked():
            do stuff
        else:
            lock.acquire()    
        
        Lock() -> same thread cannot take acquire another lock until previously unlock
        RLock() -> this call won't block if call lock twice (thread can acquire multiple times)
        """

        # self.dl_semaphore = threading.BoundedSemaphore() # single
        """
        # semaphore is a inter . threading concurrency mechanism to handle race condition
        self.dl_semaphore.acquire() -> counter decremented
        self.dl_semaphore.release() -> increment
        -> internal call can never go below 0
        
        must wait another thread to call release to
        
        # BoundedSemaphore(num_permits) 
        # allow more than x concurrent calls, limit concurrency o protect against gateway burst limit  
        
        """

        """
        threading.Event
        
        event = threading.Event()
        # a client thread can wait for the flag to be set
        event.wait() -> block if false
        @ a server thread can set or reset it
        event.set() -> block set the flag to true
        event.clear() -> resets the flag to false
        """

        """
        threading.Condition
        -> producer/consumer -> each task is consumed by single worker
        acquire()
        release()
        wait()
        notify()
        notify_all()
        
        """

        """
        queue
        """
        self.img_queue = Queue()
        self.dl_queue = Queue()


        """
        Global Interpreter Lock
        
        a lock that prevents multiple native threads from executing python code at the same time 
        
        Singleton 
        single thread multiprocessing
        """


    def download_images(self, img_url_list):
        """
        network bandwidth intensive

        thread lifecycle

        1. new (instance) ->
        2. ready (instance.start) ->
        3. running (instance.join) ->
        4. terminated -> return status 0

        blocked: io or resource competition

        The Scheduler： an os module that selects the next jobs to be admitted into the system and the next process to run
        Context Switch: the process of saving and restoring the state of a thread or process
        Thread Interference: race condition for resource
        Thread Synchronization: + memo allocated + interference prone

        Mechanism to handle synchronization:
        from threading import { Lock , Unlock}




        """
        # validate inputs
        if not img_url_list:
            return
        os.makedirs(self.input_dir, exist_ok=True)
        logging.info("beginning image downloads")

        start = time.perf_counter()
        t_list = []
        """
        [Thread-2, 2022-01-11 16:50:30,254, INFO] img saved at: ./incoming/photo-1641735123812-2c82e2d7b691.jpeg]
        [Thread-6, 2022-01-11 16:50:30,328, INFO] img saved at: ./incoming/photo-1639864191241-c3ba360d8c5f.jpeg]
        [Thread-7, 2022-01-11 16:50:30,360, INFO] img saved at: ./incoming/photo-1576777486781-4fc7184eb4f8.jpeg]
        [Thread-1, 2022-01-11 16:50:30,391, INFO] img saved at: ./incoming/photo-1641821330404-765069b99aa2.jpeg]
        [Thread-12, 2022-01-11 16:50:30,458, INFO] img saved at: ./incoming/photo-1624005355480-1ad6131cff7d.jpeg]
        [Thread-14, 2022-01-11 16:50:30,745, INFO] img saved at: ./incoming/photo-1641558995768-8d857b3ba1a8.jpeg]
        [Thread-4, 2022-01-11 16:50:31,057, INFO] img saved at: ./incoming/photo-1639972997539-ce6fd166fac4.jpeg]
        [Thread-9, 2022-01-11 16:50:31,537, INFO] img saved at: ./incoming/photo-1630643596685-d9117d5f68ed.jpeg]
        [Thread-10, 2022-01-11 16:50:31,792, INFO] img saved at: ./incoming/photo-1641170254514-0298cc8314aa.jpeg]
        [Thread-8, 2022-01-11 16:50:31,888, INFO] img saved at: ./incoming/photo-1640098178528-27bf4b399da3.jpeg]
        [Thread-13, 2022-01-11 16:50:32,211, INFO] img saved at: ./incoming/photo-1622424114500-24202766581f.jpeg]
        [Thread-3, 2022-01-11 16:50:32,633, INFO] img saved at: ./incoming/photo-1634544205365-ff8a96e06879.jpeg]
        [Thread-5, 2022-01-11 16:50:33,173, INFO] img saved at: ./incoming/photo-1582026416561-32c1a90e832f.jpeg]
        [Thread-11, 2022-01-11 16:50:35,369, INFO] img saved at: ./incoming/photo-1641236709013-3e1583f4a53d.jpeg]
        [MainThread, 2022-01-11 16:50:35,369, INFO] downloaded 14 images in 5.428619718000846 seconds]
        [MainThread, 2022-01-11 16:50:35,369, INFO] END make_thumbnails in 5.42890760499904 seconds]
        """
        for url in img_url_list:
            # download each image and save to the input dir
            t = threading.Thread(target=self.download_image, args=(url,))
            t_list.append(t)
            t.start()

        [t.join() for t in t_list]

        end = time.perf_counter()
        self.dl_queue.put(None)  # termination condition for consumer
        logging.info("downloaded {} images in {} seconds".format(len(img_url_list), end - start))

    def download_image(self):
        # with self.dl_sem:
        while not self.dl_queue.qsize() == 0:  # while image queue not empty
            try:
                url = self.dl_queue.get(block=False)
                destination_path = self.input_dir + os.path.sep
                logging.info('downloading image at ' + url)
                img_filename = urlparse(url).path.split('/')[-1] + '.jpeg'
                urlretrieve(url, destination_path + img_filename)
                img_size = os.path.getsize(destination_path + img_filename)
                # with self.dl_lock:
                #     self.downloaded_bytes_counter += img_size
                #     self.downloaded_images_counter += 1
                logging.info("%s %10s%s %s" % (
                    str(self.threads_running), str(self.downloaded_bytes_counter), ' bytes: img saved at: ',
                    img_filename))
                self.img_queue.put(img_filename)
                self.dl_queue.task_done()
            except Queue.Empty as ex:
                print(ex)
                logging.info("dl img queue empty")
                pass

    def perform_resizing(self):
        """
        cpu intensive
        """
        os.makedirs(self.output_dir, exist_ok=True)

        logging.info("beginning image resizing")
        target_sizes = [32, 64, 200]
        num_images = len(os.listdir(self.input_dir))

        start = time.perf_counter()

        while True:
            filename = self.img_queue.get()
            if filename is None:
                break
            orig_img = Image.open(self.input_dir + os.path.sep + filename)
            for basewidth in target_sizes:
                img = orig_img
                # calculate target height of the resized image to maintain the aspect ratio
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                # perform resizing
                img = img.resize((basewidth, hsize), PIL.Image.LANCZOS)

                # save the resized image to the output dir with a modified file name
                new_filename = os.path.splitext(filename)[0] + \
                               '_' + str(basewidth) + os.path.splitext(filename)[1]
                img.save(self.output_dir + os.path.sep + new_filename)

            os.remove(self.input_dir + os.path.sep + filename)
            self.img_queue.task_done()
        end = time.perf_counter()

        logging.info("created {} thumbnails in {} seconds".format(num_images, end - start))

    def make_thumbnails(self, img_url_list):
        """
        cpu intensive
        """
        logging.info("START make_thumbnails")
        start = time.perf_counter()

        for img_url in img_url_list:
            self.dl_queue.put(img_url)

        num_dl_threads = 8
        for _ in range(num_dl_threads):
            t_producer = Thread(target=self.download_image)
            t_producer.start()

        t_consumer = threading.Thread(target=self.perform_resizing)
        t_consumer.start()
        self.dl_queue.join()
        self.img_queue.put(None)
        t_consumer.join()

        end = time.perf_counter()
        logging.info("END make_thumbnails in {} seconds".format(end - start))
