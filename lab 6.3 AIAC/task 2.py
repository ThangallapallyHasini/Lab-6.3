number = int(input("Enter a number to see its first 10 multiples: "))
#using for loop
print(f"\nFirst 10 multiples of {number} using for loop:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Using while loop
print(f"\nFirst 10 multiples of {number} using while loop:")
i = 1
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1