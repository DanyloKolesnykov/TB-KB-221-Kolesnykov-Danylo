num_1 = float(input("Введіть перше число: "))
num_2 = float(input("Введіть друге  число: "))
action = input("Яку дію ви хочете зробити?: ")
if action == "+":
    result = num_1 + num_2
    print(result)

elif action == "-":
    result = num_1  - num_2
    print(result)

elif action == "*":
    result = num_1 * num_2
    print(result)
else:
    result = num_1 / num_2
    print(result)
