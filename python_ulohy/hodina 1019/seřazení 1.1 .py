print("Zadej 3 hodnoty:")
a = int(input("Zadej první hodnotu: "))
b = int(input("Zadej druhou hodnotu: "))
c = int(input("Zadej třetí hodnotu: "))

max = a
min = a

if b >= max and c <= a:
    print ("Seřazení je: ", b, a, c)
elif c >= max and b <= a:
    print ("Seřazení je: ", c, a, b)
else:
    print ("Seřazení je: ", a, b, c)
