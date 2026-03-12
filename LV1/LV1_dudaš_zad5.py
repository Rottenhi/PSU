datoteka = open("song.txt")

rjecnik = {} #dodati vrijednosti

for data in datoteka:
    rijeci = data.split()
    
    for rijec in rijeci:
        if rijec in rjecnik:
            rjecnik[rijec] += 1
        else:
            rjecnik[rijec] = 1
datoteka.close()

ponavljanjeRijeciJednom = 0

print("Rijeci koje se pojavljuju samo jednom:")

for rijec, broj in rjecnik.items():
    if broj == 1:
        print(rijec)
        ponavljanjeRijeciJednom += 1

print("Ukupno takvih rijeci:", ponavljanjeRijeciJednom)