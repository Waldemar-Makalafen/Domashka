#####Задача номер 2
#####
#####
listnw = []
listnw2 = []
a = int(input())
b = int(input())
c = int(input())
d = int(input())
listnw.append(a)
listnw.append(b)
listnw.append(c)
listnw.append(d)

def sortirovka(listnw):
	mim_znach = min(listnw)
	max_znach = max(listnw)
	kol_vo = len(listnw)
	print(min, max)
	listnw2.append(mim_znach)
	sred_znach_arif = a+b+c+d/kol_vo


	for x in listnw(1,4):
		if x > mim_znach and  x > sred_znach_arif and x > max_znach:
			listnw2.append(x)
		elif x > max_znach and x < sred_znach_arif:
			x.append(listnw2)

		listnw2.append(max_znach)
		print(listnw2)
		pass
	pass

sortirovka (listnw)

