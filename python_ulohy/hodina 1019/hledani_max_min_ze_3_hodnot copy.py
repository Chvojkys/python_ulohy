print("Zadej 3 hodnoty:")
a = int(input("Zadej první hodnotu: "))
b = int(input("Zadej druhou hodnotu: "))
c = int(input("Zadej třetí hodnotu: "))

if  a >= b and a >= c:
    print("Maximum value:", a)
elif b >= a and b >= c:
    print("Maximum value:", b)
else:
    print("Maximum value:", c)

if  c <=a and c <= b:
    print("Minimum value:", c )
elif a <= b and a <= c:
    print("Minimum value:", a)
else:
    print("Minimum value:", b)


