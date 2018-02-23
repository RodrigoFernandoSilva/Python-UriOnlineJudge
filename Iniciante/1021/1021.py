N = input()

nota, moeda = N.split(".")

nota = int(nota)
moeda = int(moeda)

nota100 = nota % 100
nota100 = int((nota - nota100) / 100)
nota -= nota100 * 100

nota50 = nota % 50
nota50 = int((nota - nota50) / 50)
nota -= nota50 * 50

nota20 = nota % 20
nota20 = int((nota - nota20) / 20)
nota -= nota20 * 20

nota10 = nota % 10
nota10 = int((nota - nota10) / 10)
nota -= nota10 * 10

nota5 = nota % 5
nota5 = int((nota - nota5) / 5)
nota -= nota5 * 5

nota2 = nota % 2
nota2 = int((nota - nota2) / 2)
nota -= nota2 * 2

print("NOTAS:")
print("%i nota(s) de R$ 100.00" % nota100)
print("%i nota(s) de R$ 50.00" % nota50)
print("%i nota(s) de R$ 20.00" % nota20)
print("%i nota(s) de R$ 10.00" % nota10)
print("%i nota(s) de R$ 5.00" % nota5)
print("%i nota(s) de R$ 2.00" % nota2)

moeda1 = int(nota)

moeda50 = moeda % 50
moeda50 = int((moeda - moeda50) / 50)
moeda -= moeda50 * 50

moeda25 = moeda % 25
moeda25 = int((moeda - moeda25) / 25)
moeda -= moeda25 * 25

moeda10 = moeda % 10
moeda10 = int((moeda - moeda10) / 10)
moeda -= moeda10 * 10

moeda05 = moeda % 5
moeda05 = int((moeda - moeda05) / 5)
moeda -= moeda05 * 5

moeda01 = int(moeda)

print("MOEDAS:")
print("%i moeda(s) de R$ 1.00" % moeda1)
print("%i moeda(s) de R$ 0.50" % moeda50)
print("%i moeda(s) de R$ 0.25" % moeda25)
print("%i moeda(s) de R$ 0.10" % moeda10)
print("%i moeda(s) de R$ 0.05" % moeda05)
print("%i moeda(s) de R$ 0.01" % moeda01)
