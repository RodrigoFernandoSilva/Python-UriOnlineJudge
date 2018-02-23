import math

line1 = input()
line2 = input()

x1, y1 = line1.split(" ")
x2, y2 = line2.split(" ")

x1 = float(x1)
y1 = float(y1)

x2 = float(x2)
y2 = float(y2)

distance = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
distance = math.sqrt(distance)

print("%0.4f" % distance)
