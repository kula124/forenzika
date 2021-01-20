from PIL import Image, ImageFilter, ImageChops
import numpy as np

from helper import equalise_rgb, equalise_g, amplify, SeparableMedianFilter


image = Image.open("twa2.png")
image = equalise_rgb(image)
image.show("eq")

#filteredImage = image.filter(ImageFilter.MedianFilter(size=9))
filteredImage = SeparableMedianFilter(image, 3)
filteredImage.save("filtered.png")

noise = ImageChops.difference(image, filteredImage)
noise = amplify(noise, 1)
noise.show()
