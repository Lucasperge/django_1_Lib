
import sys
import requests
import json
import dewiki

def get_wikipedia_extract(query):
    url = "https://fr.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "explaintext": True,
        "redirects": 1,
        "titles": query
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        pages = data["query"]["pages"]
        page = next(iter(pages.values()))

        if "extract" not in page or not page["extract"]:
            raise ValueError("Aucun contenu trouvé pour cette recherche.")

        return dewiki.from_string(page["extract"])

    except Exception as e:
        print("Erreur :", e)
        return None

def save_to_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    if len(sys.argv) != 2:
        print("Erreur : Veuillez fournir un seul terme de recherche.")
        return

    query = sys.argv[1]
    cleaned_filename = query.replace(" ", "_") + ".wiki"

    result = get_wikipedia_extract(query)

    if result:
        save_to_file(cleaned_filename, result)

if __name__ == '__main__':
    main()
