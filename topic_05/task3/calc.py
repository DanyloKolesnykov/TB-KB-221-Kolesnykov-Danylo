import functions
import operations

while True:
    x, y = operations.get_user_input()
    operation = operations.get_operation()

    if operation == '+':
        result = functions.add(x, y)
    elif operation == '-':
        result = functions.subtract(x, y)
    elif operation == '*':
        result = functions.multiply(x, y)
    elif operation == '/':
        result = functions.divide(x, y)
    else:
        result = "Непідтримувана операція"

    print(f"Результат: {result}")

    again = input("Бажаєте продовжити? (Так/Ні): ")
    if again.lower() != "так":
        break
