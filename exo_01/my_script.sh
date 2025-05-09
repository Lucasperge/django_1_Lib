#!/bin/bash

# 1. Affiche la version de pip
pip3 --version

# 2. Installe path.py depuis GitHub dans le dossier local_lib
#    et enregistre les logs dans install.log
pip3 install --target=./local_lib git+https://github.com/jaraco/path.git > install.log 2>&1

# 3. Vérifie si l'installation a réussi (code retour = 0)
if [ $? -eq 0 ]; then
    echo "Installation réussie, exécution du programme Python..."
    python3 my_program.py
else
    echo "Erreur : l'installation de path.py a échoué. Vérifiez install.log pour plus de détails."
fi

