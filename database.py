import sqlite3
conn = sqlite3.connect("studyhub.db")
cursor = conn.cursor()

#  table Cours
cursor.execute("""
CREATE TABLE IF NOT EXISTS cours (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
)
""")

# table Document
cursor.execute("""
CREATE TABLE IF NOT EXISTS document (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT,
    course_id INTEGER,
    FOREIGN KEY(course_id) REFERENCES Course(id)
)
""")

# table Event
cursor.execute("""
CREATE TABLE IF NOT EXISTS event (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    date TEXT,
    description TEXT
)
""")

#  table Grade
cursor.execute("""
CREATE TABLE IF NOT EXISTS grade (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER,
    score REAL NOT NULL,
    FOREIGN KEY(course_id) REFERENCES Course(id)
)
""")

print("Toutes les tables ont été créées avec succès.")

def initialiser_base():
    connexion = sqlite3.connect("studyhub.db")
    curseur = connexion.cursor()

    curseur.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT,
        matiere TEXT,
        semestre TEXT,
        chemin_fichier TEXT,
        type_fichier TEXT,
        date_ajout TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)


conn.commit()
conn.close()

   

