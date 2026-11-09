hodina = int(input("Zadej hodinu: "))

if hodina < 0:
    print("Hodina nemůže být záporná.")
elif hodina >= 24:
    print("Zadávejte platné hodiny, protože den má 24h né více")
elif 4 <= hodina <= 8:
    print("Dobré ráno")
elif 9 <= hodina <= 11:
    print("Dobré dopoledne")
elif hodina == 12:
    print("Dobré poledne")
elif 13 <= hodina <= 17:
    print("Dobré odpoledne")
elif 18 <= hodina <= 21:
    print("Dobrý večer")
else:
    print("Dobrá noc")
    