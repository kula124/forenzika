from PIL import Image
slika = Image.open("slika.jpg")
stupci, retci = slika.size

matrix = slika.load()

counter = 0

for x in range(stupci):
    for y in range(retci):
        if((matrix[x, y][0] + matrix[x, y][1] + matrix[x, y][2]) > 300):
            matrix[x, y] = (255, 255, 255)
            counter += 1

print(counter)
slika.save('out/save.jpg')
