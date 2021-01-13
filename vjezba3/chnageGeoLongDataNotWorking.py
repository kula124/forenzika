import piexif
from PIL import Image
from PIL.ExifTags import TAGS
import PIL.ExifTags as ExifTags

metaData = {}
gpsinfo = {}

slika = Image.open("changedGeo.jpg")
exifPodaci = slika._getexif()
if exifPodaci:
    for (tag, vrijednost) in exifPodaci.items():
        imeTaga = TAGS.get(tag, tag)
        metaData[imeTaga] = vrijednost
        print(imeTaga, vrijednost)

for key in metaData['GPSInfo'].keys():
    decode = ExifTags.GPSTAGS.get(key, key)
    gpsinfo[decode] = metaData['GPSInfo'][key]
# print(gpsinfo)

print("Zapis dan u obliku: (stupnjevi, minute, sekunde)")
tagToFInd = "GPSLongitude"

print(tagToFInd)
print(gpsinfo[tagToFInd])

gpsinfo[tagToFInd] = (11.0, 60, 7)
metaData["GPSInfo"] = gpsinfo

slika.save("ChangedGeo.jpg", exif=piexif.dump(metaData))
