name = input('Введите ваше имя')
age = int(input('Введите ваш возраст'))

age = age - 18
if age > 0:
	if age <5:
		print (name, 'на',age, 'год/года старше 18')
	else:
		print (name, 'на',age, 'лет старше 18')
else:
	age = age*(-1)
	print (name, 'на',age, 'года/лет младше 18')
























Chtoby_ne_vilitalo = input ()