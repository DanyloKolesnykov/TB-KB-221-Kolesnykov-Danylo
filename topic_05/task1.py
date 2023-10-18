import random

def get_user_choice():
    """Функція для отримання вибору користувача."""
    user_choice = input("Оберіть: Камінь (r), Ножиці (s), або Папір (p): ")
    if user_choice not in ['r', 's', 'p']:
        print("Невірний вибір. Спробуйте ще раз.")
        return get_user_choice()
    return user_choice

def get_computer_choice():
    """Функція для отримання випадкового вибору комп'ютера."""
    choices = ['r', 's', 'p']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user, computer):
    """Функція для визначення переможця."""
    if user == computer:
        return "Нічия"
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return "Ви виграли!"
    return "Комп'ютер виграв."

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"Ваш вибір: {user_choice}")
    print(f"Вибір комп'ютера: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Грати ще раз? (y / n): ").lower()
    if play_again != 'y':
        break
