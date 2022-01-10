"""
Resources

Program elements that must be released or closed after use
python provides special syntax for managing resources.

"""
import pdb
import pprint
import sys
from io import TextIOWrapper

def file_like_objects():
    """
    objects that behave like files
    a semi-formal protocol
    file behaviours are too varied for fully specified proto
    EAFP - if it looks like a file, and reads like a file then it's a file (smart mode)
    """
def open_files():
    """

    mode[0]: r/w/a => read/write/append
    mode[1]: b/t => binary/text

    build in open
    """

    f = open('data/dataset.txt', mode='at', encoding='utf-8')

    # print(help(f))
    f.writelines("N")
    f.write("O")
    f.write("L")
    f.write("L")
    f.write("\n")
    f.close()

    read_file = open('data/dataset.txt', mode='rt', encoding='utf-8')
    index = 0
    for line in read_file:
        index += 1
        print(index, line, "0tell position", line, line)
    pass
    read_file.close()

    read_file = open('data/dataset.txt', mode='rt', encoding='utf-8')
    line = read_file.seek(5)
    print("1tell position", line, read_file.tell())  # tells the file size
    print(read_file.seek(0))
    print("2tell position", line, read_file.tell())
    read_file.close()


def with_context():
    """
    BMP writer => module for dealing with BMP bitmap images files
    Control flow structure for managing resources
        sugar
        syntactic sugar
    """

    from contextlib import closing
    # create our own context manager
    # with closing( instance close method ) as context_id:


    """Computing Mandelbrot sets."""

    import math

    def mandel(real, imag):
        """The logarithm of number of iterations needed to
        determine whether a complex point is in the
        Mandelbrot set.

        Args:
            real: The real coordinate
            imag: The imaginary coordinate

        Returns:
            An integer in the range 1-255.
        """
        x = 0
        y = 0
        for i in range(1, 257):
            if x * x + y * y > 4.0:
                break
            xt = real + x * x - y * y
            y = imag + 2.0 * x * y
            x = xt
        return int(math.log(i) * 256 / math.log(256)) - 1

    def mandelbrot(size_x, size_y):
        """Make an Mandelbrot set image.

        Args:
            size_x: Image width
            size_y: Image height

        Returns:
            A list of lists of integers in the range 0-255.
        """
        return [[mandel((3.5 * x / size_x) - 2.5,
                        (2.0 * y / size_y) - 1.0)
                 for x in range(size_x)]
                for y in range(size_y)]

    ratio = (7, 4)
    rescale = 1024

    size = [item * rescale for item in ratio]
    pixels = mandelbrot(*size)  # best result 7:4 ratio

    from reprlib import repr
    image_pix = repr(pixels)

    from lib.bmp import write_grayscale
    image_file = 'output/google.bmp'
    write_grayscale(image_file, pixels)
    rotate_image(image_file)
    # pprint.pprint(image_pix)

    pass


def rotate_image(image_file, degree=90):
    # import the Python Image processing Library

    from PIL import Image

    # Create an Image object from an Image

    image = Image.open(image_file)

    # Rotate it by 45 degrees

    rotated = image.rotate(degree)

    rotated.save(image_file)

    # Rotate it by 90 degrees

    # transposed = colorImage.transpose(Image.ROTATE_90)

    # Display the Original Image

    # colorImage.show()

    # Display the Image rotated by 45 degrees

    # rotated.show()

    # Display the Image rotated by 90 degrees

    # transposed.show()


if __name__ == "__main__":
    print(sys.getdefaultencoding())

    # pdb
    # open_files()
    # with_context()
    pass
