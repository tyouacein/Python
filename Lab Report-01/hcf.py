def hcf(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The HCF of {num1} and {num2} is: {hcf(num1, num2)}")