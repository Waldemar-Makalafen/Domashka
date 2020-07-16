lst = []

a = int(input())
b = int(input())
c = int(input())
d = int(input())
lst.append(a)
lst.append(b)
lst.append(c)
lst.append(d)


lst1 = [x for x in lst if x >= 0 and x%4 and not x%3]

print(lst1)


