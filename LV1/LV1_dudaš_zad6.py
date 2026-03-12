datoteka = open("SMSSpamCollection.txt")
hamRijeci = 0
hamPoruke = 0
spamRijeci = 0
spamPoruke = 0
usklicnik = 0


for data in datoteka:
    dijelovi = data.strip().split('\t')

    tip = dijelovi[0]
    poruka = dijelovi[1]

    rijeci = poruka.split()
    brojRijeci = len(rijeci)

    if tip == "ham":
        hamPoruke += 1
        hamRijeci += brojRijeci

    elif tip == "spam":
            spamPoruke += 1
            spamRijeci += brojRijeci

            if poruka.endswith("!"):
                usklicnik += 1

prosjekHamova = hamRijeci / hamPoruke
prosjekSpamova = spamRijeci / spamPoruke

print("Prosjecan broj rijeci u ham porukama: {:.2f} ".format(prosjekHamova))
print("Prosjecan broj rijeci u spam porukama: {:.2f}".format(prosjekSpamova))
print("Broj spam poruka koje zavrsavaju usklicnikom:", usklicnik)

datoteka.close()