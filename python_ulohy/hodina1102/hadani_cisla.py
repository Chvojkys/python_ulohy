import random
tajne_cislo = random.randint(1, 20)
print("Hádání čísla mezi 1 a 20")
pokusy = 0
Max_pokusy = 5

print(f"Hádej celé číslo od 1 do 20, máš {Max_pokusy} pokusů")

tip = 0
while tip != tajne_cislo and pokusy <= Max_pokusy:
    tip = int(input("Zadej tip: "))
    if tip <= 1 or tip >= 20:
        print("Zadej číslo mezi 1 a 20") 
        continue   
    pokusy += 1
    if tip < tajne_cislo:
        print("Tajné číslo je větší")
    elif tip > tajne_cislo:
        print("Tajné číslo je menší")
 
if tip == tajne_cislo:
    print(f"Gratulace! Uhodl jsi číslo {tajne_cislo} na {pokusy}. pokus")
else:
    print(f"Prohrál jsi! Tajné číslo bylo {tajne_cislo}")
