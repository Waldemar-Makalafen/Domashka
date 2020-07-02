import math


a = int(input('Введи а '))
b = int(input('Введи б '))
c = int(input('Введи с '))


d = b**2+4*a*c
d = math.sqrt(d)


print (d)
if d > 0:
	x1 = -b-d/2*a
	x2 = -b+d/2*a
print(x1,x2)
else:
 x = -b/2*a
print(x)










Chtoby_ne_vilitalo = input ()
