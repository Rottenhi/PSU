imeDatoteke = input("Unesite ime datoteke: ")

try:
    suma = 0
    brojac = 0
    datoteka = open(imeDatoteke)

    for data in datoteka:
        if data.startswith("X-DSPAM-Confidence:"):
            atpos = data.find(":")
            broj = float(data[atpos+1:].strip())

            suma += broj
            brojac += 1

    if brojac > 0:
        srednjaVrijednost = suma / brojac
        print("Average X-DSPAM-Confidence: ", srednjaVrijednost)
    else:
        print("Nema vrijednosti!")
except:
    print("Nema datoteke/pristup datoteci!")

datoteka.close()