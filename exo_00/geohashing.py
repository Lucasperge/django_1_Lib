import sys
sys.path.append('./local_lib')

from path import Path

def main():
    # 1. Créer un dossier
    folder = Path("my_folder")
    folder.mkdir_p()

    # 2. Créer un fichier dans ce dossier
    file_path = folder / "my_file.txt"

    # 3. Écrire dans le fichier (avec méthode standard)
    with open(file_path, 'w') as f:
        f.write("Bonjour, ceci est un test de path.py !")

    # 4. Lire et afficher le contenu
    with open(file_path, 'r') as f:
        content = f.read()
        print("Contenu du fichier :", content)

if __name__ == '__main__':
    main()


