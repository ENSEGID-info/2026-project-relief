"""Étape 3 : résultats ou affichage final.

Ce fichier enchaîne les tâches du sous-groupe 3.
Renommez tache1.py, tache2.py, tache3.py selon ce qu'ils font,
et mettez à jour les imports ci-dessous.
"""

from .tache1 import formater_resultats
from .tache2 import afficher
from .tache3 import sauvegarder


def etape3_main(resultats):
    """Exécute l'étape 3 : affiche et sauvegarde les résultats."""
    print("Exécution de l'étape 3...")
    texte = formater_resultats(resultats)
    afficher(texte)
    sauvegarder(texte, "resultats.txt")
