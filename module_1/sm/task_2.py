import re


arr = [
    'Питон язык программирования',
    'Питон входит в 3 популярных языков программирования',
    'Питон использует динамическую типизацию',
    'Питон обладает интуитивно понятным синтаксисом'
]
try:

    send = input("Введите текст для поиска: ").lower()

    if len(send) != 1 or not send.isalpha():
        raise ValueError("Введено не слово!")

    found_indices = [index for index, text in enumerate(arr) if re.search(r'\b' + re.escape(send) + r'\b', text)]

    print(f"Количество найденных запросов: {len(found_indices)}")
    print(f"Номера элементов массива, в которых запрос найден: {found_indices}")

except ValueError as e:
    print(f"Ошибка: {e}")