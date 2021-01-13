# Lab 3

Metapodaci (engl. metadata) su dodatne informacije o digitalnoj slici koje slika može sadržavati uz podatke o boji piksela. Metapodaci obicno sadrže informacije o uređaju kojim je slika snimljena te o postavkama tog uredaja prilikom snimanja te slike

## Zadatak 1

Desnim klikom miša kliknite na proizvoljnu digitalnu sliku, odaberite Properties, pa zatim Details. Prikazati će vam se EXIF podaci odabrane slike. Što iz prikazanih podataka možete saznati o slici? Izbrišite EXIF podatke slike klikom na Remove Properties and Personal Information. Je li se veličina slike promijenila?

Slika:

<div align="center">
  <img src="./image.jpg" width="500"/>
</div>

Prije uklanjanja EXIF podataka:

<div align="center">
  <img src="./exif_data_of_image.jpg" width="500"/>
</div>

Nakon uklanjanja EXIF podataka:

- ne ispiše ništa :)

Iz prikazanih podataka (photo details) možemo saznati razne podatke kao što su:

- naslov slike, autora, tagove, datum
- dimenzije slike, tj. broj stupaca, redaka i kanala
- GPS koordinate na kojima je slika nastala
- ISO razina korištena prilikom snimanja slike
- informacija o tome je li blic bio korišten prilikom snimanja slike
- ime programa u kojemu je slika posljednji put obrađena
- koliki je bio otvor blende prilikom snimanja slike
- model lece fotoaparata korištenog za snimanje slike
- itd...

Nakon brisanja EXIF podataka dimenzije slike se nisu promijenile.

DOhvaćanje i ispisivanje EXIF informacija o slici u Pythonu:

```
from PIL import Image
from PIL.ExifTags import TAGS

metaData = {}
slika = Image.open("slika.jpg")
exifPodaci = slika._getexif()

if exifPodaci:
    for (tag, vrijednost) in exifPodaci.items():
        imeTaga = TAGS.get(tag, tag)
        metaData[imeTaga] = vrijednost
        print(imeTaga, vrijednost)

```

## Zadatak 2

Proučite JPEG File Interchange Format standard. Gdje su unutar JPEG datoteke zapisani metapodaci i kako im se može pristupiti?

- Metapodaci JPEG slike se nalaze u zaglavlju, kroz svojstva->detalji slike.

## Zadatak 3

Proučite strukturu EXIF zaglavlja RGB slike te ga ukratko opišite.

- Nekomprimirani RGB podaci snimaju se u skladu s osnovnim TIFF-om Rev. 6.0 RGB full-color img.

- Podaci o atributima bilježe se u oznakama, tagovima

- EXIF se snima pomoću privatnih oznaka rezerviranih u TIFF-u za ovaj standard

- Privatne oznake upućuju na skupove ovih podataka o atributima (Exif IDF)

- IDF vrijednost nije specificirana za File Header, 0th IFD, 0th IFD value, 1st IFD, 1st IFD value, 1st thumbnail image data, 0th primary image data

<div align="center">
  <img src="./EXIF_RGB_img.JPG" width="500"/>
</div>

## Zadatak 4

Učitajte sliku u boji u Pythonu i ispišite njezine GPS koordinate. GPS koordinate zatim promijenite u Pythonu, no pripazite na to da ostali metapodaci ostanu isti kao na ulaznoj slici.

Primjer dohvacanja i ispisivanja specifične EXIF informacije (u ovom slučaju informacije o aplikaciji kojom se je obrađivala slika):

```
from PIL import Image
from PIL.ExifTags import TAGS

metaData = {}
slika = Image.open("slika.jpg")
exifPodaci = slika._getexif()

# Ime svakog EXIF taga definirano je EXIF standardom
trazeniTag = 'Software'
flag = 0

for (i,j) in exifPodaci.iteritems():
    if TAGS.get(i) == trazeniTag:
        print("Trazimo: " + trazeniTag)
        print(j)
        flag = 1
if (flag == 0):
    print("Trazimo: " + trazeniTag)
    print ("Trazena vrijednost nije u EXIF podacima slike")
```

Just example:

```
import piexif
from PIL import Image

slika = Image.open('image.jpg')
exif_dict = piexif.load(slika.info['exif'])

longitude = exif_dict['GPS'][piexif.GPSIFD.GPSLongitude]
print(longitude)

exif_dict['GPS'][piexif.GPSIFD.GPSLongitude] = (
    (117, 1), (33, 1), (190555, 10000))

exif_bytes = piexif.dump(exif_dict)
piexif.insert(
    exif_bytes, 'D:/Users/Korisnik/Desktop/Python/forenzicka/lab3/image.jpg')
```
