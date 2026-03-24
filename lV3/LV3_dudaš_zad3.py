import urllib.request
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

url = 'https://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&polutant=5&tipPodatka=4&vrijemeOd=01.01.2017&vrijemeDo=31.12.2017'

try:
    airQualityHR = urllib.request.urlopen(url).read()
    root = ET.fromstring(airQualityHR)
except Exception as e:
    print(f"Greška pri dohvaćanju podataka: {e}")
    exit()

data_list = []

for child in root:
    try:
        mjerenje = float(child[0].text)
        vrijeme = child[2].text
        data_list.append({'mjerenje': mjerenje, 'vrijeme': vrijeme})
    except (IndexError, TypeError, ValueError):
        continue

df = pd.DataFrame(data_list)
df.vrijeme = pd.to_datetime(df.vrijeme, utc=True)


najvece_koncentracije = df.sort_values('mjerenje', ascending=False).head(3)

print("Tri datuma u 2017. godini s najvećom koncentracijom PM10 u Osijeku:")
for index, row in najvece_koncentracije.iterrows():
    print(f"Datum: {row['vrijeme'].strftime('%d.%m.%Y.')} - Koncentracija: {row['mjerenje']} µg/m3")

df.plot(y='mjerenje', x='vrijeme', title='Koncentracija PM10 Osijek 2017.')
plt.ylabel('PM10 (µg/m3)')
plt.show()