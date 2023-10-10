# Створюємо порожній словник
my_dict = {}

# Додаємо пари ключ-значення до словника
my_dict['name'] = 'John'
my_dict['age'] = 30
my_dict['city'] = 'New York'

# Виводимо словник
print("Початковий словник:")
print(my_dict)

# Оновлюємо значення для ключа
my_dict['age'] = 31
print("Оновлений словник:")
print(my_dict)

# Видаляємо пару ключ-значення
del my_dict['city']
print("Словник після видалення ключа 'city':")
print(my_dict)

# Очищаємо весь словник
my_dict.clear()
print("Словник після очищення:")
print(my_dict)

# Створюємо новий словник
new_dict = {'name': 'Alice', 'age': 25, 'country': 'Canada'}

# Отримуємо ключі словника
keys = new_dict.keys()
print("Ключі словника:")
print(keys)

# Отримуємо значення словника
values = new_dict.values()
print("Значення словника:")
print(values)

# Отримуємо пари ключ-значення словника
items = new_dict.items()
print("Пари ключ-значення словника:")
print(items)
