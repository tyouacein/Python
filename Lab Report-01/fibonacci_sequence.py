fibo = int(input("Enter a number: "))
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(fibo):
    print(a)
    a, b = b, a + b