class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Створення об'єктів класу Student
students = [
    Student("Alice", 22),
    Student("Bob", 20),
    Student("Charlie", 21),
    Student("David", 19),
]

# Власна функція для сортування
def custom_sort(student):
    return student.age  # Сортування за віком

# Сортування студентів за допомогою власної функції custom_sort
sorted_students = sorted(students, key=custom_sort)

# Виведення відсортованого списку студентів
for student in sorted_students:
    print(f"Name: {student.name}, Age: {student.age}")
