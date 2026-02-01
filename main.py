import sqlite3
import tkinter as tk
from database import initialiser_base
import ui.document_ui

initialiser_base()

def main():
    from db.database import init_db
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