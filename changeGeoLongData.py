import piexif
from PIL import Image

slika = Image.open('geo.jpg')
exif_key_value = piexif.load(slika.info['exif'])

longitude = exif_key_value['GPS'][piexif.GPSIFD.GPSLongitude]

exif_key_value['GPS'][piexif.GPSIFD.GPSLongitude] = (
    (12, 1), (60, 1), (190000, 10000))

print(exif_key_value['GPS'][piexif.GPSIFD.GPSLongitude])
exif_bytes = piexif.dump(exif_key_value)

slika.save("changedGeoWorking.jpeg", exif=exif_bytes)
