# Приклад використання __init__
class Student:
    def __init__(self, name, points):
        self.name = name
        self.points = points
    
    # Приклад використання __str__
    def __str__(self):
        return f"Student {self.name} has a {self.points} points"

student = Student("Danylo", 75)
print(student)