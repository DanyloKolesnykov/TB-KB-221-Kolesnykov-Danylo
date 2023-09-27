import math

operation = input("Enter the operation to perform: (+ - * / ^ sqrt %) ")

number1 = float(input("Enter the first number: "))

if operation not in ['sqrt']:
    number2 = float(input("Enter the second number: "))

result = None

if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2
elif operation == '/':
    if number2 == 0:
        result = "Error: division by zero"
    else:
        result = number1 / number2
elif operation == '^':
    result = math.pow(number1, number2)
elif operation == 'sqrt':
    if number1 < 0:
        result = "Error: cannot compute square root of a negative number"
    else:
        result = math.sqrt(number1)
elif operation == '%':
    result = number1 % number2
else:
    result = "Invalid operation choice"

print(f"Result: {result}")
