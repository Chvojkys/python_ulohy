# test čísla

cislo = float(input("Zadej číslo"))

if cislo>0:
    print("kladné")
else:
    if cislo<0:
        print("záporné")
        absolutni_hodnota = -cislo
    else:
        print("nula")


print(f"Absoltní hodnota: {cislo} je {absolutni_hodnota}")