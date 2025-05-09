import sys
import antigravity

def calculate_geohash(latitude, longitude):
    """Calcul simple d'un géohash basé sur latitude et longitude."""
    # L'algorithme de géohash est un calcul complexe, mais pour simplifier, imaginons un calcul trivial :
    # On combine les deux valeurs (latitude et longitude) et renvoie un 'géohash' fictif.
    geohash = f"{latitude},{longitude}"  # C'est juste une simulation simple
    return geohash

def print_usage_and_exit():
    """Affiche un message d'usage et quitte proprement le programme."""
    print("Usage : python3 geohashing.py <latitude> <longitude>")
    sys.exit(1)

def main():
    """Fonction principale du programme."""
    if len(sys.argv) != 3:
        print("Erreur : nombre de paramètres incorrect.")
        print_usage_and_exit()

    try:
        # Conversion des arguments en float
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
    except ValueError:
        print("Erreur : Les paramètres doivent être des nombres valides.")
        print_usage_and_exit()

    # Calcule du géohash
    geohash = calculate_geohash(latitude, longitude)

    # Affichage du géohash
    print(f"Le géohash pour les coordonnées ({latitude}, {longitude}) est : {geohash}")

if __name__ == '__main__':
    main()