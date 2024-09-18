a = {1, 3, 5, 8, 3, 7}
b = {0, False, 1, 5}


print("Length of a: ",len(a))
print("Type of a: ", type(a))

a.add(10)
print("Adding 10 in Set a: ", a)

a.remove(8)
print("Removing 8 from Set a: ", a)

print("After Union :", a | b)
print("After Intersection: ", a & b)
print("Difference of a and b: ", a - b)

for x in a :
    if x==5 :
        break
    print(x)

print(a.union("After Joining: ",set([2,3,4])))

if 3 in a :
    print("3 is present")