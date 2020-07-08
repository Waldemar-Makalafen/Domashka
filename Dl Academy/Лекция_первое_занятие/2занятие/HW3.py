a = int(input())

m = a%10
a = a//10
while a > 0:
	if a%10 > m:
		m = a%10
		a = a//10
pass
print(m)



stop_vilit = input()