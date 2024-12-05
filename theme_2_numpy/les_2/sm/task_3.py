import numpy as np


def get_array_from_input():
    array_type = input(
        "Вы хотите создать одномерный или многомерный массив? (введите '1' для одномерного или '2' для многомерного): ").strip()

    if array_type == '1':
        raw_data = input("Введите элементы одномерного массива, разделенные пробелами: ").strip()
        array = np.array([float(x) for x in raw_data.split()])

    elif array_type == '2':
        rows = int(input("Введите количество строк: ").strip())
        print("Введите элементы массива построчно. Элементы в строке разделяйте пробелами.")
        data = []
        for i in range(rows):
            raw_row = input(f"Строка {i + 1}: ").strip()
            data.append([float(x) for x in raw_row.split()])
        array = np.array(data)

    else:
        raise ValueError("Неверный выбор. Перезапустите программу и введите '1' или '2'.")

    return array


try:
    user_array = get_array_from_input()
    print("Введенный массив:")
    print(user_array)

    filename = "user_array.txt"
    np.savetxt(filename, user_array, fmt='%f', delimiter=' ')
    print(f"Массив сохранен в файл {filename}")

    loaded_array = np.loadtxt(filename, delimiter=' ')
    print("Загруженный массив:")
    print(loaded_array)

except Exception as e:
    print(f"Произошла ошибка: {e}")
