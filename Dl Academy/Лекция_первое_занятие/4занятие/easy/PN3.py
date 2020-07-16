def _1_x_bet(bilet):
	num = int(bilet)
	lst1 = int(num[:1] + int(num[1:2]))
	lst2 = int(num[-1] + int(num[-2]))
	if lst1 == lst2:
		return True
	else:
		return False
	pass
	
bilet = 228228
_1_x_bet(bilet)
print(bilet)






