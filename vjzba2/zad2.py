from PIL import Image
from PIL import ImageChops
from PIL import ImageEnhance

slika = Image.open("watermarked_image.png")

watermark = Image.open("slika.png")

razlika = ImageChops.difference(slika, watermark)
razlika.save("razlika.png")
# Poja£ajmo razliku da bude vidljivija
pojacana_razlika = ImageEnhance.Contrast(razlika)
skala = 7
pojacana_razlika_slika = pojacana_razlika.enhance(skala)
pojacana_razlika_slika.save("pojacana_razlika.png")
