from PIL import Image
from PIL import ImageOps

slika = Image.open("slika.jpg")
siva_slika = ImageOps.grayscale(slika)
siva_slika.save("out/siva_slika.jpg")
