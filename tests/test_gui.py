import sys
import os
import pytest
import tkinter as tk

# Met à jour le chemin du système pour inclure le répertoire parent
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.', '..')))

from gui_budget_manager import BudgetManagerApp

@pytest.fixture
def gui():
    root = tk.Tk()  # Initialise la racine Tkinter
    root.withdraw()  # Masque la fenêtre principale
    gui_app = BudgetManagerApp(root, show_messages=False)  # Crée une instance de BudgetManagerApp sans afficher de messages
    yield gui_app  # Rend l'instance GUI pour les tests
    root.destroy()  # Nettoie la fenêtre Tkinter après le test

def test_gui_initialization(gui):
    assert gui is not None  # Vérifie que la GUI est initialisée

def test_add_expense(gui):
    gui.manager.ajouter_revenu("Initial Balance", 1000)  # Définit le solde initial
    gui.entry_categorie.insert(0, 'Food')  # Définit la catégorie dans l'entrée de la GUI
    gui.entry_description.insert(0, 'Lunch')  # Définit la description dans l'entrée de la GUI
    gui.entry_montant_depense.insert(0, '100')  # Définit le montant dans l'entrée de la GUI
    gui.button_ajouter_depense.invoke()  # Simule le clic sur le bouton "Ajouter Dépense"
    assert gui.manager.calculer_solde() == 900  # Vérifie que le solde est mis à jour correctement

def test_calculate_average_expenses_no_expenses(gui):
    gui.entry_categorie_moyenne.insert(0, 'Nonexistent Category')  # Définit une catégorie inexistante
    gui.calculer_moyenne_depenses()  # Invoque le calcul de la moyenne
