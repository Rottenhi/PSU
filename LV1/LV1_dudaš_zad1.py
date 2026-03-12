satiRada = input('Unesite broj radnih sati: ')
placaPoSatu = input('Unesite placu po radnom satu: ')

def total_euro(satiRada, placaPoSatu):
    total = float(satiRada) * float(placaPoSatu)
    return(total)


print("Radni sati: " + satiRada + " h")
print("eura/h: " + placaPoSatu)
print("Ukupno: " + str(total_euro(satiRada, placaPoSatu)) + " eura")
