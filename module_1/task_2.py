import json

students = {}
# Открываем файл и загружаем данные
with open('students.json', 'r') as file:
    students = json.load(file)


def comp(list1, list2):
    for val in list1:
        if val in list2:
            return True
    return False


bad_score = [2, 3]
count_students = len(students)
subjects = ["mathematics", "physics", "informatics"]
majors = ["Mathematics", "Physics", "Computer Science", "Software Engineering", "Information Security"]


def format_input_fio(student):
    return "{s} {n} {m}".format(s=student['last_name'],
                                n=student['first_name'],
                                m=student["last_name"])


def avg(numbers):
    return round(sum(numbers) / len(numbers), 2) if numbers else 0


good_students = [format_input_fio(student) for student in students if
                 all(grade >= 4 for grade in student["grades"].values())]
bad_students = [format_input_fio(student) for student in students if
                any(grade == 2 for grade in student["grades"].values())]

average_grades = {subject: sum(student["grades"][subject] for student in students) / count_students for subject in
                  subjects}
specialty_twos = {major: sum(grade == 2 for student in students
                             if student["specialty"] == major
                             for grade in student["grades"].values())
                  for major in majors}
best_subjects = {subject: avg for subject, avg in average_grades.items() if avg == max(average_grades.values())}
least_twos_specialties = [major for major, count in specialty_twos.items() if count == min(specialty_twos.values())]

course_averages = {course: sum(
    avg(student["grades"].values()) for student in students if student["course"] == course)
                           / len([s for s in students if s["course"] == course])
                   for course in range(1, 5)
                   }
best_courses = [course for course, avg in course_averages.items() if avg == max(course_averages.values())]

print("ФИО (Фамилии) тех, у кого среди оценок только 4 или 5: ", good_students)
print("ФИО (Фамилии) тех, у кого среди оценок есть хотя бы одна 2:", bad_students)
print("Предмет (предметы), который (которые) сдали лучше других по итогам сессии: ", best_subjects)
print("Найти название специальностей (специальности), у студентов которых (которой) меньшее количество 2",
      least_twos_specialties)
print("Номер курса (курсов), студенты которого (которых) лучше сдали сессию: ", best_courses)
