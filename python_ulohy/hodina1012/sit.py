x1_oblast = 4
y1_oblast = 5
x2_oblast = 9
y2_oblast = 7

xb = int(input("Zadej souřadnici x bodu: "))
yb = int(input("Zadej souřadnici y bodu: "))

if xb > x1_oblast and xb < x2_oblast and yb > y1_oblast and yb < y2_oblast:
    print("Bod je uvnitř oblasti")
else:
    print("Bod je mimo oblast")

if (xb == x1_oblast or xb == x2_oblast) and (yb >= y1_oblast and yb <= y2_oblast):
    print("Bod je na levé nebo pravé horní nebo dolní hranici oblasti")
else:
    print("bod je mimo hranicei")

if (xb == x1_oblast or xb == x2_oblast) and (yb == y1_oblast or yb == y2_oblast):
    print("Bod je na rohu oblasti")
else: 
    print("bod je mimo roh oblasti")

