list = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@example.com", "age": 25},
    {"name": "Emma", "phone": "0631234567", "email": "emma@example.com", "age": 22},
    {"name": "Jon", "phone": "0631234567", "email": "jon@example.com", "age": 28},
    {"name": "Tom", "phone": "0631234567", "email": "zak@example.com", "age": 24}
]

def printAllList():
    for elem in list:
        strForPrint = (
            f"Student name is {elem['name']}, Phone is {elem['phone']}, "
            f"Email is {elem['email']}, Age is {elem['age']}"
        )
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    age = int(input("Please enter student age: "))
    newItem = {"name": name, "phone": phone, "email": email, "age": age}
    list.append(newItem)
    list.sort(key=lambda x: x["name"])  
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    for item in list:
        if name == item["name"]:
            list.remove(item)
            list.sort(key=lambda x: x["name"])  
            print("Element has been deleted")
            return
    print("Element not found")

def updateElement():
    name = input("Please enter name to be updated: ")
    for i, item in enumerate(list):
        if name == item["name"]:
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email: ")
            new_age = int(input("Enter new age: "))

            list[i]["name"] = new_name
            list[i]["phone"] = new_phone
            list[i]["email"] = new_email
            list[i]["age"] = new_age

            list.sort(key=lambda x: x["name"])  
            print("Element has been updated")
            return
    print("Element not found")

def main():
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit] ")
        match choice.lower():
            case "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "p":
                print("List will be printed")
                printAllList()
            case "x":
                print("Exit()")
                break
            case _:
                print("Wrong choice")

main()
