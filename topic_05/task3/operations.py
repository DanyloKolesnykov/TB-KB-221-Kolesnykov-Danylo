def genIntValue(prompt: str):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Значення повинно бути цілим числом")

def get_user_input():
    x = genIntValue("Введіть перше число: ")
    y = genIntValue("Введіть друге число: ")
    return x, y

def get_operation():
    while True:
        operation = input("Виберіть операцію (+, -, *, /): ")
        if operation in ('+', '-', '*', '/'):
            return operation
        else:
            print("Неправильний вибір операції. Будь ласка, виберіть одну з операцій (+, -, *, /).")


if __name__ == "__main__":
    x, y = get_user_input()
    operation = get_operation()
