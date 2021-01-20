from PIL import Image, ImageFilter, ImageChops
import numpy as np

from helper import equalise_rgb, equalise_g, amplify, SeparableMedianFilter
from config import loadConfiguration, toBool, constructWrapper, shouldShowSave

config = loadConfiguration("config.ini")
wrapper = constructWrapper(config)
# Main
mainConfig = config["main"]
filterConfig = config["filter"]
showConfig = config["show"]

image = Image.open(mainConfig["image_name"])

image = wrapper(lambda: wrapper(lambda: equalise_g(
    image), 'filter.use_grayscale', lambda: equalise_rgb(image)), 'filter.equalise', '', False)

filteredImage = wrapper(
    lambda: SeparableMedianFilter(image, filterConfig["mask_size"]),
    'filter.use_separable',
    lambda: image.filter(
        ImageFilter.MedianFilter(int(filterConfig["mask_size"]))))

shouldShowSave(mainConfig, lambda x: filteredImage.save(x),
               'filtered_image_out')
shouldShowSave(showConfig, lambda x: filteredImage.show(x), 'filtered')

# Post filter
postConfig = config["post"]
noise = ImageChops.difference(image, filteredImage)
noise = amplify(noise, postConfig["amplify"])

shouldShowSave(showConfig, lambda x: noise.show(x), 'noise')

if (mainConfig["noise_out"]):
    noise.save(mainConfig["noise_out"])
if (toBool(postConfig["blend"])):
    out = Image.blend(image, noise, float(
        postConfig["blend_scale"]))
    shouldShowSave(postConfig, lambda x: out.save(x), "blend_out")
    shouldShowSave(showConfig, lambda x: out.show(x), 'blend')
