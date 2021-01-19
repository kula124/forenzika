import numpy as np
from PIL import Image


def equalise_g(image):
    image = image.convert("L")
    width, height = image.size
    totalPixels = width * height
    freq = [0] * 256  # fill
    cProbability = [0] * 256  # fill zeros

    freq = image.histogram()
    # HISTOGRAM EQUALIZATION
    prevSum = 0
    for i in range(256):
        prevSum += freq[i]*1.0/totalPixels  # add the probablity to calculate
        cProbability[i] = prevSum

    pixels = image.load()  # allows the image to be writable

    for x in range(width):
        for y in range(height):
            pixels[x, y] = int(255 * cProbability[pixels[x, y]])
    return image


def equalise_rgb(image):
    width, height = image.size
    totalPixels = width * height
    r, g, b = image.split()
    channels = [r, g, b]

    for c in channels:
        freq = [0] * 256  # fill
        cProbability = [0] * 256  # fill zeros
        freq = c.histogram()
        prevSum = 0
        for i in range(256):
            # add the probablity to calculate
            prevSum += freq[i]*1.0/totalPixels
            cProbability[i] = prevSum
        channel_pixles = c.load()  # allows the image to be writable

        for x in range(width):
            for y in range(height):
                channel_pixles[x, y] = int(
                    255 * cProbability[channel_pixles[x, y]])
    return Image.merge(image.mode, (r, g, b))


def amplify(image, factor=1):
    src = image.split()
    channels = list(src)
    w, h = image.size

    for c in channels:
        pixels = c.load()
        for x in range(w):
            for y in range(h):
                pixel = pixels[x, y]
                if ((pixel * factor) > 255):
                    pixels[x, y] = 255
                else:
                    pixels[x, y] = pixel * factor
    return Image.merge(image.mode, src)
