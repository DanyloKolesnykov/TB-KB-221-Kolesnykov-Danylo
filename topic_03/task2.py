list = [10, 4, -1, 54, 5, 91, -102]
#Сортування списку
list.sort()
print(list)
# перевертання списку
list.reverse()
print(list)
#Додавання до списку
list.append(4308)
print(list)
#Розширення списку
list.extend([9])
print(list)
#Заміна в списку
list.insert(2202, 43300)
print(list)
#Видалення зі списку
list.remove(43300)
print(list)
#Копіювання списку
copy_list = list.copy()
print(list)
print(copy_list)
# Довжина списку
dv = list.__len__()
print(dv)
#Видалення списку
list.clear()
print(list)
