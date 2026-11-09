****************************************
# správná odpověď:
print("Zadej 3 hodnoty:")
a = int(input("Zadej první hodnotu: "))
b = int(input("Zadej druhou hodnotu: "))
c = int(input("Zadej třetí hodnotu: "))

max = a 
min = a

if b<min:
    min = b
elif b>max:
    max = b

if c<min:
    min = c 
elif c>max:
    max = c
print ("Nejmenší čísslo:", min, \nNejvětší číslo:", max)




