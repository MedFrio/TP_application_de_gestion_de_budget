# TP_application_de_gestion_de-_budget
Sujet de TP : Développement d'une Application de Gestion de  Budget avec Intégration de Tests Complets


## Contexte
Vous allez développer une application de gestion de budget très simple. 
L'objectif est de vous familiariser avec les différentes approches de tests 
(unitaires, d'intégration, fonctionnels) ainsi que les méthodologies TDD et BDD. 
Vous devrez également configurer une pipeline de CI/CD utilisant GitLab CI ou 
Github Actions,  pour automatiser l'exécution des tests et la vérification de la 
couverture de code.


# Application de Gestion de Budget

Cette application permet de gérer un budget personnel, avec une interface graphique pour faciliter les interactions. Ce document fournit des instructions sur la façon d'exécuter l'application et les tests.

## Prérequis

Assurez-vous d'avoir Python 3.10 ou une version ultérieure installé sur votre machine. Vous aurez également besoin de `pip` pour installer les dépendances.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository
   ```


2. Créez un environnement virtuel :
  ```bash
   python -m venv venv
```
3.Activez l'environnement virtuel :
sur Windows :
  ```bash
  venv\Scripts\activate
```
sur macOS/Linux :
  ```bash
  source venv/bin/activate
```
4. Installez les dépendances :

  ```bash
  pip install -r requirements.txt
```

# Exécution de l'application
## Pour exécuter l'application, utilisez la commande suivante :

  ```bash
  python gui_budget_manager.py
```
# Exécution des tests
## Pour exécuter les tests unitaires et générer un rapport de couverture, utilisez la commande suivante :
  ```bash
  pytest --cov=. --cov-report=xml:coverage/coverage.xml --cov-report=html:coverage/htmlcov tests
```
## Pour exécuter simplement les tests de comportement, utilisez :
  ```bash
  behave features/
```

# Intégration Continue
## Le fichier de configuration pour GitHub Actions est situé dans le répertoire .github/workflows. Cela permet d'exécuter automatiquement les tests lors des pushs ou des pull requests sur la branche principale.
