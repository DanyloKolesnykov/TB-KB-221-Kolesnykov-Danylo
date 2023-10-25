# Не відсортований список словників
data = [
    {"ім'я": "Anna", "оцінка": 95},
    {"ім'я": "Petro", "оцінка": 85},
    {"ім'я": "Maria", "оцінка": 92},
    {"ім'я": "Ivan", "оцінка": 78},
]

# Вивести список не відсортований
print("Список не відсортований:")
for item in data:
    print(item)

# Функція для сортування за ключем (ім'я або оцінка)
def sort_by_key(data, key):
    sorted_data = sorted(data, key=lambda x: x[key])
    return sorted_data

# Сортування за ім'ям
sorted_by_name = sort_by_key(data, "ім'я")

# Виведення відсортованого списку за ім'ям
print("Список відсортований за ім'ям:")
for item in sorted_by_name:
    print(item)

# Сортування за оцінкою
sorted_by_score = sort_by_key(data, "оцінка")

# Виведення відсортованого списку за оцінкою
print("Список відсортований за оцінкою:")
for item in sorted_by_score:
    print(item)
