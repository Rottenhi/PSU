import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.transform import resize  # type: ignore
from skimage import color  # type: ignore
from tensorflow.keras import models  # type: ignore
import numpy as np

filename = 'test.png'

img_original = mpimg.imread('test.png')
img = color.rgb2gray(img_original)
img = resize(img, (28, 28))

# Prikazi sliku
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.axis('off')
plt.show()

# Pripremi sliku - ulaz u mrezu
img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')

# TODO: ucitaj izgradenu mrezu
model = models.load_model('best_model.h5')

# TODO: napravi predikciju za ucitanu sliku pomocu mreze
predictions = model.predict(img)
predicted_digit = np.argmax(predictions, axis=1)[0]

# TODO: ispis rezultat u terminal
print(f"Prepoznata znamenka: {predicted_digit}")
