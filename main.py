# ===============================
# Projet Informatique
# Programme principal
# ===============================
# Fichier géré par le chef d'équipe.

import etape1
import etape2
import etape3


def main():
    print("=== Début du programme ===")

    # Étape 1 – Lecture ou préparation des données
    print("\n--- Étape 1 : Lecture ou préparation ---")
    donnees = etape1.etape1_main()

    # Étape 2 – Traitement ou analyse
    print("\n--- Étape 2 : Traitement principal ---")
    resultats = etape2.etape2_main(donnees)

    # Étape 3 – Résultats ou affichage final
    print("\n--- Étape 3 : Résultats ou sortie ---")
    etape3.etape3_main(resultats)

    print("\n=== Fin du programme ===")


if __name__ == "__main__":
    main()
