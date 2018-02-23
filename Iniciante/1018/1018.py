valor = int(input())

nota100 = valor % 100
nota100 = int((valor - nota100) / 100)
valor -= nota100 * 100

nota50 = valor % 50
nota50 = int((valor - nota50) / 50)
valor -= nota50 * 50

nota20 = valor % 20
nota20 = int((valor - nota20) / 20)
valor -= nota20 * 20

nota10 = valor % 10
nota10 = int((valor - nota10) / 10)
valor -= nota10 * 10

nota5 = valor % 5
nota5 = int((valor - nota5) / 5)
valor -= nota5 * 5

nota2 = valor % 2
nota2 = int((valor - nota2) / 2)
valor -= int(nota2 * 2)

print((nota100 * 100) + (nota50 * 50) + (nota20 * 20) + (nota10 * 10) + (nota5 * 5) + (nota2 * 2) + valor)
print('%d nota(s) de R$ 100,00' % nota100)
print('%d nota(s) de R$ 50,00' % nota50)
print('%d nota(s) de R$ 20,00' % nota20)
print('%d nota(s) de R$ 10,00' % nota10)
print('%d nota(s) de R$ 5,00' % nota5)
print('%d nota(s) de R$ 2,00' % nota2)
print('%d nota(s) de R$ 1,00' % valor)
