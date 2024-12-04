import re
text = '''
Зимний вечер. Холодный ветер скользит по улицам города, но несмотря на это, на тротуарах можно увидеть следы, оставленные людьми, спешащими домой. 
Где-то вдалеке мерцают огоньки, отражаясь в витринах магазинов и светящихся окнах. 
В воздухе витает легкий запах снега и хвои, а тишина вокруг лишь усиливает ощущение спокойствия.

В кафе, на углу улицы, сидят несколько людей! Один из них с увлечением листает книгу, другой задумчиво смотрит в окно, в то время как третья компания обсуждает что-то важное. 
'''

try:
    letter = input('Введите букву: ').lower()
    if len(letter) != 1 or not letter.isalpha():
        raise ValueError("Введена не буква!")
    arr_words = [word.lower() for word in re.split(r'[\n,\.; !?]', text) if word]

    find_words = {word: arr_words.count(word) for word in arr_words if word[0] == letter}
    print('send =', letter, 'output: n =', len(find_words), ' ', dict(find_words))

except ValueError as e:
    print(f"Ошибка: {e}")

