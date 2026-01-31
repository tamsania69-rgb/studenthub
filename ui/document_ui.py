import tkinter as tk
from tkinter import filedialog, messagebox
import os
from services.document_manager import ajouter_document, recuperer_tous_documents
2
fenetre = tk.Tk()
fenetre.title("StudyHub - Documents")
fenetre.geometry("700x450")

def importer_fichier():
    chemin_fichier = filedialog.askopenfilename(
        filetypes=[
            ("Fichiers PDF", "*.pdf"),
            ("Images", "*.png *.jpg *.jpeg")
        ]
    )

    if not chemin_fichier:
        return

    titre = os.path.basename(chemin_fichier)
    matiere = champ_matiere.get()
    semestre = champ_semestre.get()
    type_fichier = chemin_fichier.split(".")[-1]

    if matiere == "" or semestre == "":
        messagebox.showwarning("Erreur", "Veuillez remplir la matière et le semestre")
        return

    ajouter_document(titre, matiere, semestre, chemin_fichier, type_fichier)
    rafraichir_liste()
    messagebox.showinfo("Succès", "Fichier ajouté avec succès")


def rafraichir_liste():
    liste_documents.delete(0, tk.END)
    documents = recuperer_tous_documents()

    for doc in documents:
        liste_documents.insert(tk.END, f"{doc[2]} | {doc[3]} | {doc[1]}")


def ouvrir_fichier():
    selection = liste_documents.curselection()
    if not selection:
        return

    documents = recuperer_tous_documents()
    document = documents[selection[0]]
    os.startfile(document[4])  # Windows

tk.Label(fenetre, text="Matière").pack(pady=5)
champ_matiere = tk.Entry(fenetre)
champ_matiere.pack()

tk.Label(fenetre, text="Semestre / Année").pack()
champ_semestre = tk.Entry(fenetre,width=10)
champ_semestre.pack()

tk.Button(fenetre, text="Importer PDF / Image", command=importer_fichier).pack(pady=5)

liste_documents = tk.Listbox(fenetre, width=50)
liste_documents.pack(pady=10)

tk.Button(fenetre, text="Ouvrir le fichier", command=ouvrir_fichier).pack()


# =====
tk.Label(fenetre, text="--- Filtres & Recherche ---").pack(pady=5)

champ_filtre_matiere = tk.Entry(fenetre)
champ_filtre_matiere.pack()
champ_filtre_matiere.insert(0, "Filtrer par matière")

champ_filtre_semestre = tk.Entry(fenetre)
champ_filtre_semestre.pack()
champ_filtre_semestre.insert(0, "Filtrer par semestre")

champ_recherche = tk.Entry(fenetre)
champ_recherche.pack()
champ_recherche.insert(0, "Rechercher par nom")

tk.Button(fenetre, text="Appliquer filtres", command=rafraichir_liste).pack(pady=6)

# LISTE DOCUMENTS 
liste_documents = tk.Listbox(fenetre, width=50)
liste_documents.pack(pady=10)

rafraichir_liste()
fenetre.mainloop()