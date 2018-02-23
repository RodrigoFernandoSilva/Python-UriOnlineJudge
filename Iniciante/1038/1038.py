cardapio = {1: 4.0, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

line = input().split(" ")

cod, quan = line

cod = int(cod)
quan = int(quan)

print("Total: R$ %0.2f" % (cardapio[cod] * quan))
