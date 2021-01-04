from PIL import Image
from PIL import ImageFilter

slika = Image.open("slika.jpg")
detektirani_rubovi = slika.filter(ImageFilter.FIND_EDGES)
zamucena_slika = slika.filter(ImageFilter.BLUR)
izostrena_slika = slika.filter(ImageFilter.SHARPEN)
detektirani_rubovi.save("out/detektirani_rubovi.jpg")
zamucena_slika.save("out/zamucena_slika.jpg")
izostrena_slika.save("out/izostrena_slika.jpg")
