def genIntValue(prompt: str):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Помилка: Введіть ціле число.")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Помилка: Ділення на нуль неможливе"
    return result

def main():
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

        num1 = genIntValue("Введіть перше число: ")
        num2 = genIntValue("Введіть друге число: ")

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            if num2 == 0:
                print("Помилка: Ділення на нуль неможливе")
                continue
            result = divide(num1, num2)

        print(f"Результат: {result}")

if __name__ == "__main__":
    main()
