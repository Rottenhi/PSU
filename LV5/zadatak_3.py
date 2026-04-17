import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, precision_score, recall_score, accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier, plot_tree

df = pd.read_csv('occupancy_processed.csv')

feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

x_train, x_test, y_train, y_test = train_test_split(X,y, stratify=y)
scaler = StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.fit_transform(x_test)

dt = DecisionTreeClassifier()
dt.fit(x_train ,y_train)
y_pred = dt.predict(x_test)

plt.figure(figsize=(12, 8))
plot_tree(dt, filled=True)
plt.show()

matrix = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=matrix, display_labels=['Free', 'Occupied'])
disp.plot(cmap=plt.cm.Reds)
plt.title('Confusion matrix')
plt.show()

accuracy = accuracy_score(y_test, y_pred)
print("Točnost modela:", accuracy)

precision = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

print(f"Preciznost: {precision:.3f}")

print(f"Odziv: {recall:.3f}")

print("Izvještaj klasifikacije:\n", classification_report(y_test, y_pred, target_names=['Slobodna', 'Zauzeta']))

"""
Umjesto algoritma K najbližih susjeda koristite stablo odlučivanja te ponovite korake a) do d) iz prethodnog zadatka.
a) Vizualizirajte dobiveno stablo odlučivanja.
b) Što se događa s rezultatima ako mijenjate parametar max-depth stabla odlučivanja?
c) Što se događa s rezultatima ako ne koristite skaliranje ulaznih veličina?
d) Evaluirajte izgrađeni klasifikator na testnom skupu podataka:
a. prikažite matricu zabune
b. izračunajte točnost klasifikacije
c. izračunajte preciznost i odziv po klasama
"""