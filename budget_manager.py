# budget_manager.py

class BudgetManager:
    def __init__(self):
        self.depenses = []
        self.revenus = []

    # Ajouter une dépense
    def ajouter_depense(self, categorie, description, montant):
        self.depenses.append({
            'categorie': categorie,
            'description': description,
            'montant': montant
        })

    # Ajouter une source de revenu
    def ajouter_revenu(self, description, montant):
        self.revenus.append({
            'description': description,
            'montant': montant
        })

    # Calculer le solde total
    def calculer_solde(self):
        total_depenses = sum([d['montant'] for d in self.depenses])
        total_revenus = sum([r['montant'] for r in self.revenus])
        return total_revenus - total_depenses

    # Calculer la répartition par catégorie
    def repartition_par_categorie(self):
        repartition = {}
        for depense in self.depenses:
            categorie = depense['categorie']
            montant = depense['montant']
            if categorie not in repartition:
                repartition[categorie] = 0
            repartition[categorie] += montant
        return repartition

    # Calculer la moyenne des dépenses pour une catégorie donnée
    def moyenne_depenses_categorie(self, categorie):
        depenses_categorie = [d['montant'] for d in self.depenses if d['categorie'] == categorie]
        
        if len(depenses_categorie) == 0:
            return 0  # Retourne 0 au lieu de provoquer une division par zéro
        
        total = sum(depenses_categorie)
        moyenne = total / len(depenses_categorie)
        return moyenne
