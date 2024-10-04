import unittest
from budget_manager import BudgetManager

class TestBudgetManager(unittest.TestCase):

    def setUp(self):
        self.manager = BudgetManager()

    def test_ajouter_depense(self):
        self.manager.ajouter_depense("Alimentaire", "Achat de légumes", 50)
        self.assertEqual(len(self.manager.depenses), 1)
        self.assertEqual(self.manager.depenses[0]['montant'], 50)

    def test_ajouter_revenu(self):
        self.manager.ajouter_revenu("Salaire", 1000)
        self.assertEqual(len(self.manager.revenus), 1)
        self.assertEqual(self.manager.revenus[0]['montant'], 1000)

    def test_calculer_solde(self):
        self.manager.ajouter_depense("Alimentaire", "Achat de légumes", 50)
        self.manager.ajouter_revenu("Salaire", 1000)
        solde = self.manager.calculer_solde()
        self.assertEqual(solde, 950)

    def test_moyenne_depenses_categorie(self):
        self.manager.ajouter_depense("Transport", "Ticket de bus", 10)
        self.manager.ajouter_depense("Transport", "Essence", 40)
        moyenne = self.manager.moyenne_depenses_categorie("Transport")
        self.assertEqual(moyenne, 25)

    '''def test_moyenne_depenses_categorie_division_zero(self):
        # Test pour la division par zéro (aucune dépense dans la catégorie)
        with self.assertRaises(ZeroDivisionError):
            self.manager.moyenne_depenses_categorie("Voyages")'''

    def test_moyenne_depenses_categorie_avec_aucune_depense(self):
        # Test après la correction de l'erreur (aucune dépense)
        moyenne = self.manager.moyenne_depenses_categorie("Inconnue")
        self.assertEqual(moyenne, 0)

if __name__ == '__main__':
    unittest.main()
