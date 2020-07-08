list1 = []
list2 = []

a = int(input())
b = int(input())
d = int(input())
c = int(input())
e = int(input())
list1.append(int(a))
list1.append(int(b))
list1.append(int(d))
list1.append(int(c))
list1.append(int(e))
print(list1)


list2= list(set(list1))

print(list2)

#list1.append(int(a))
#list1.append(int(b))
#list1.append(int(d))
#list1.append(int(c))
#list1.append(int(e))