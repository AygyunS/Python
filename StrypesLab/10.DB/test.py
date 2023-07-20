import sqlite3

# Свързване с базата данни (създава нов файл, ако не съществува)
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

# Създаване на таблиците
cursor.execute("""
CREATE TABLE IF NOT EXISTS Teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    year_of_study INTEGER NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    num_classes INTEGER NOT NULL,
    teacher_id INTEGER,
    required_for TEXT,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS CourseRegistrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    grade REAL,
    FOREIGN KEY (student_id) REFERENCES Students(id),
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);
""")

# Изпълнение на заявките и затваряне на връзката
conn.commit()
conn.close()
