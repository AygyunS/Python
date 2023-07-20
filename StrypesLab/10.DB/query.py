import sqlite3

def insert_teacher(cursor, name, position):
    cursor.execute("""
    INSERT INTO Teachers (name, position) VALUES (?, ?);
    """, (name, position))

def insert_student(cursor, name, year_of_study):
    cursor.execute("""
    INSERT INTO Students (name, year_of_study) VALUES (?, ?);
    """, (name, year_of_study))

def insert_course(cursor, name, num_classes, teacher_id, required_for):
    cursor.execute("""
    INSERT INTO Courses (name, num_classes, teacher_id, required_for) VALUES (?, ?, ?, ?);
    """, (name, num_classes, teacher_id, required_for))

def insert_course_registration(cursor, student_id, course_id, grade):
    cursor.execute("""
    INSERT INTO CourseRegistrations (student_id, course_id, grade) VALUES (?, ?, ?);
    """, (student_id, course_id, grade))

# Свързване с базата данни
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

# Добавяне на преподаватели
insert_teacher(cursor, "Иван Иванов", "Професор")
insert_teacher(cursor, "Петър Петров", "Доцент")

# Добавяне на студенти
insert_student(cursor, "Георги Георгиев", 1)
insert_student(cursor, "Мария Маринова", 2)

# Добавяне на курсове
insert_course(cursor, "Математика", 30, 1, "Бакалавър")
insert_course(cursor, "Физика", 20, 2, "Бакалавър")

# Добавяне на записи за курсове
insert_course_registration(cursor, 1, 1, 5.5)
insert_course_registration(cursor, 1, 2, 6.0)
insert_course_registration(cursor, 2, 1, 4.5)

# Запазване на промените и затваряне на връзката
conn.commit()
conn.close()
