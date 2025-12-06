# Asking for user inputs
number1 = int(input("Enter 1st number: "))

# Operation menu
print("Pick your operator")
print("1. +")
print("2. -")
print("3. x")
print("4. / ")
operation = int(input(""))

number2 = int(input("Enter 2nd number: "))

# Logic for operations

if operation == 3:
    product = number1 * number2
    print(product)
elif operation == 2:
    difference = number1 - number2
    print(difference)
elif operation == 1:
    sum = number1 + number2
    print(sum)
else:
    quotient = number1 / number2
    print(quotient)