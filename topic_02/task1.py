import math
a = float(input("Введіть коефіціент a: "))
b = float(input("Введіть коефіціент b: "))
c = float(input("Введіть коефіціент c: "))
D = b**2 - 4 *a *c
if D > 0:
    x1 = (-b + math.sqrt(D) / 2 * a)
    x2 = (-b - math.sqrt(D) / 2 * a)
    print(f"Рівняння має два корені: x1 = {x1}, x2 = {x2}")
elif D==0:
    x1 = -b/(2 * a)
    print(f"Рівняння має один подвійний корінь: x1 = {x1}")
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-D) / (2*a)
    print(f"Рівняння має два комплексні корені: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i")

    