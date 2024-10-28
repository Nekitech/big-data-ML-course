import json
import math


students = {}
# Открываем файл и загружаем данные
with open('students.json', 'r') as file:
    students = json.load(file)
    print(students)

def comp(list1, list2):
    for val in list1:
        if val in list2:
            return True
    return False

bad_score = [2, 3]

good_students = [student for student in students if comp(student["grades"].values(), bad_score)]
print([student["grades"].values() for student in good_students])
print(good_students)
