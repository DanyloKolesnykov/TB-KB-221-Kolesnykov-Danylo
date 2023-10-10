def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Помилка: ділення на нуль"

choice = input("Введіть яку операцію ви хочете зробити?: ")

number1 = float(input("Введіть перше число: "))
number2 = float(input("Введіть друге число: "))

if choice == "+":
    result = addition(number1, number2)
elif choice == "-":
    result = subtraction(number1, number2)
elif choice == "*":
    result = multiplication(number1, number2)
elif choice == "/":
    result = division(number1, number2)
else:
    result = "Невірний вибір операції"

print("Результат: ", result)
