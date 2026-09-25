def sauvegarder(texte, nom_fichier):
    """Exemple : écrit un texte dans un fichier (donnée produite par l'étape)."""
    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        fichier.write(texte)
    print("Résultats sauvegardés dans " + nom_fichier)
