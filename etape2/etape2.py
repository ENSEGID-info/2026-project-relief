"""Étape 2 : traitement ou analyse des données.

Ce fichier enchaîne les tâches du sous-groupe 2.
Renommez tache1.py, tache2.py, tache3.py selon ce qu'ils font,
et mettez à jour les imports ci-dessous.
"""

from .tache1 import calculer_minimum
from .tache2 import calculer_maximum
from .tache3 import calculer_moyenne


def etape2_main(donnees):
    """Exécute l'étape 2 et renvoie les résultats sous forme de dictionnaire."""
    print("Exécution de l'étape 2...")
    resultats = {
        "minimum": calculer_minimum(donnees),
        "maximum": calculer_maximum(donnees),
        "moyenne": calculer_moyenne(donnees),
    }
    return resultats
