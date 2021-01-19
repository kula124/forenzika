from PIL import Image, ImageFilter, ImageChops
import numpy as np

from helper import equalise_rgb, equalise_g, amplify


image = Image.open("twa2.png")
image = equalise_g(image)
image.show("eq")

filteredImage = image.filter(ImageFilter.MedianFilter(size=9))

noise = ImageChops.difference(image, filteredImage)
noise = amplify(noise, 5)
noise.show()
