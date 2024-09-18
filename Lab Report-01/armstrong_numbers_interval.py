start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))
for num in range(start, end + 1):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    if sum_of_powers == num:
        print(num)
