N = int(input())

horas = N % 3600
horas = int((N - horas) / 3600)
N -= horas * 3600

minutos = N % 60
minutos = int((N - minutos) / 60)
N -= int(minutos * 60)

print("%i:%i:%i" % (horas, minutos, N))
