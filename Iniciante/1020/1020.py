dias = int(input())

anos = dias % 365
anos = int((dias - anos) / 365)
dias -= (anos * 365)

meses = dias % 30
meses = int((dias - meses) / 30)
dias -= int((meses * 30))

print("%i ano(s)" % anos)
print("%i mes(es)" % meses)
print("%i dia(s)" % dias)
