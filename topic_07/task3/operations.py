class CalculatorOperations:
    @staticmethod
    def get_user_input():
        x = CalculatorOperations.genIntValue("Введіть перше число: ")
        y = CalculatorOperations.genIntValue("Введіть друге число: ")
        return x, y

    @staticmethod
    def get_operation():
        while True:
            operation = input("Виберіть операцію (+, -, *, /): ")
            if operation in ('+', '-', '*', '/'):
                return operation
            else:
                print("Неправильний вибір операції. Будь ласка, виберіть одну з операцій (+, -, *, /).")

    @staticmethod
    def genIntValue(prompt: str):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Значення повинно бути цілим числом")
