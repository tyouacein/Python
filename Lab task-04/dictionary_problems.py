emp = {
    "name" : "A",
    "age" : 40,
    "type" : {"developer" : ["ios", "android"]},
    "Parmanent" : True,
    "Salary" : 30000.5,
    100 : (1,2,3),
    4.5 : {5,6,True,7,1},
    True : 1
}

print("Type of Employee: ", type(emp))
print("Length of Employee: ", len(emp))
print(emp["type"])
print(emp["age"])
print(emp[4.5])
print(emp["type"]["developer"])
print(emp["type"]["developer"][1])
emp["Parmanent"] = False
print(emp)
emp["gender"] = "male"
print(emp)
emp.pop("age")
for x in emp.keys():
    print(x)
for x in emp.items():
    print(x)
for x in emp.values():
    print(x)