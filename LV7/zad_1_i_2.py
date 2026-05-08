import numpy as np  
from tensorflow import keras # type: ignore
from keras import layers  
from keras.models import Sequential
from keras.layers import Dense
from matplotlib import pyplot as plt 
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay  


(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# TODO: prikazi nekoliko slika iz train skupa
plt.figure(figsize=(12, 5), num='Slike iz train skupa')
for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f"\nBroj: {y_train[i]}")
plt.subplots_adjust(hspace= 0.5)
plt.show()

x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

x_train_s = x_train_s.reshape(60000, 784)
x_test_s = x_test_s.reshape(10000, 784)

y_train_s = keras.utils.to_categorical(y_train, 10)
y_test_s = keras.utils.to_categorical(y_test, 10)

# TODO: kreiraj mrezu pomocu keras.Sequential(); prikazi njenu strukturu pomocu .summary()
model = keras.Sequential([
    layers.Dense(100, activation='relu', input_shape=(784,)),
    layers.Dense(50, activation='relu'),
    layers.Dense(10, activation='softmax')
])
model.summary()

# TODO: definiraj karakteristike procesa ucenja pomocu .compile()
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# TODO: provedi treniranje mreze pomocu .fit()
fit = model.fit(x_train_s, y_train_s, epochs=3, batch_size=32)

# TODO: Izracunajte tocnost mreze na skupu podataka za ucenje i skupu podataka za testiranje
train_loss, train_accuracy = model.evaluate(x_train_s, y_train_s)
test_loss, test_accuracy = model.evaluate(x_test_s, y_test_s)

print(f"Trening Tocnost: {train_accuracy:.3f}")
print(f"Test Tocnost: {test_accuracy:.3f}")

# TODO: Prikazite matricu zabune na skupu podataka za testiranje
y_test_pred = model.predict(x_test_s)
y_test_pred_classes = np.argmax(y_test_pred, axis=1)
cm = confusion_matrix(y_test, y_test_pred_classes)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=range(10))
disp.plot(cmap=plt.cm.plasma)
plt.title("Matrica zabune")
plt.show()

# TODO: Prikazi nekoliko primjera iz testnog skupa podataka koje je izgrađena mreza pogresno klasificirala
pogresni_primjer = np.where(y_test != y_test_pred_classes)[0]
plt.figure(figsize=(12, 5), num='Primjera iz testnog skupa podataka koje je izgrađena mreza pogresno klasificirala')
for i in range(9):
    index = pogresni_primjer[i]
    plt.subplot(3, 3, i+1)
    plt.imshow(x_test[index], cmap='gray')
    plt.title(f"Istinito: {y_test[index]} \nPredvideno: {y_test_pred_classes[index]}")
plt.tight_layout()
plt.show()


'''
Potrebno je izgraditi potpuno povezanu unaprijednu višeslojnu neuronsku mrežu na temelju MNIST skupa podataka te 
izvršiti njenu evaluaciju.  U prilogu vježbe nalazi se skripta 7.1. koja učitava MNIST skup podataka. Dopunite skriptu na 
odgovarajućim mjestima: 
 
1) Prikažite nekoliko slika iz MNIST skupa podataka (pomoću matplotlib biblioteke). 
 
2) Izgradite potpuno povezanu neuronsku mrežu pomoću Keras API. Mreža treba imati strukturu danu slikom 7.1. 
https://keras.io/guides/sequential_model/ 
 
3) Izračunajte točnost izgrađene mreže na skupu podataka za učenje i skupu podataka za testiranje. 
 
4) Prikažite matricu zabune na skupu podataka za učenje i na skupu podataka za testiranje. Komentirajte dobivene 
rezultate. 

Zadatak 2 
 
Prikažite nekoliko nasumičnih primjera iz testnog skupa podataka koje je izgrađena mreža pogrešno klasificirala (napišite 
iznad slike koja je stvarna oznaka slike i oznaku koju je mreža procijenila).
'''