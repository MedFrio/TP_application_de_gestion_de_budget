Feature: Ajouter une source de revenu
  En tant qu'utilisateur,
  Je veux ajouter une source de revenu
  Pour voir comment cela affecte mon budget.

  Scenario: Ajouter une source de revenu et vérifier l'impact
    Given un utilisateur avec un solde initial de 1000
    When il ajoute une source de revenu de 200
    Then le solde total doit être de 1200
