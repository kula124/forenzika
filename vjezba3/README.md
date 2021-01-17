# Lab 3

Metapodaci (engl. metadata) su dodatne informacije o digitalnoj slici koje slika može sadržavati uz podatke o boji piksela. Metapodaci obično sadrže informacije o uređaju kojim je slika snimljena te o postavkama tog uredaja prilikom snimanja te slike.

## Zadatak 1

Brisanjem EXIF-a veličina slike se neznatno promjenila.

Iz prikazanih podataka (photo details) možemo saznati razne podatke kao što su:

- naslov slike, autora, tagove, datum
- dimenzije slike, tj. broj stupaca, redaka i kanala
- GPS koordinate na kojima je slika nastala
- ISO razina korištena prilikom snimanja slike
- informacija o tome je li blic bio korišten prilikom snimanja slike
- ime programa u kojemu je slika posljednji put obrađena
- koliki je bio otvor blende prilikom snimanja slike
- model leće fotoaparata korištenog za snimanje slike

## Zadatak 2

Metapodatci se nalaze u zaglavlju. Može im se pristupiti iz file explorera na Windowsu pod "Properties" stavkom

## Zadatak 3

Struktura EXIF zaglavlja RGB slike:

- EXIF se snima pomoću privatnih oznaka rezerviranih u TIFF-u za ovaj standard
- Nekomprimirani RGB podaci snimaju se u skladu s osnovnim TIFF-om Rev. 6.0 RGB full-color img.
- Podaci o atributima bilježe se u oznakama, tagovima
- Privatne oznake upućuju na skupove ovih podataka o atributima (Exif IDF)
- IDF vrijednost nije specificirana za File Header, 0th IFD, 0th IFD value, 1st IFD, 1st IFD value, 1st thumbnail image data, 0th primary image data