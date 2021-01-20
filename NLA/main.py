from PIL import Image, ImageFilter, ImageChops
import numpy as np

from helper import equalise_rgb, equalise_g, amplify, SeparableMedianFilter
from config import loadConfiguration, toBool

config = loadConfiguration("config.ini")

# Main
mainConfig = config["main"]
image = Image.open(mainConfig["image_name"])

# Filtering
filterConfig = config["filter"]
if (toBool(filterConfig["equalise"])):
    if(toBool(filterConfig["use_grayscale"])):
        image = equalise_g(image)
    else:
        image = equalise_rgb(image)

filteredImage = ""
if (toBool(filterConfig["use_separable"])):
    filteredImage = SeparableMedianFilter(image, filterConfig["mask_size"])
else:
    filteredImage = image.filter(
        ImageFilter.MedianFilter(int(filterConfig["mask_size"])))

if (mainConfig["filtered_image_out"]):
    filteredImage.save(mainConfig["filtered_image_out"])
filteredImage.show()

# Post filter
postConfig = config["post"]
noise = ImageChops.difference(image, filteredImage)
noise = amplify(noise, postConfig["amplify"])

noise.show()
if (mainConfig["noise_out"]):
    noise.save(mainConfig["noise_out"])
if (toBool(postConfig["blend"])):
    out = Image.blend(image, noise, float(
        postConfig["blend_scale"])).save(postConfig["blend_out"])
