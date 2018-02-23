import sys

n = float(input())

if n < 0 or n > 100:
    print("Fora de intervalo")
    sys.exit()

for line in range(4):
    if line == 0 and float(line) <= n <= ((line + 1) * 25):
        print("Intervalo [0,25]")
        break
    elif (line * 25) < n <= (line + 1) * 25:
        print("Intervalo (%i,%i]" % (line * 25, (line + 1) * 25))
        break
