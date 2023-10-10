def dicriminant(a, b, c):
    D = b**2 - 4 * a * c
    return D
a = float(input("Введіть коефіцієнт а: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))
print(dicriminant(a, b, c))