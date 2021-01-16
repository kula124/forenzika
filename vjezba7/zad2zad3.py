from PIL import Image, ImageDraw, ImageFont
import numpy as np
from scipy.fftpack import dct, idct

slika = Image.open("mod.png")

if (slika.mode == "RGB"):
    print("Broj kanala: 3")
else:
    print("Broj kanala: 1")

slika_grayscale = slika.convert('L')
slika_matrix = np.asarray(slika_grayscale)

velicina_bloka = 40
stupci, retci = slika_grayscale.size
print("Broj stupaca: " + str(stupci))
print("Broj redaka: " + str(retci))

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

koeficijenti = np.zeros(shape=broj_vertikalnih_blokova *
                        broj_horizontalnih_blokova, dtype='f')
brojac = 0

for redak in range(broj_vertikalnih_blokova):
    trenutni_pocetni_stupac = 0
    trenutni_pocetni_redak = trenutni_pocetni_redak + velicina_bloka

    for stupac in range(broj_horizontalnih_blokova):
        temp_matrix = np.zeros(shape=(velicina_bloka, velicina_bloka))

        histogram = np.zeros(shape=256)

        trenutni_redak = 0

        for i in range(trenutni_pocetni_redak, trenutni_pocetni_redak + velicina_bloka):
            trenutni_stupac = 0
            trenutni_redak = 0

            for j in range(trenutni_pocetni_stupac, trenutni_pocetni_stupac + velicina_bloka):
                temp_matrix[trenutni_redak,
                            trenutni_stupac] = slika_matrix[i, j]
                trenutni_stupac = trenutni_stupac + 1
                trenutni_redak = trenutni_redak + 1

        #print("Trenutni blok: ")
        # print(temp_matrix)
       # print("\n")

        for i in range(0, velicina_bloka):
            for j in range(0, velicina_bloka):
                binary = bytearray('', 'utf-8')
                pixel = temp_matrix[i, j]

                if (i+1 < velicina_bloka):
                    if (pixel > temp_matrix[i+1, j]):
                        binary += b'1'
                    else:
                        binary += b'0'

                if (i+1 < velicina_bloka and j+1 < velicina_bloka):
                    if (pixel > temp_matrix[i+1, j+1]):
                        binary += b'1'
                    else:
                        binary += b'0'

                if (j+1 < velicina_bloka):
                    if (pixel > temp_matrix[i, j+1]):
                        binary += b'1'
                    else:
                        binary += b'0'

                if (i-1 > 0 and j+1 < velicina_bloka):
                    if (pixel > temp_matrix[i-1, j+1]):
                        binary += b'1'
                    else:
                        binary += b'0'

                if (i-1 > 0):
                    if (pixel > temp_matrix[i-1, j]):
                        binary += b'1'
                    else:
                        binary += b'0'

                if (i-1 > 0 and j-1 > 0):
                    if (pixel > temp_matrix[i-1, j-1]):
                        binary += b'1'
                    else:
                        binary += b'0'

                if (j-1 > 0):
                    if (pixel > temp_matrix[i, j-1]):
                        binary += b'1'
                    else:
                        binary += b'0'

                if (i+1 < velicina_bloka and j-1 > 0):
                    if (pixel > temp_matrix[i+1, j-1]):
                        binary += b'1'
                    else:
                        binary += b'0'

                binaryString = binary.decode("utf-8")
                newPixel = int(binaryString, 2)

               # print(newPixel)

        trenutni_pocetni_stupac = trenutni_pocetni_stupac + velicina_bloka

        koeficijenti[brojac] = temp_matrix[0, 0]
        brojac = brojac + 1

print(koeficijenti)

for i in range(0, koeficijenti.size):
    for j in range(i+1, koeficijenti.size):
        if (abs(koeficijenti[i] - koeficijenti[j]) < 1000):
            print("---Blokovi " + str(i+1) + " i " + str(j+1) + " su slicni!")

print("Kraj programa!\n")
