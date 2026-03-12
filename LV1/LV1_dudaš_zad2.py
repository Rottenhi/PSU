aktivno = True

def ocjenjivanje(ocjena):
    if ocjena >= 0.9:
        print("Ocjena: A")
    elif ocjena >= 0.8:
        print("Ocjena: B")
    elif ocjena >= 0.7:
        print("Ocjena: C")
    elif ocjena >= 0.6:
        print("Ocjena: C")
    else:
        print("Ocjena: F")

while aktivno:
    try:
        ocjena = float(input('Unesite broj izmedju 0.0 i 1.0: '))
        if ocjena > 1.0 or ocjena < 0.0:
            print("Unesen je broj ivan granica!")
        else:
            aktivno = False
            ocjenjivanje(ocjena)
    except:
        print("Greska, nije unesen broj!")

