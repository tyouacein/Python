import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

root = b**2 - 4*a*c
if root > 0:
    root1 = (-b + math.sqrt(root)) / (2*a)
    root2 = (-b - math.sqrt(root)) / (2*a)
    print(f"Two real solutions: {root1} and {root2}")
elif root == 0:
    sol = -b / (2*a)
    print(f"One real solution: {sol}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-root) / (2*a)
    print(f"Two complex solutions: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")