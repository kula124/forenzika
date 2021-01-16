from PIL import Image, ImageDraw, ImageFont
import numpy as np
from scipy.fftpack import dct, idct

# instalirati potrebne biblioteke - pip install scipy

# da vam donji kod idealno radi (tj. da vam donji broj blokova slike odgovara cijeloj slici), mozete koristiti sliku dimenzija 321 retka, 481 stupca - ovakve slike mozete pronaci na Berkeley Image Database

# program pokrenite sa python3 dct.py

slika = Image.open("slika.png")

stupci, retci = slika.size
print("Broj stupaca: " + str(stupci))
print("Broj redaka: " + str(retci))
if (slika.mode == "RGB"):
    print("Broj kanala: 3")
else:
    print("Broj kanala: 1")

slika_grayscale = slika.convert('L')
slika_matrix = np.asarray(slika_grayscale)

velicina_bloka = 40

broj_horizontalnih_blokova = stupci // velicina_bloka
broj_vertikalnih_blokova = retci // velicina_bloka

broj_trenutnog_bloka = 1

# dijelimo sliku na blokove i svakom bloku dodijelimo broj
for i in range(0, broj_vertikalnih_blokova):
    for j in range(0, broj_horizontalnih_blokova):
        draw = ImageDraw.Draw(slika)
        draw.rectangle(((j*velicina_bloka, i*velicina_bloka),
                        (j*velicina_bloka+velicina_bloka, i*velicina_bloka+velicina_bloka)))
        broj_trenutnog_bloka_1 = str(broj_trenutnog_bloka)
        draw.text((j*velicina_bloka, i*velicina_bloka), broj_trenutnog_bloka_1)
        broj_trenutnog_bloka = broj_trenutnog_bloka + 1

slika.show()

trenutni_pocetni_stupac = 0
trenutni_pocetni_redak = -velicina_bloka

# kreiramo prazni niz u kojega cemo staviti po jednu DCT frekvenciju svakog bloka slike
frekvencije = [0] * (broj_horizontalnih_blokova * broj_vertikalnih_blokova)
frekvencije2 = [0] * (broj_horizontalnih_blokova * broj_vertikalnih_blokova)
frekvencije3 = [0] * (broj_horizontalnih_blokova * broj_vertikalnih_blokova)
brojac_frekvencija = 0
# print(frekvencije)


for redak in range(broj_vertikalnih_blokova):
    trenutni_pocetni_stupac = 0
    trenutni_pocetni_redak = trenutni_pocetni_redak + velicina_bloka

    for stupac in range(broj_horizontalnih_blokova):
        temp_matrix = np.zeros(shape=(velicina_bloka, velicina_bloka))
        temp_matrix_dct = np.zeros(shape=(velicina_bloka, velicina_bloka))
        trenutni_redak = 0

        for i in range(trenutni_pocetni_redak, trenutni_pocetni_redak + velicina_bloka):
            trenutni_stupac = 0
            trenutni_redak = 0

            for j in range(trenutni_pocetni_stupac, trenutni_pocetni_stupac + velicina_bloka):
                temp_matrix[trenutni_redak,
                            trenutni_stupac] = slika_matrix[i, j]
                trenutni_stupac = trenutni_stupac + 1
                trenutni_redak = trenutni_redak + 1

        print("Trenutni blok: ")
        print(temp_matrix)
        print("\n")

        temp_matrix_dct = dct(dct(temp_matrix.T).T)

        print("DCT matrica za trenutni blok:")
        print(temp_matrix_dct)
        print("\n")

        # gornju lijevu frekvenciju zapisujemo u niz frekvencije
        # frekvenciju na indeksu [1,1] zapisujemo u frekvencije2
        # frekvenciju na indeksu [2,2] zapisujemo u frekvencije3
        frekvencije[brojac_frekvencija] = temp_matrix_dct[0, 0]
        frekvencije2[brojac_frekvencija] = temp_matrix_dct[1, 1]
        frekvencije3[brojac_frekvencija] = temp_matrix_dct[2, 2]
        brojac_frekvencija = brojac_frekvencija + 1

        trenutni_pocetni_stupac = trenutni_pocetni_stupac + velicina_bloka

# ispisujemo najvaznije frekvencije svakog bloka slike
# print(frekvencije)
for i in range(0, broj_horizontalnih_blokova * broj_vertikalnih_blokova):
    print("Blok " + str(i+1) + ": (1) " + str(frekvencije[i]) + " (2) " + str(
        frekvencije2[i]) + " (3) " + str(frekvencije3[i]))

print("Kraj programa!\n")
