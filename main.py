import sqlite3
import tkinter as tk
from database import initialiser_base
import ui.document_ui

initialiser_base()

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
