from PIL import Image
from PIL.ExifTags import TAGS

metaData = {}
slika = Image.open("geo.jpg")
exifPodaci = slika._getexif()
if exifPodaci:
    for (tag, vrijednost) in exifPodaci.items():
        imeTaga = TAGS.get(tag, tag)
        metaData[imeTaga] = vrijednost
        print(imeTaga, vrijednost)
