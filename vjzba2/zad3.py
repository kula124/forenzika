from PIL import Image
slika = Image.open("slika.png")

w, h = slika.size

watermark = Image.open("custom_wm.jpg").resize((w, h))

skala = 0.3
Image.blend(slika, watermark, skala).save("custom_watermarked_image.png")
