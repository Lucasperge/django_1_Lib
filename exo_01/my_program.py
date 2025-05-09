import sys

# Ajouter le chemin vers la librairie installée localement
sys.path.append('./local_lib')

# Importer Path depuis la librairie path.py
from path import Path

def main():
    # 1. Créer un dossier (en utilisant path.py pour gérer le chemin)
    folder = Path("my_folder")
    folder.mkdir_p()  # Crée le dossier même s'il existe déjà

    # 2. Créer un fichier dans ce dossier
    file_path = folder / "my_file.txt"

    # 3. Écrire dans le fichier en utilisant la méthode open de Python standard
    with open(file_path, 'w') as f:
        f.write("Bonjour, ceci est un test de path.py !")

    # 4. Lire et afficher le contenu du fichier
    with open(file_path, 'r') as f:
        content = f.read()
        print("Contenu du fichier :", content)

if __name__ == '__main__':
    main()



