# Students' Grades
n = int(input())

student_data = {}

for student in range(n):
    name, grade = input().split(' ')
    if name not in student_data:
        student_data[name] = []

    student_data[name].append(float(grade))

for student, grades in student_data.items():
    convert_grades_to_string = ' '.join(
        map(lambda grade: f'{grade:.2f}', grades))
    average_grade = sum(grades)/len(grades)
    print(f"{student} -> {convert_grades_to_string} (avg: {average_grade:.2f})")
