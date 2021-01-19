from PIL import Image, ImageFilter, ImageChops
import numpy as np

from helper import equalise_rgb, equalise_g


image = Image.open("twa2.png")
image = equalise_rgb(image)

filteredImage = image.filter(ImageFilter.MedianFilter(size=9))

noise = ImageChops.difference(image, filteredImage)
noise.show()
