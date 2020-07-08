import math
list1 = []

a = int(input())
b = int(input())
d = int(input())
c = int(input())
########################################### В список
list1.append(int(a))
list1.append(int(b))
list1.append(int(d))
list1.append(int(c))

#list1 = [2, -5, 8, 9, -25, 25, 4]
list2 = []



print (list1)
for a in list1:
	#a = math.sqrt(a)  a.append(list2)
	if a >= 0:
		a = math.sqrt(a)
		if a > 0 and a% 1 ==0:
			list2.append(int(a))
	print (list2)
	pass



