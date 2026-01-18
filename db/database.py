import sqlite3
conn = sqlite3.connect("studyhub.db")
cursor = conn.cursor()

#  table Cours
cursor.execute("""
CREATE TABLE IF NOT EXISTS cours (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    semester TEXT NOT NULL,
    year INTEGER NOT NULL,
    description TEXT
)
""")

# table Document
cursor.execute("""
CREATE TABLE IF NOT EXISTS document (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    doc_type TEXT NOT NULL,
    content TEXT,
    course_id INTEGER,
    FOREIGN KEY(course_id) REFERENCES course(id)
)
""")

# table Event
cursor.execute("""
CREATE TABLE IF NOT EXISTS event (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    event_type TEXT NOT NULL,
    date TEXT,
    description TEXT
)
""")

#  table Grade
cursor.execute("""
CREATE TABLE IF NOT EXISTS grade (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER,
    value REAL NOT NULL,
    max_value REAL NOT NULL,
    FOREIGN KEY(course_id) REFERENCES course(id)
)
""")

conn.commit()
conn.close()

print("Toutes les tables ont été créées avec succès.")