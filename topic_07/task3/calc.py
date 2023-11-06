import functions
import operations

class Calculator:
    def run(self):
        while True:
            x, y = operations.CalculatorOperations.get_user_input()
            operation = operations.CalculatorOperations.get_operation()

            if operation == '+':
                result = functions.CalculatorFunctions.add(x, y)
            elif operation == '-':
                result = functions.CalculatorFunctions.subtract(x, y)
            elif operation == '*':
                result = functions.CalculatorFunctions.multiply(x, y)
            elif operation == '/':
                result = functions.CalculatorFunctions.divide(x, y)
            else:
                result = "Непідтримувана операція"

            # Вивести результат в консоль
            print(f"Результат: {result}")

            # Записати лог у файл у режимі додавання
            with open("log.txt", "a") as log_file:
                log_entry = f"Введено: {x}, {y}, Операція: {operation}, Результат: {result}\n"
                log_file.write(log_entry)

            again = input("Бажаєте продовжити? (Так/Ні): ")
            if again.lower() != "так":
                break

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
