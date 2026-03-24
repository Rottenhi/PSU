import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('mtcars.csv')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(18, 10))

cilindri = np.unique(df.cyl.values)
meanMPG = [np.mean(df.mpg.values[df.cyl.values == c]) for c in cilindri]

ax1.bar(cilindri.astype(str), meanMPG, color=['lightblue'], edgecolor='black')
ax1.set_title('Mean MPG po cilindrima')
ax1.set_xlabel('Broj cilindara')
ax1.set_ylabel('MPG')

wt = [df.wt.values[df.cyl.values == c] for c in cilindri]

ax2.boxplot(wt, tick_labels=[f"{c} cil" for c in cilindri], patch_artist=True, boxprops=dict(facecolor='lightblue', color='black'), medianprops=dict(color='red'))
ax2.set_title('Wt po cilindrima')
ax2.set_xlabel('Broj cilindara')
ax2.set_ylabel('Tezina lbs u tisucama lbs')

automatski = df.mpg.values[df.am.values == 0]
rucni = df.mpg.values[df.am.values == 1]

ax3.boxplot([automatski, rucni], tick_labels=['Automatski (0)', 'Rucni (1)'], patch_artist=True, boxprops=dict(facecolor='lightblue', color='black'), medianprops=dict(color='red'))
ax3.set_title('Automatski i rucni mjenjaci')
ax3.set_ylabel('MPG')

hp = df.hp.values
akceleration = df.qsec.values * 0.25
am = df.am.values

ax4.scatter(hp[am == 0], akceleration[am == 0], c='red', label='Automatski', marker = 'o', s = 50, alpha = 0.7)
ax4.scatter(hp[am == 1], akceleration[am == 1], c='blue', label='Rucni', marker = 'o', s = 50, alpha = 0.7)

ax4.set_title('Snage : ubrzanje')
ax4.set_xlabel('HP')
ax4.set_ylabel('Vrijeme u sekundama')
ax4.legend()

plt.tight_layout()
plt.show()
