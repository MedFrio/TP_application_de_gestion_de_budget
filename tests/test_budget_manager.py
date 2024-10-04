import sys
import os

# Met à jour le chemin du système pour inclure le répertoire parent
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.', '..')))

import unittest
from budget_manager import BudgetManager

class TestBudgetManager(unittest.TestCase):

    def setUp(self):
        # Initialise une instance de BudgetManager pour chaque test
        self.manager = BudgetManager()

    def test_ajouter_depense(self):
        # Teste l'ajout d'une dépense
        self.manager.ajouter_depense("Alimentaire", "Achat de légumes", 50)
        self.assertEqual(len(self.manager.depenses), 1)  # Vérifie qu'une dépense a été ajoutée
        self.assertEqual(self.manager.depenses[0]['montant'], 50)  # Vérifie le montant de la dépense

    def test_ajouter_revenu(self):
        # Teste l'ajout d'un revenu
        self.manager.ajouter_revenu("Salaire", 1000)
        self.assertEqual(len(self.manager.revenus), 1)  # Vérifie qu'un revenu a été ajouté
        self.assertEqual(self.manager.revenus[0]['montant'], 1000)  # Vérifie le montant du revenu

    def test_calculer_solde(self):
        # Teste le calcul du solde après avoir ajouté une dépense et un revenu
        self.manager.ajouter_depense("Alimentaire", "Achat de légumes", 50)
        self.manager.ajouter_revenu("Salaire", 1000)
        solde = self.manager.calculer_solde()  # Calcule le solde
        self.assertEqual(solde, 950)  # Vérifie que le solde est correct

    def test_moyenne_depenses_categorie(self):
        # Teste le calcul de la moyenne des dépenses dans une catégorie
        self.manager.ajouter_depense("Transport", "Ticket de bus", 10)
        self.manager.ajouter_depense("Transport", "Essence", 40)
        moyenne = self.manager.moyenne_depenses_categorie("Transport")  # Calcule la moyenne
        self.assertEqual(moyenne, 25)  # Vérifie que la moyenne est correcte

    '''def test_moyenne_depenses_categorie_division_zero(self):
        # Test pour la division par zéro (aucune dépense dans la catégorie)
        with self.assertRaises(ZeroDivisionError):
            self.manager.moyenne_depenses_categorie("Voyages")'''

    def test_moyenne_depenses_categorie_avec_aucune_depense(self):
        # Test après la correction de l'erreur (aucune dépense)
        moyenne = self.manager.moyenne_depenses_categorie("Inconnue")  # Calcule la moyenne pour une catégorie inconnue
        self.assertEqual(moyenne, 0)  # Vérifie que la moyenne est 0

if __name__ == '__main__':
    unittest.main()  # Exécute les tests
