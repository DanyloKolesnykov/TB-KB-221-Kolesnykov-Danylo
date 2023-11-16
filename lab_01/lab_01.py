
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "surname": "Mirales", "phone":"0631234567", "email": "bob123@gmail.com" },
    {"name":"Emma", "surname": "Tompson","phone":"0631234567", "email": "emmatompson@gmail.com"},
    {"name":"Jon",  "surname": "Tas","phone":"0631234567", "email": "jonsons@gmail.com"},
    {"name":"Zak",  "surname": "Mykolenko","phone":"0631234A567", "email": "mykolenko@gmail.com"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ", Surname is "+elem["surname"] + ",  Phone is " + elem["phone"] + ", " + ", email is " +elem["email"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    surname = input("Please enter student surname: ")
    phone = input("Please enter student phone: ")   
    email = input("Please enter student email: ")
    newItem = {"name": name,"surname": surname, "phone": phone, "email": email}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    for i, item in enumerate(list):
        if name == item["name"]:
            new_name = input("Enter a new name: ")
            new_surname = input("Enter a new surname: ")
            new_phone = input("Enter a new phone: ")
            new_email = input("Enter a new email: ")

            # Додайте ключ "surname", якщо його немає
            if "surname" not in list[i]:
                list[i]["surname"] = ""

            list[i]["name"] = new_name
            list[i]["surname"] = new_surname
            list[i]["phone"] = new_phone
            list[i]["email"] = new_email



def main():
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit] ").lower()
        match choice:
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



