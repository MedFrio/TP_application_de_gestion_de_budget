import sys
import os
import pytest
import tkinter as tk

# Update the system path to include the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.', '..')))

from gui_budget_manager import BudgetManagerApp

@pytest.fixture
def gui():
    root = tk.Tk()  # Initialize the Tkinter root
    root.withdraw()  # Hide the main window
    gui_app = BudgetManagerApp(root, show_messages=False)  # Create the BudgetManagerApp instance without showing messages
    yield gui_app  # Yield the GUI instance for testing
    root.destroy()  # Clean up the Tkinter window after the test

def test_gui_initialization(gui):
    assert gui is not None  # Ensure the GUI is initialized

def test_add_expense(gui):
    gui.manager.ajouter_revenu("Initial Balance", 1000)  # Set the initial balance
    gui.entry_categorie.insert(0, 'Food')  # Set category in the GUI entry
    gui.entry_description.insert(0, 'Lunch')  # Set description in the GUI entry
    gui.entry_montant_depense.insert(0, '100')  # Set amount in the GUI entry
    gui.button_ajouter_depense.invoke()  # Simulate clicking the "Add Expense" button
    assert gui.manager.calculer_solde() == 900  # Check that the balance is updated correctly


def test_add_income(gui):
    gui.manager.ajouter_revenu("Initial Balance", 1000)  # Set the initial balance
    gui.entry_description_revenu.insert(0, 'Salary')  # Set description in the GUI entry
    gui.entry_montant_revenu.insert(0, '500')  # Set amount in the GUI entry
    gui.button_ajouter_revenu.invoke()  # Simulate clicking the "Add Income" button
    assert gui.manager.calculer_solde() == 1500  # Check that the balance is updated correctly

def test_calculate_balance(gui):
    gui.manager.ajouter_revenu("Initial Balance", 1000)  # Set the initial balance
    gui.manager.ajouter_depense("Food", "Lunch", 100)  # Add an expense
    gui.calculer_solde()  # Invoke the calculation of balance
    assert gui.manager.calculer_solde() == 900  # Check the balance

def test_calculate_average_expenses(gui):
    gui.manager.ajouter_depense("Food", "Lunch", 100)  # Add an expense
    gui.manager.ajouter_depense("Food", "Dinner", 200)  # Add another expense
    gui.entry_categorie_moyenne.insert(0, 'Food')  # Set the category in the GUI entry
    gui.calculer_moyenne_depenses()  # Invoke the average calculation
    assert gui.manager.moyenne_depenses_categorie("Food") == 150.0  # Check the average is correct

def test_calculate_average_expenses_no_expenses(gui):
    gui.entry_categorie_moyenne.insert(0, 'Nonexistent Category')  # Set a nonexistent category
    gui.calculer_moyenne_depenses()  # Invoke the average calculation
    # Check that it raises an exception
