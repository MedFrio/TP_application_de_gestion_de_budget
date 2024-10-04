import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.', '..')))




import pytest
from budget_manager import BudgetManager



# Tests fonctionnels pour le BudgetManager
def test_ajouter_depense_et_verifier_solde():
    manager = BudgetManager()
    manager.ajouter_revenu("Initial Balance", 1000)  # Solde initial

    manager.ajouter_depense("Alimentaire", "Dépense repas", 100)
    
    solde = manager.calculer_solde()  # Vérification du solde
    assert solde == 900, "Le solde devrait être de 900 après la dépense."

def test_ajouter_revenu_et_verifier_solde():
    manager = BudgetManager()
    manager.ajouter_revenu("Initial Balance", 1000)  # Solde initial

    manager.ajouter_revenu("Bonus", 200)  # Ajouter une source de revenu
    solde = manager.calculer_solde()  # Vérification du solde
    assert solde == 1200, "Le solde devrait être de 1200 après l'ajout du revenu."

def test_calculer_repartition_par_categorie():
    manager = BudgetManager()
    manager.ajouter_revenu("Initial Balance", 1000)  # Solde initial
    manager.ajouter_depense("Alimentaire", "Dépense repas", 150)
    manager.ajouter_depense("Loisirs", "Dépense cinéma", 50)
    manager.ajouter_depense("Transport", "Dépense bus", 100)

    repartition = manager.repartition_par_categorie()
    expected_repartition = {
        "Alimentaire": 150,
        "Loisirs": 50,
        "Transport": 100
    }
    
    assert repartition == expected_repartition, "La répartition par catégorie ne correspond pas aux attentes."
