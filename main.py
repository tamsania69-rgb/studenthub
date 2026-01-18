import sqlite3
import tkinter as tk

def init_db():
    conn = sqlite3.connect("studyhub.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS TestInit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()
    print("Base de données initialisée")

def main():
    init_db()
    root = tk.Tk()
    root.title("StudentHub - Lancement Minimal")
    root.geometry("300x200")
    label = tk.Label(root, text="StudentHub fonctionne et s'ouvre correctement!")
    label.pack(pady=50)
    root.mainloop()

if __name__ == "__main__":
    main()
from services.course_manager import add_course, get_all_courses

add_course("Maths", 1, 2026)
print(get_all_courses())