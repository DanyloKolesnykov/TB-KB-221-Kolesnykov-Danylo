import requests

# Словник з відповідностями між кодами валют і країнами
currency_countries = {
    "EUR": "Єврозона",
    "USD": "Сполучені Штати Америки",
    "PLN": "Польща",
    "GBP": "Велика Британія",
    "CAD": "Канада",
    "JPY": "Японія",
    "CNY": "Китай",
    "AUD": "Австралія",
    "CHF": "Швейцарія",
    "SEK": "Швеція"
}

def get_exchange_rate(currency_code):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(url)
    data = response.json()
    for item in data:
        if item["cc"] == currency_code:
            return item["rate"]
    raise Exception("Помилка при отриманні курсу валюти")

def convert_currency(amount, currency_code):
    try:
        rate = get_exchange_rate(currency_code)
        converted_amount = amount / rate
        return converted_amount
    except Exception as e:
        return f"Помилка: {e}"

while True:
    user_input = input("Введіть суму в гривнях або 'exit' для виходу: ")
    
    if user_input == 'exit':
        print("Дякую за використання програми. До побачення!")
        break  # Виходимо з циклу при введенні "exit"
    
    try:
        amount = float(user_input)
        
        if amount <= 0:
            raise ValueError("Помилка: Сума повинна бути більше нуля.")
        print(currency_countries)
        currency_code = input("Введіть код валюти для конвертації: ").upper()

        # Перевірка, чи код валюти є в списку
        if currency_code in currency_countries:
            result = convert_currency(amount, currency_code)
            country_name = currency_countries[currency_code]
            print(f"{amount} UAH = {result:.2f} {currency_code} - {country_name}")
        else:
            print("Код валюти введений невірно або дана валюта не підтримується. Спробуйте ще раз.")
    except ValueError as ve:
        print(f"Помилка: {ve}")
    except Exception as e:
        print(f"Помилка: {e}")
