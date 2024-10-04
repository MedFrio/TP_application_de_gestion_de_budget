Feature: Gestion du budget

  En tant qu'utilisateur,
  Je veux ajouter une dépense
  Pour voir comment cela affecte mon budget.

  Scenario: Ajouter une dépense et vérifier l'impact sur le budget
    Given un utilisateur avec un solde initial de 1000
    When il ajoute une dépense de 100 dans la catégorie "Alimentaire"
    Then le solde total doit être de 900
