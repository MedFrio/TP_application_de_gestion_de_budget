from behave import given, when, then
from budget_manager import BudgetManager
from hamcrest import assert_that, equal_to

@given('un utilisateur avec un solde initial de {montant}')
def step_impl(context, montant):
    context.manager = BudgetManager()
    context.manager.ajouter_revenu("Salaire", float(montant))

@when('il ajoute une dépense de {montant} dans la catégorie "{categorie}"')
def step_impl(context, montant, categorie):
    context.manager.ajouter_depense(categorie, "Achat", float(montant))

@then('le solde total doit être de {montant}')
def step_impl(context, montant):
    solde = context.manager.calculer_solde()
    assert_that(solde, equal_to(float(montant)))
