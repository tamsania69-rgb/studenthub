import sqlite3
from db.database import DB_PATH

def add_course(title, semester, year):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO courses (title, description, created_at, semester, year) VALUES (?, ?, CURRENT_TIMESTAMP, ?, ?)",
        (title, "", semester, year)
    )
    conn.commit()
    conn.close()

def get_all_courses():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_course(course_id, title, semester, year):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE courses SET title=?, semester=?, year=? WHERE id=?",
        (title, semester, year, course_id)
    )
    conn.commit()
    conn.close()

def delete_course(course_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM courses WHERE id=?", (course_id,))
    conn.commit()
    conn.close()

