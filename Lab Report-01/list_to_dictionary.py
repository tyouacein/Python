list = ['name', 'Alice', 'age', 25, 'city', 'New York']

dict = {list[i]: list[i + 1] for i in range(0, len(list), 2)}

print("List:", list)
print("Dictionary:", dict)