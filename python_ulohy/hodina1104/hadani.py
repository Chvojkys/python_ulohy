print("Mysli si číslo od 1 do 100")
print("Odpovídej následovně:")
print("  v - pokud je tvé číslo VĚTŠÍ než tip počítače")
print("  m - pokud je tvé číslo MENŠÍ než tip počítače")
print("  s - pokud je tip počítače SPRÁVNĚ")

dole = 1 
nahore = 100
pokusy = 0
Max_pokusy = 10
odpoved = ""
print(f"Hádej celé číslo od 1 do 100, máš {Max_pokusy} pokusů")


tip = 0
while tip != odpoved and pokusy <= Max_pokusy:
    tip = (nahore + dole) //2
pokusy +=1

print(f"Můj tip je: {tip}")
odpoved = input("Zadej odpověď (v / m / s): ")

if odpoved == "v":
    dole = tip +1
elif odpoved == "m":
    nahore = tip -1 
elif odpoved == "s":
    print(f"uhodl jsem to, pocet pokusů byl: {pokusy}")
else :
    print("Neplatná odpověď, zadej v, m nebo s")
    pokusy -= 1  



