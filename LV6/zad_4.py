import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from sklearn import cluster
import numpy as np


image = mpimg.imread('example_grayscale.png')
if len(image.shape) == 3:
    image = np.mean(image, axis=2)

X = image.reshape((-1, 1))
k_means = cluster.KMeans(n_clusters=5, n_init=10)
k_means.fit(X)
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
image_compressed = np.choose(labels, values)
image_compressed.shape = image.shape

plt.figure("Gray")
plt.imshow(image,  cmap='gray')
plt.show()

plt.figure("Gray compressed")
plt.imshow(image_compressed,  cmap='gray')
plt.show()

'''
Primijenite scikit-learn kmeans metodu za kvantizaciju boje na slici. Proučite kod 6.2. iz priloga vježbe te ga primijenite 
za kvantizaciju boje na slici example_grayscale.png koja dolazi kao prilog ovoj vježbi. Mijenjajte broj klastera. 
Što primjećujete? Izračunajte kolika se kompresija ove slike može postići ako se koristi 10 klastera. 
Pomoću sljedećeg koda možete učitati sliku: 
 
import matplotlib.image as mpimg 
 
imageNew = mpimg.imread('example_grayscale.png') 
'''