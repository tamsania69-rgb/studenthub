import sqlite3

NOM_BASE = "studyhub.db"

def ajouter_document(titre, matiere, semestre, chemin_fichier, type_fichier):
    connexion = sqlite3.connect(NOM_BASE)
    curseur = connexion.cursor()

    curseur.execute("""
        INSERT INTO Document (titre, matiere, semestre, chemin_fichier, type_fichier)
        VALUES (?, ?, ?, ?, ?)
    """, (titre, matiere, semestre, chemin_fichier, type_fichier))

    connexion.commit()
    connexion.close()


def recuperer_tous_documents():
    connexion = sqlite3.connect(NOM_BASE)
    curseur = connexion.cursor()

    curseur.execute("SELECT * FROM Document")
    documents = curseur.fetchall()

    connexion.close()
    return documents

def recuperer_documents_filtres(matiere=None, semestre=None, recherche=None):
    connexion = sqlite3.connect(NOM_BASE)
    curseur = connexion.cursor()

    requete = "SELECT * FROM Document WHERE 1=1"
    parametres = []

    if matiere:
        requete += " AND matiere LIKE ?"
        parametres.append(f"%{matiere}%")

    if semestre:
        requete += " AND semestre LIKE ?"
        parametres.append(f"%{semestre}%")

    if recherche:
        requete += " AND titre LIKE ?"
        parametres.append(f"%{recherche}%")

    curseur.execute(requete, parametres)
    documents = curseur.fetchall()

    connexion.close()
    return documents