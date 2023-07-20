import sqlite3

def fetch_all_data(cursor):
    # Извличане на преподаватели
    cursor.execute("SELECT * FROM Teachers;")
    teachers = cursor.fetchall()
    print("Преподаватели:")
    for teacher in teachers:
        print(teacher)

    # Извличане на студенти
    cursor.execute("SELECT * FROM Students;")
    students = cursor.fetchall()
    print("\nСтуденти:")
    for student in students:
        print(student)

    # Извличане на курсове
    cursor.execute("""
    SELECT Courses.id, Courses.name, Courses.num_classes, Courses.required_for, Teachers.name, Teachers.position 
    FROM Courses 
    JOIN Teachers ON Courses.teacher_id = Teachers.id;
    """)
    courses = cursor.fetchall()
    print("\nКурсове:")
    for course in courses:
        print(course)

    # Извличане на записи за курсове
    cursor.execute("""
    SELECT CourseRegistrations.id, Students.name, Courses.name, CourseRegistrations.grade 
    FROM CourseRegistrations 
    JOIN Students ON CourseRegistrations.student_id = Students.id 
    JOIN Courses ON CourseRegistrations.course_id = Courses.id;
    """)
    course_registrations = cursor.fetchall()
    print("\nЗаписи за курсове:")
    for course_registration in course_registrations:
        print(course_registration)

# Свързване с базата данни
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

# Извличане и извеждане на данните
fetch_all_data(cursor)

# Затваряне на връзката
conn.close()
