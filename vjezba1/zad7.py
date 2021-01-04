from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

slika = Image.open("slika.png")
slika_grayscale = slika.convert('L')
slika_matrix = np.asarray(slika_grayscale)

plt.hist(slika_matrix.flatten())
plt.xlabel('Intenzitet')
plt.ylabel('Broj piksela')
plt.show()
