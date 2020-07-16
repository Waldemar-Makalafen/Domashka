import math
chislo = float(input())

def m_okr(chislo):
	celoe = math.trunc(chislo)
	ostatok = chislo - celoe
	if ostatok >= 0.5000000000000000000000000000:
		nw_chislo = math.ceil(chislo)
		print(nw_chislo)
		
	else:
		nw_chislo = math.floor(chislo)
		print(nw_chislo)
	pass

m_okr (chislo)
