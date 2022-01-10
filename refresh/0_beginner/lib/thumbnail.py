# thumbnail.py
import time
import os
import logging
from urllib.parse import urlparse
from urllib.request import urlretrieve

import PIL
from PIL import Image

logging.basicConfig(filename='logfile.log', level=logging.DEBUG)
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
     'https://images.unsplash.com/photo-1641558995768-8d857b3ba1a8', ]


class ThumbnailMakerService(object):
    def __init__(self, home_dir='.'):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'

    def download_images(self, img_url_list):
        """
        network bandwidth intensive
        """
        # validate inputs
        if not img_url_list:
            return
        os.makedirs(self.input_dir, exist_ok=True)

        logging.info("beginning image downloads")

        start = time.perf_counter()
        for url in img_url_list:
            # download each image and save to the input dir
            img_filename = urlparse(url).path.split('/')[-1]
            urlretrieve(url, self.input_dir + os.path.sep + img_filename + '.jpeg')
        end = time.perf_counter()

        logging.info("downloaded {} images in {} seconds".format(len(img_url_list), end - start))

    def perform_resizing(self):
        """
        cpu intensive
        """
        # validate inputs
        if not os.listdir(self.input_dir):
            return
        os.makedirs(self.output_dir, exist_ok=True)

        logging.info("beginning image resizing")
        target_sizes = [32, 64, 200]
        num_images = len(os.listdir(self.input_dir))

        start = time.perf_counter()
        for filename in os.listdir(self.input_dir):
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
        end = time.perf_counter()

        logging.info("created {} thumbnails in {} seconds".format(num_images, end - start))

    def make_thumbnails(self, img_url_list):
        """
        cpu intensive
        """
        logging.info("START make_thumbnails")
        start = time.perf_counter()

        self.download_images(img_url_list)
        self.perform_resizing()

        end = time.perf_counter()
        logging.info("END make_thumbnails in {} seconds".format(end - start))
