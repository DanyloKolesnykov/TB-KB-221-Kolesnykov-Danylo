import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ділення на нуль неможливе"
    return x / y

while True:
    print("Виберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5 Вихід")

    choice = input("Введіть номер операції (1/2/3/4/5): ")
    
    match choice:
        case '1':
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
            print("Результат:", add(num1, num2))
        case '2':
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
            print("Результат:", subtract(num1, num2))
        case '3':
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
            print("Результат:", multiply(num1, num2))
        case '4':
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
            result = divide(num1, num2)
            print("Результат:", result)
        case '5':
            print("Бувай!")
            break
        case _:
            print("Невірний вибір. Будь ласка спробуйте ще раз.")
