x1 = input('чётные или не ?')

chet = [0 ,2 ,4 ,6 ,8 ,10 ,12 ,14 ,16 ,18 ,20 ]
nechet = [1 ,3 ,5 ,7 ,9 ,11 ,13, 15 ,17 ,19 ]
n = 0
list (chet)
list (nechet)
while n == 0:
	if x1 == "чётные" or "чёт":
		print (chet)
		exit = input("exit ?")
		if exit == "no":
			x1 = input('чётные или не ?')
		else:
			break
	elif x1 == "не" or "нечётные" :
		print(nechet)
		exit = input("exit ?")
		if exit == "no":
			x1 = input('чётные или не ?')
		else:
			break
	else:
		print("Я не понял")
		break
	pass




stop_vilit = input()