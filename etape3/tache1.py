def formater_resultats(resultats):
    """Exemple : transforme un dictionnaire de résultats en texte lisible."""
    lignes = []
    for nom, valeur in resultats.items():
        lignes.append(nom + " : " + str(valeur))
    return "\n".join(lignes)
