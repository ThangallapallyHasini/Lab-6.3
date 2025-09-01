def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Ask user to enter a value for n
n = int(input("Enter a number to find the sum of first n numbers: "))

# Call the function and print the result
result = sum_to_n(n)
print(f"The sum of the first {n} numbers is: {result}")