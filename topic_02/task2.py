# Введення чисел та операції від користувача
num1 = float(input("Введіть перше число: "))
operator = input("Введіть операцію (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))

# Виконання обчислень на основі введеної операції
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Помилка: Ділення на нуль неможливе")
    else:
        result = num1 / num2
else:
    print("Помилка: Невідома операція")

print(f"Результат: {result}")

