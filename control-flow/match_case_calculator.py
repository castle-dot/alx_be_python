num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /):")
if operation == "+":
    print(f'The result is {num1 + num2}.')
elif operation == '-':
    print(f'The result is {num1 - num2}.')
elif operation == '*':
    print(f'The result is {num1 * num2}.')
elif operation == '/':
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print(f'The result is {num1 / num2}.')
else:
    print("Please Try Again!")

