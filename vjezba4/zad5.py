import numpy as np
from PIL import Image, ImageFilter, ImageChops
from PIL import Image

# slika 1
slika1 = Image.open('Canon_40D.jpg')
slika1.load()
# Median 1
slika1_median = slika1.filter(ImageFilter.MedianFilter(size=3))
slika1_median.save("Cannon_40D_medain.jpg")
# stvaranje razlike slike 1
razlika1 = ImageChops.difference(slika1, slika1_median)
razlika1.save("Canon_40D_razlika.jpg")

# slika 2
slika2 = Image.open('Canon_DIGITAL_IXUS_400.jpg')
slika2.load()
# # Median 2
slika2_median = slika2.filter(ImageFilter.MedianFilter(size=3))
slika2_median.save("Canon_DIGITAL_IXUS_median.jpg")
# stvaranje razlike slike 2
razlika2 = ImageChops.difference(slika2, slika2_median)
razlika2.save("Canon_DIGITAL_IXUS_razlika.jpg")
