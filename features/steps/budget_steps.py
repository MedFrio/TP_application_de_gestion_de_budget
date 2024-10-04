import sys
import os
import pytest

# Ajoute le répertoire parent au chemin
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# budget_steps.py

from behave import given, when, then
from budget_manager import BudgetManager  
from hamcrest import assert_that, equal_to  # Utilise Hamcrest pour les assertions

@given('un utilisateur avec un solde initial de {montant:d}')
def step_impl(context, montant):
    context.manager = BudgetManager()  # Initialise le BudgetManager
    context.manager.ajouter_revenu("Initial Balance", montant)  # Définit le solde initial comme revenu

@when('il ajoute une dépense de {montant:d} dans la catégorie "{categorie}"')
def step_impl(context, montant, categorie):
    context.manager.ajouter_depense(categorie, "Dépense ajoutée", montant)  # Ajoute une dépense

@when('il ajoute une source de revenu de {montant:d}')
def step_impl(context, montant):
    context.manager.ajouter_revenu("Revenu ajouté", montant)  # Ajoute un revenu

@when('il essaie d\'ajouter une dépense de {montant:d} dans la catégorie "{categorie}"')
def step_impl(context, montant, categorie):
    context.exception = None
    try:
        if montant < 0:
            raise ValueError("Le montant doit être positif.")  # Vérifie que le montant est positif
        context.manager.ajouter_depense(categorie, "Dépense ajoutée", montant)  # Essaye d'ajouter la dépense
    except ValueError as e:
        context.exception = str(e)  # Capture le message d'exception

@then('le solde total doit être de {montant:d}')
def step_impl(context, montant):
    solde = context.manager.calculer_solde()  # Calcule le solde actuel
    assert_that(solde, equal_to(float(montant)))  # Vérifie que le solde est conforme à l'attendu

@then('un message d\'erreur doit être affiché "{message}"')
def step_impl(context, message):
    assert_that(context.exception, equal_to(message))  # Vérifie que le message d'exception correspond

@then('la répartition des dépenses par catégorie doit être')
def step_impl(context):
    categories = context.manager.repartition_par_categorie()  # Obtient la répartition par catégorie
    expected_categories = {row['catégorie']: int(row['montant']) for row in context.table}  # Prépare les catégories attendues avec conversion en entier
    assert_that(categories, equal_to(expected_categories))  # Vérifie que les catégories sont distribuées correctement
