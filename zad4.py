from PIL import Image
slika = Image.open("slika.jpg")
R, G, B = slika.split()
R.save("out/crveni_kanal.jpg")
G.save("out/zeleni_kanal.jpg")
B.save("out/plavi_kanal.jpg")
