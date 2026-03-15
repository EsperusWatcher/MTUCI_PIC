groupmates = [
{
"name": u"Василий",
"group": "912-2",
"age": 19,
"marks": [4, 3, 5, 5, 4]
},
{
"name": u"Анна",
"group": "912-1",
"age": 18,
"marks": [3, 2, 3, 4, 3]
},
{
"name": u"Георгий",
"group": "912-2",
"age": 19,
"marks": [3, 5, 4, 3, 5]
},
{
"name": u"Валентина",
"group": "912-1",
"age": 18,
"marks": [5, 5, 5, 4, 5]
}
]

def print_students(students):
    print (u"Имя студента".ljust(15), \
        u"Группа".ljust(8), \
        u"Возраст".ljust(8), \
        u"Оценки".ljust(20))
    for student in students:
        print (\
            student["name"].ljust(15), \
            student["group"].ljust(8), \
            str(student["age"]).ljust(8), \
            str(student["marks"]).ljust(20))
    print ("\n")

def filter_students(students, min_avg_mark):
    filtered_students = []
    
    for student in students:
        marks = student["marks"]
        avg_mark = sum(marks) / len(marks)
        
        if avg_mark > min_avg_mark:
            filtered_students.append(student)
    
    return filtered_students

print("Все студенты:")
print_students(groupmates)

print("Студенты со средним баллом выше 4.0:")
filtered = filter_students(groupmates, 4.0)
print_students(filtered)

print("Студенты со средним баллом выше 3.5:")
filtered = filter_students(groupmates, 3.5)
print_students(filtered)

