lstBrojevi = []

while True:
    unos = input("Unesite broj ili  'Done' za kraj: ")

    if unos == "Done":
        break

    try:
        broj = float(unos)
        lstBrojevi.append(broj) 
    except:
        print("Nije unesen broj!")

if len(lstBrojevi) == 0:
    print("lista je prazna/ne sadrzi niti jedan broj")
else:
    print("Broj unesenih brojeva: ", len(lstBrojevi))

    srednjaVrijednost = sum(lstBrojevi) / len(lstBrojevi)
    print("Srednja vrijednost je :", srednjaVrijednost)
    print("Minimalna vrijednost je: ", min(lstBrojevi))
    print("Maksimalna vrijednost je: ", max(lstBrojevi))

    lstBrojevi.sort()
    print("Sortirani: ", lstBrojevi)
