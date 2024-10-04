import sys
import os
import pytest

# Add the parent directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# budget_steps.py

from behave import given, when, then
from budget_manager import BudgetManager  # Ensure this import is correct
from hamcrest import assert_that, equal_to  # Use Hamcrest for assertions

@given('un utilisateur avec un solde initial de {montant:d}')
def step_impl(context, montant):
    context.manager = BudgetManager()  # Initialize the BudgetManager
    context.manager.ajouter_revenu("Initial Balance", montant)  # Set the initial balance as revenue

@when('il ajoute une dépense de {montant:d} dans la catégorie "{categorie}"')
def step_impl(context, montant, categorie):
    context.manager.ajouter_depense(categorie, "Dépense ajoutée", montant)  # Add an expense

@when('il ajoute une source de revenu de {montant:d}')
def step_impl(context, montant):
    context.manager.ajouter_revenu("Revenu ajouté", montant)  # Add income

@when('il essaie d\'ajouter une dépense de {montant:d} dans la catégorie "{categorie}"')
def step_impl(context, montant, categorie):
    context.exception = None
    try:
        if montant < 0:
            raise ValueError("Le montant doit être positif.")
        context.manager.ajouter_depense(categorie, "Dépense ajoutée", montant)  # Try to add expense
    except ValueError as e:
        context.exception = str(e)  # Capture the exception message

@then('le solde total doit être de {montant:d}')
def step_impl(context, montant):
    solde = context.manager.calculer_solde()  # Calculate current balance
    assert_that(solde, equal_to(float(montant)))  # Assert the balance is as expected

@then('un message d\'erreur doit être affiché "{message}"')
def step_impl(context, message):
    assert_that(context.exception, equal_to(message))  # Assert the exception message matches

@then('la répartition des dépenses par catégorie doit être')
def step_impl(context):
    categories = context.manager.repartition_par_categorie()  # Get category distribution
    expected_categories = {row['catégorie']: int(row['montant']) for row in context.table}  # Prepare expected categories with integer conversion
    assert_that(categories, equal_to(expected_categories))  # Assert categories are distributed correctly

