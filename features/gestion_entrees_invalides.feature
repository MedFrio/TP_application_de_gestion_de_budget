Feature: Gérer les entrées invalides
  En tant qu'utilisateur,
  Je veux que l'application gère les entrées invalides
  Pour éviter les erreurs dans la gestion de mon budget.

  Scenario: Ajouter une dépense avec un montant négatif
    Given un utilisateur avec un solde initial de 1000
    When il essaie d'ajouter une dépense de -50 dans la catégorie "Alimentaire"
    Then un message d'erreur doit être affiché "Le montant doit être positif."
