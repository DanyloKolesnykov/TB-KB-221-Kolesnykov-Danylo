def test_dictionary_operations():
    # Створення порожнього словника
    my_dict = {}

    # Додавання пар ключ-значення до словника
    my_dict['name'] = 'John'
    my_dict['age'] = 30
    my_dict['city'] = 'New York'
    my_dict['country'] = 'USA'
    my_dict['job'] = 'Engineer'
    my_dict['email'] = 'john@example.com'

    # Перевірка наявності ключів у словнику
    assert 'name' in my_dict
    assert 'city' in my_dict

    # Перевірка доступу до значень за ключами
    assert my_dict['age'] == 30
    assert my_dict['email'] == 'john@example.com'

    # Перевірка зміни значень за ключами
    my_dict['age'] = 31
    assert my_dict['age'] == 31

    # Перевірка видалення пар ключ-значення за ключем
    del my_dict['job']
    assert 'job' not in my_dict

    # Перевірка отримання списку всіх ключів та значень
    keys = list(my_dict.keys())
    values = list(my_dict.values())
    assert keys == ['name', 'age', 'city', 'country', 'email']
    assert values == ['John', 31, 'New York', 'USA', 'john@example.com']

    # Перевірка отримання пар ключ-значення у вигляді кортежів
    items = list(my_dict.items())
    assert items == [('name', 'John'), ('age', 31), ('city', 'New York'), ('country', 'USA'), ('email', 'john@example.com')]

    print("Усі операції словників успішно протестовані!")

if __name__ == "__main__":
    test_dictionary_operations()
