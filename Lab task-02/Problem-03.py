a = (1,3,5,7,4)
print(len(a))
print(type(a))
print(a[-2], ",", a[2])

a=list(a)
a[-3]=50
a=tuple(a)
print(a)

print(a[2:4], ",",a[:-3])

a=list(a)
a.append(100)
print(a)
a.insert(2,200)
print(a)

a.pop(-1)
a.pop(1)
print(a)

n=[2,4,6]
a=a+n
print(a)

b=a.copy()
b.sort()
b=tuple(b)
print(b)