import math

def calculate_discriminant_and_roots(a, b, c):
    # Формула
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant > 0:
        # Два різних корені
        sqrt_discriminant = math.sqrt(discriminant)

        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)

        return f"Два різних дійсних корені: root1 = {root1}, root2 = {root2}"
    
    elif discriminant == 0:
        # Один корінь 
        root = -b / (2 * a)
        return f"Один дійсний корінь: root = {root}"
    
    else:
        # Немає дійсних коренів
        return "Немає дійсних коренів"

# Введення коефіцієнтів a, b, і c від користувача
a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

result = calculate_discriminant_and_roots(a, b, c)
print(result)
