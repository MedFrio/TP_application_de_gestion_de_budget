Feature: Calculer la répartition par catégorie
  En tant qu'utilisateur,
  Je veux voir un résumé des dépenses par catégorie
  Pour mieux gérer mon budget.
  
  Scenario: Voir les dépenses par catégorie
    Given un utilisateur avec un solde initial de 1000
    When il ajoute une dépense de 150 dans la catégorie "Alimentaire"
    And il ajoute une dépense de 50 dans la catégorie "Loisirs"
    And il ajoute une dépense de 100 dans la catégorie "Transport"
    Then la répartition des dépenses par catégorie doit être
      | catégorie   | montant |
      | Alimentaire | 150     |
      | Loisirs     | 50      |
      | Transport   | 100     |
