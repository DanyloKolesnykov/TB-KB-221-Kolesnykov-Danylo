# Початковий список
my_list = [10, 4, -1, 54, 5, 91, -102]

# Сортування списку
sorted_list = sorted(my_list)
print("Сортування списку - результат:", sorted_list)
print("Початковий список:", my_list)

# Перевертання списку
reversed_list = list(reversed(my_list))
print("Перевертання списку - результат:", reversed_list)
print("Початковий список:", my_list)

# Додавання до списку
my_list.append(4308)
print("Додавання до списку - результат:", my_list)

# Розширення списку
my_list.extend([9])
print("Розширення списку - результат:", my_list)

# Заміна в списку
my_list.insert(2, 43300)
print("Заміна в списку - результат:", my_list)

# Видалення зі списку
my_list.remove(43300)
print("Видалення зі списку - результат:", my_list)

# Копіювання списку
copy_list = my_list.copy()
print("Копіювання списку - результат:", copy_list)
print("Початковий список:", my_list)

# Довжина списку
length = len(my_list)
print("Довжина списку - результат:", length)

# Видалення списку
my_list.clear()
print("Видалення списку - результат:", my_list)
