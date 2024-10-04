import tkinter as tk
from tkinter import messagebox
from budget_manager import BudgetManager

class BudgetManagerApp:
    def __init__(self, root, show_messages=True):
        self.root = root
        self.root.title("Gestionnaire de Budget")
        self.root.geometry("300x400")  # Définit la taille de la fenêtre à 300x400 pixels
        self.manager = BudgetManager()
        self.show_messages = show_messages  # Store the message display preference

        # Ajouter une dépense
        self.label_categorie = tk.Label(root, text="Catégorie de dépense")
        self.label_categorie.pack()
        self.entry_categorie = tk.Entry(root)
        self.entry_categorie.pack()

        self.label_description = tk.Label(root, text="Description de dépense")
        self.label_description.pack()
        self.entry_description = tk.Entry(root)
        self.entry_description.pack()

        self.label_montant_depense = tk.Label(root, text="Montant de la dépense")
        self.label_montant_depense.pack()
        self.entry_montant_depense = tk.Entry(root)
        self.entry_montant_depense.pack()

        self.button_ajouter_depense = tk.Button(root, text="Ajouter Dépense", command=self.ajouter_depense)
        self.button_ajouter_depense.pack()

        # Ajouter un revenu
        self.label_description_revenu = tk.Label(root, text="Description de revenu")
        self.label_description_revenu.pack()
        self.entry_description_revenu = tk.Entry(root)
        self.entry_description_revenu.pack()

        self.label_montant_revenu = tk.Label(root, text="Montant du revenu")
        self.label_montant_revenu.pack()
        self.entry_montant_revenu = tk.Entry(root)
        self.entry_montant_revenu.pack()

        self.button_ajouter_revenu = tk.Button(root, text="Ajouter Revenu", command=self.ajouter_revenu)
        self.button_ajouter_revenu.pack()

        # Calculer solde
        self.button_calculer_solde = tk.Button(root, text="Calculer Solde", command=self.calculer_solde)
        self.button_calculer_solde.pack()

        # Calculer la moyenne des dépenses par catégorie
        self.label_categorie_moyenne = tk.Label(root, text="Catégorie pour calculer la moyenne")
        self.label_categorie_moyenne.pack()
        self.entry_categorie_moyenne = tk.Entry(root)
        self.entry_categorie_moyenne.pack()

        self.button_calculer_moyenne = tk.Button(root, text="Calculer Moyenne", command=self.calculer_moyenne_depenses)
        self.button_calculer_moyenne.pack()

    def show_message(self, title, message):
        if self.show_messages:
            messagebox.showinfo(title, message)  # Show message box if allowed

    def ajouter_depense(self):
        categorie = self.entry_categorie.get()
        description = self.entry_description.get()
        try:
            montant = float(self.entry_montant_depense.get())
            self.manager.ajouter_depense(categorie, description, montant)
            self.show_message("Succès", "Dépense ajoutée avec succès!")
        except ValueError:
            self.show_message("Erreur", "Veuillez entrer un montant valide.")

    def ajouter_revenu(self):
        description = self.entry_description_revenu.get()
        try:
            montant = float(self.entry_montant_revenu.get())
            self.manager.ajouter_revenu(description, montant)
            self.show_message("Succès", "Revenu ajouté avec succès!")
        except ValueError:
            self.show_message("Erreur", "Veuillez entrer un montant valide.")

    def calculer_solde(self):
        solde = self.manager.calculer_solde()
        self.show_message("Solde total", f"Le solde total est: {solde}")

    def calculer_moyenne_depenses(self):
        categorie = self.entry_categorie_moyenne.get()
        try:
            moyenne = self.manager.moyenne_depenses_categorie(categorie)
            self.show_message("Moyenne des dépenses", f"La moyenne des dépenses pour '{categorie}' est: {moyenne}")
        except ZeroDivisionError:
            self.show_message("Erreur", f"Aucune dépense trouvée pour la catégorie '{categorie}'. Division par zéro!")

# Lancer l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetManagerApp(root)
    root.mainloop()
