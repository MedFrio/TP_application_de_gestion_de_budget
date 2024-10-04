Feature: Calculer le solde total
  En tant qu'utilisateur,
  Je veux calculer mon solde total
  Pour voir la différence entre mes revenus et mes dépenses.

  Scenario: Calculer le solde total après plusieurs opérations
    Given un utilisateur avec un solde initial de 1000
    When il ajoute une source de revenu de 300
    And il ajoute une dépense de 100 dans la catégorie "Alimentaire"
    And il ajoute une dépense de 200 dans la catégorie "Loisirs"
    Then le solde total doit être de 1000
