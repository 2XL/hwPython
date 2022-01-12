# thumbnail.py
import multiprocessing
import threading
import time
import os
import logging
import yaml
import PIL

from urllib.parse import urlparse
from urllib.request import urlretrieve
from PIL import Image
from queue import Queue, Empty
from threading import Thread, Lock

FORMAT = "[%(threadName)10s, %(asctime)s, %(levelname)s] %(message)s]"

logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format=FORMAT)

settings_path = 'media/source.yml'
with open(settings_path, 'r') as stream:
    data_loaded = yaml.safe_load(stream)
    pass

IMG_URLS = data_loaded['image_urls']
TB_SIZES = data_loaded['thumbnail_sizes']


class ThumbnailMakerService(object):
    def __init__(self, home_dir='.', max_threads=4, tb_sizes=[200, ]):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'
        self.img_queue = multiprocessing.JoinableQueue()
        self.dl_size = 0
        self.tb_sizes = tb_sizes

    def mp_download_image(self, dl_image_list, dl_size_lock=None):
        # validate inputs
        if not dl_image_list:
            return
        os.makedirs(self.input_dir, exist_ok=True)
        # with self.dl_sem:
        logging.info("beginning image downloads")

        start = time.perf_counter()
        while not dl_image_list.empty():  # while image queue not empty
            try:
                url = dl_image_list.get(block=False)

                destination_path = self.input_dir + os.path.sep
                img_filename = urlparse(url).path.split('/')[-1] + ".jpeg"
                urlretrieve(url, destination_path + img_filename)
                with dl_size_lock:
                    self.dl_size += os.path.getsize(destination_path + img_filename)
                dl_image_list.task_done()
                self.img_queue.put(img_filename)
            except Empty as ex:
                print(ex)
                logging.info("dl img queue empty")
                pass

        end = time.perf_counter()

        self.img_queue.put(None)

        # while not dl_image_list.empty():  # while image queue not empty
        #     try:
        #         url = dl_image_list.get(block=False)
        #
        #         destination_path = self.input_dir + os.path.sep
        #         img_filename = urlparse(url).path.split('/')[-1] + ".jpeg"
        #         urlretrieve(url, destination_path + img_filename)
        #         self.img_queue.put(img_filename)
        #         with dl_size_lock:
        #             self.dl_size += os.path.getsize(destination_path + img_filename)
        #         self.img_queue.put(destination_path + img_filename)
        #         dl_image_list.task_done()
        #     except Empty as ex:
        #         print(ex)
        #         logging.info("dl img queue empty")
        #         pass

    def mp_resize_image(self):

        # validate inputs
        os.makedirs(self.output_dir, exist_ok=True)
        target_sizes = self.tb_sizes

        while True:
            filename = self.img_queue.get()
            if filename:
                orig_img = Image.open(self.input_dir + os.path.sep + filename)
                for base_width in target_sizes:
                    img = orig_img
                    # calculate target height of the resized image to maintain the aspect ratio
                    w_percent = (base_width / float(img.size[0]))
                    hsize = int((float(img.size[1]) * float(w_percent)))
                    # perform resizing
                    img = img.resize((base_width, hsize), PIL.Image.LANCZOS)

                    # save the resized image to the output dir with a modified file name
                    new_filename = os.path.splitext(filename)[0] + \
                                   '_' + str(base_width) + os.path.splitext(filename)[1]
                    img.save(self.output_dir + os.path.sep + new_filename)
                # os.remove(self.input_dir + os.path.sep + filename)
                self.img_queue.task_done()
            else:
                self.img_queue.task_done()
                break
            pass

    def mp_make_thumbnails(self, img_url_list):
        """
        cpu intensive
        """
        logging.info("START make_thumbnails")
        start = time.perf_counter()

        dl_queue = Queue()
        dl_size_lock = Lock()

        for img_url in img_url_list:
            dl_queue.put(img_url)

        num_dl_threads = 8
        for _ in range(num_dl_threads):
            t_producer = Thread(target=self.mp_download_image, args=(dl_queue, dl_size_lock))
            t_producer.start()

        num_processes = multiprocessing.cpu_count()
        for _ in range(num_processes):
            p = multiprocessing.Process(target=self.mp_resize_image)
            p.start()

        dl_queue.join()
        for _ in range(num_processes):
            self.img_queue.put(None)
        end = time.perf_counter()
        logging.info("END make_thumbnails in {} seconds".format(end - start))
