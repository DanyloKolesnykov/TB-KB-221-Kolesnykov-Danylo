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

    # Вивести результат в консоль
    print(f"Результат: {result}")

    # Записати лог у файл у режимі додавання
    with open("log.txt", "a") as log_file:
        log_entry = f"Введено: {x}, {y}, Операція: {operation}, Результат: {result}\n"
        log_file.write(log_entry)

    again = input("Бажаєте продовжити? (Так/Ні): ")
    if again.lower() != "так":
        break
