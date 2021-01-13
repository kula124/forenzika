from PIL import Image, ImageFilter, ImageChops
from PIL import Image
import numpy as np

# creating a image object
slika = Image.open('slika.png')
slika.load()
img_array1 = np.asarray(slika, dtype='int32')

slika_median = Image.open('median_filter.png')
slika_median.load()
img_array2 = np.asarray(slika_median, dtype='int32')

img_array3 = img_array1 - img_array2

# print(img_array3)

razlika = ImageChops.difference(slika, slika_median)
razlika.save("razlika.png")
