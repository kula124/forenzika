from PIL import Image
from PIL.ExifTags import TAGS
import piexif
# Može ih biti više
keywords = ["Photoshop", "Gimp", "Paint"]

metaData = {}
slika = Image.open("slika.jpg")

exif_key_value = piexif.load(slika.info['exif'])
software = exif_key_value["0th"][305].decode('utf')
print(software)

for kw in keywords:
    if (kw.lower() in software.lower()):
        print(f"Image manipulation sofware detected: {kw}")
        exif_key_value["0th"][305] = ""

slika.save("manip.jpg", exif=piexif.dump(exif_key_value))

#### TESTING ####

test_s = Image.open("manip.jpg")
exif_key_value = piexif.load(test_s.info['exif'])
software = exif_key_value["0th"][305].decode('utf')
failed = 0

for kw in keywords:
    if (kw.lower() in software.lower()):
        print(f"Test failed! Manipulation sofware detected: {kw}")
        failed = 1
if not failed:
    print("Manipulation software signature removed successfully!")
