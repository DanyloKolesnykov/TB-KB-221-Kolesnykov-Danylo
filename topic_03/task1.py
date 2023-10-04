def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Помилка: Ділення на нуль неможливе"
    return x / y

while True:
    print("Оберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вихід")

    choice = input("Введіть номер операції (1/2/3/4/5): ")

    if choice == '5':
        print("Дякую за використання калькулятора!")
        break

    if choice not in ['1', '2', '3', '4']:
        print("Неправильний вибір операції. Спробуйте ще раз.")
        continue

    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)

    print(f"Результат: {result}")
