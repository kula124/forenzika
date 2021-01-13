from PIL import Image
slika = Image.open("slika.png")

w, h = slika.size

watermark = Image.open("watermark.png").resize((w, h))
skala = 0.1
Image.blend(slika, watermark, skala).save("watermarked_image.png")
