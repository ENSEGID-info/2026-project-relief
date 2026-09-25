"""Étape 1 : lecture ou préparation des données.

Ce fichier enchaîne les tâches du sous-groupe 1.
Renommez tache1.py, tache2.py, tache3.py selon ce qu'ils font,
et mettez à jour les imports ci-dessous.
"""

from .tache1 import lire_donnees
from .tache2 import nettoyer
from .tache3 import trier


def etape1_main():
    """Exécute l'étape 1 et renvoie les données préparées."""
    print("Exécution de l'étape 1...")
    donnees = lire_donnees()
    donnees = nettoyer(donnees)
    donnees = trier(donnees)
    print("Données préparées : " + str(donnees))
    return donnees
