# ue19-lab-05
# Projet API & Docker (ue19-lab-05)

Ce projet est un simple script Python qui interroge une API publique (par exemple, JokesAPI) pour afficher une blague aléatoire dans le terminal. Il est conteneurisé avec Docker.

---

## 🚀 Comment l'utiliser (Howto)

Vous avez deux façons de lancer ce programme : localement avec Python, ou via Docker.

### 1. Lancement local (sans Docker)

1.  **Clonez le dépôt :**
    ```bash
    git clone [https://github.com/acaboalexishelmo/ue19-lab-05.git](https://github.com/acaboalexishelmo/ue19-lab-05.git)
    cd ue19-lab-05
    ```

2.  **Installez les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Exécutez le script :**
    ```bash
    python app.py
    ```

### 2. Lancement avec Docker (Recommandé)

Docker doit être installé et en cours d'exécution sur votre machine.

1.  **Construisez l'image Docker :**
    (Le `.` à la fin est important)
    ```bash
    docker build -t app-blague .
    ```

2.  **Exécutez le conteneur :**
    Le conteneur va démarrer, exécuter le script (qui affiche la blague) et s'arrêter.
    ```bash
    docker run app-blague
    ```

---

## 📦 Fichiers du projet

* `app.py`: Le script Python principal qui appelle l'API.
* `requirements.txt`: Les dépendances Python (la librairie `requests`).
* `Dockerfile`: La "recette" pour construire l'image conteneur.
* `README.md`: Ce fichier d'instructions.
