customers = ["Alice", "Bob", "Charlie", "David", "Eve"]

# a
print("Third customer:", customers[2])
print()

# b
customers[1] = "Ben"
print("Change second customer's name:", customers)
print()

# c
customers.append("Frank")
print("Adding new customer:", customers)
print()

# d
customers.remove("David")
print("Removing customer 'David':", customers)
print()

# e
customers.sort()
print("Final sorted list:", customers)