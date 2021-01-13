import sys
from PIL import Image

# koristite lossless format slike, npr. png - nemojte koristiti jpg
# slika_1 i slika_2 moraju biti istih dimenzija
slika_1 = ""
slika_2 = ""
bitCount = 2
channel_count = 0
argc = len(sys.argv)

if (argc == 1):
    slika_1 = Image.open("envelope.png")
    w, h = slika_1.size
    slika_2 = Image.open("target.png").resize((w, h))
elif (argc == 2):
    bitCount = sys.argv[1]
    slika_1 = Image.open("envelope.png")
    w, h = slika_1.size
    slika_2 = Image.open("target.png").resize((w, h))
elif (argc == 4):
    slika_1 = Image.open(sys.argv[1])
    w, h = slika_1.size
    slika_2 = Image.open(sys.argv[2]).resize((w, h))
    bitCount = int(sys.argv[3])

stupci, retci = slika_1.size
print("Broj stupaca: " + str(stupci))
print("Broj redaka: " + str(retci))
if (slika_1.mode == "RGB"):
    print("Broj kanala: 3")
    channel_count = 3
else:
    print("Broj kanala: 1")
    channel_count = 1
    exit("Not supported")

matrica_sa_pikselima_1 = slika_1.load()
matrica_sa_pikselima_2 = slika_2.load()

# print(matrica_sa_pikselima_1[stupci-1,retci-1])

for i in range(0, stupci):
    for j in range(0, retci):
        r = matrica_sa_pikselima_1[i, j][0]
        g = matrica_sa_pikselima_1[i, j][1]
        b = matrica_sa_pikselima_1[i, j][2]

        r_binary = format(r, '#010b').replace("0b", "")
        g_binary = format(g, '#010b').replace("0b", "")
        b_binary = format(b, '#010b').replace("0b", "")

        r2 = matrica_sa_pikselima_2[i, j][0]
        g2 = matrica_sa_pikselima_2[i, j][1]
        b2 = matrica_sa_pikselima_2[i, j][2]

        r_binary2 = format(r2, '#010b').replace("0b", "")
        g_binary2 = format(g2, '#010b').replace("0b", "")
        b_binary2 = format(b2, '#010b').replace("0b", "")

        # steganografija
        novi_r_binary = [0, 0, 0, 0, 0, 0, 0, 0]
        novi_g_binary = [0, 0, 0, 0, 0, 0, 0, 0]
        novi_b_binary = [0, 0, 0, 0, 0, 0, 0, 0]
        for k in range(8 - bitCount):
            novi_r_binary[k] = int(r_binary[k])
        for g in range(8 - bitCount, 8, 1):
            novi_r_binary[k] = int(r_binary2[g])

        for k in range(8 - bitCount):
            novi_g_binary[k] = int(g_binary[k])
        for g in range(8 - bitCount, 8, 1):
            novi_g_binary[k] = int(g_binary2[g])

        for k in range(8 - bitCount):
            novi_b_binary[k] = int(b_binary[k])
        for g in range(8 - bitCount, 8, 1):
            novi_b_binary[k] = int(b_binary2[g])

        novi_r_int = int("".join(map(str, novi_r_binary)), 2)
        novi_g_int = int("".join(map(str, novi_g_binary)), 2)
        novi_b_int = int("".join(map(str, novi_b_binary)), 2)

        matrica_sa_pikselima_1[i, j] = (novi_r_int, novi_g_int, novi_b_int)
# sacuvamo novu sliku
slika_1.save("skrivena_slika.png")
