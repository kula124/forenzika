from PIL import Image, ImageFilter

# creating a image object
slika = Image.open("slika.png")

# applying the Gaussian Blur filter
slika_gauss = slika.filter(ImageFilter.MedianFilter(size=9))

slika_gauss.save("median_filter.png")
