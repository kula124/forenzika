from PIL import Image
slika = Image.open("slika.jpg")
matrica_sa_pikselima = slika.load()
print("Prvi piksel: " + str(matrica_sa_pikselima[0, 0]))
matrica_sa_pikselima[0, 0] = (255, 255, 255)
print("Prvi piksel: " + str(matrica_sa_pikselima[0, 0]))
