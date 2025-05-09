#!/bin/bash

# Créer un environnement virtuel
python3 -m venv django_venv

# Activer l'environnement virtuel
source django_venv/bin/activate

# Installer les dépendances à partir du fichier requirements.txt
pip install -r requirements.txt

# Afficher un message pour indiquer que l'environnement est prêt
echo "L'environnement virtuel est créé et les dépendances sont installées."

# Laisser l'utilisateur dans l'environnement virtuel
echo "L'environnement virtuel django_venv est activé. Vous pouvez maintenant travailler sur votre projet Django."

# Fin du script
