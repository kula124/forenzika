from PIL import Image
from PIL import ImageOps
slika = Image.open("slika.jpg")
stupci, retci = slika.size
# 1. na£in - specifikacija novog broja redaka i stupaca
smanjena_slika_1 = slika.resize((256, 256))
# 2. na£in - skaliranje (// - integer dijeljenje)
smanjena_slika_2 = slika.resize((stupci//2, retci//2))
smanjena_slika_1.save("out/smanjena_slika_1.jpg")
smanjena_slika_2.save("out/smanjena_slika_2.jpg")
