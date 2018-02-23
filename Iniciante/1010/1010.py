linha1 = input()
linha2 = input()

codigo1, quantidade1, preco1 = linha1.split(" ")
codigo2, quantidade2, preco2 = linha2.split(" ")

total = (int(quantidade1) * float(preco1))
total += (int(quantidade2) * float(preco2))

print ("VALOR A PAGAR: R$ %0.2f" %total)
