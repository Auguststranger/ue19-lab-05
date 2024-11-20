# Application JokesAPI de Blagues

Cette application interroge le service JokesAPI pour afficher une blague.

## Fonctionnalités
- Affiche une blague aléatoire (type "single" ou "twopart") récupérée depuis JokeAPI.
- Facile à exécuter via Python ou un conteneur Docker.

## Installation et utilisation 

Clonez le repository et naviguez dans le répertoire :
```bash
git clone https://github.com/Auguststranger/ue19-lab-05.git
cd ue19-lab-05
```

### Methode 1: Execution avec Python

#### Prérequis:
- Python 3.9 ou version ulterieure
- Pip installer
#### Etapes
- Installez les dépendances:
```bash
pip install -r requirements.txt
```
-lancer le programme:
```bash
python app.py
```

### Methode 1: Execution avec Docker
#### Prérequis :
- Docker installé
#### Étapes :
- Construire l'image Docker:
```bash
docker build -t jokes-api-app .
```
- Executer le conteneur:
```bash
docker run jokes-api-app
```
## Fichiers inclus
- app.py : Le programme principal qui interroge l'API et affiche une blague.
- requirements.txt : Liste des dépendances Python nécessaires.
- Dockerfile : Configuration pour créer l'image Docker.
- README.md : Ce fichier de documentation.

## Dépendance

- python 3.9
- requests
