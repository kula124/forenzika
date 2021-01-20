import numpy as np
from PIL import Image
import math as Math


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


def _findQuick3x3Median(tuple3):
    a, b, c = tuple3
    mx = max(max(a, b), c)
    mi = min(min(a, b), c)
    return a ^ b ^ c ^ mx ^ mi


def _getSubArray(pixels, x, y, dim_size, dim):
    res = []
    if (dim == "w"):
        res.append(pixels[x, y])
        res.append(pixels[x + 1, y] if x + 1 < dim_size else 0)
        res.append(pixels[x + 2, y] if x + 2 < dim_size else 0)
    elif (dim == "h"):
        res.append(pixels[x, y])
        res.append(pixels[x, y + 1] if y + 1 < dim_size else 0)
        res.append(pixels[x, y + 2] if y + 2 < dim_size else 0)
    return res


def SeparableMedianFilter(image, size):
    if (size != 3 and size != 9):
        raise "Bad size param! Must be 3 or 9"
    if (size == 9):
        raise "Size 9 not implemented (yet)! Use 3"
    w, h = image.size
    src = image.split()
    channels = list(src)

    for c in channels:
        pixles = c.load()
        for x in range(w):
            for y in range(h):
                pixles[x, y] = _findQuick3x3Median(
                    _getSubArray(pixles, x, y, w, "w"))
    halfImage = Image.merge(image.mode, src)

    src = halfImage.split()
    channels = list(src)
    for c in channels:
        pixles = c.load()
        for y in range(h):
            for x in range(w):
                pixles[x, y] = _findQuick3x3Median(
                    _getSubArray(pixles, x, y, h, "h"))
    return Image.merge(halfImage.mode, src)
