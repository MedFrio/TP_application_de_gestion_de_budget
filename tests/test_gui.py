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
