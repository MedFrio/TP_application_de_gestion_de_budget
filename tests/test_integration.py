import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.', '..')))



# test_integration.py

import pytest
from budget_manager import BudgetManager

def test_ajouter_depense_mise_a_jour_solde():
    manager = BudgetManager()
    manager.ajouter_revenu("Initial Balance", 1000)  # Solde initial
    manager.ajouter_depense("Alimentaire", "Achat de nourriture", 200)  # Ajouter une dépense

    solde_total = manager.calculer_solde()  # Calculer le solde
    assert solde_total == 800  # Vérifier que le solde est mis à jour correctement

def test_multiple_depenses_mise_a_jour_solde():
    manager = BudgetManager()
    manager.ajouter_revenu("Salaire", 2000)
    
    # Ajouter plusieurs dépenses
    manager.ajouter_depense("Loisirs", "Sortie au cinéma", 50)
    manager.ajouter_depense("Transport", "Achat de ticket de train", 30)
    manager.ajouter_depense("Alimentaire", "Courses", 100)

    solde_total = manager.calculer_solde()
    assert solde_total == 1820  # Vérifier que le solde est correct après les dépenses
