str1 = "apple12331231"
str2 = "banana!$@$%hhdfgh"

# Додавання рядків і виведення результату
result = str1 + " " + str2
print("Додавання рядків:", result)

# Довжина рядків
length_str1 = len(str1)
length_str2 = len(str2)
print("Довжина першого рядка:", length_str1)
print("Довжина другого рядка:", length_str2)

# Вирізка підрядка  
substring_str1 = str1[2:7]
substring_str2 = str2[6:11]
print("Вирізка підрядка з першого рядка:", substring_str1)
print("Вирізка підрядка з другого рядка:", substring_str2)

# Пошук підрядка
search_string = "banana"
if search_string in str2:
    print(f"Рядок '{search_string}' знайдений в другому рядку.")
else:
    print(f"Рядок '{search_string}' не знайдений в другому рядку.")

# Верхній та нижній регістр
uppercase_str1 = str1.upper()
lowercase_str2 = str2.lower()
print("Перший рядок у верхньому регістрі:", uppercase_str1)
print("Другий рядок у нижньому регістрі:", lowercase_str2)

# Заміна підрядка
replaced_str2 = str2.replace("banana", "orange")
print("Заміна підрядка у другому рядку:", replaced_str2)

# Розділення рядка на список
words_str2 = str2.split("!")
print("Розділення другого рядка на список за символом '!':", words_str2)

# Об'єднання списку в рядок
joined_string = " ".join(words_str2)
print("Об'єднання списку в рядок:", joined_string)

# Перевірка, чи є рядок числовим
numeric_str1 = "12345"
is_numeric = numeric_str1.isnumeric()
print(f"Чи є рядок '{numeric_str1}' числовим: {is_numeric}")

# Видалення пробілів з другого рядка
whitespace_str2 = "  Пробіли  "
stripped_str2 = whitespace_str2.strip()
print("Видалення пробілів з другого рядка:", stripped_str2)
