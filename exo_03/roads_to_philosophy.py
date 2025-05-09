import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, urljoin

WIKI_BASE_URL = "https://en.wikipedia.org"
PHILOSOPHY_URL = "/wiki/Philosophy"


def get_first_valid_link(soup):
    content_div = soup.find(id="mw-content-text")
    if not content_div:
        return None

    paragraphs = content_div.find_all("p", recursive=False)
    for para in paragraphs:
        if para.find("a"):
            # Remove all parenthesis
            text = str(para)
            clean_html = ""
            depth = 0
            for char in text:
                if char == '(':
                    depth += 1
                elif char == ')':
                    if depth > 0:
                        depth -= 1
                elif depth == 0:
                    clean_html += char

            clean_soup = BeautifulSoup(clean_html, "html.parser")

            for link in clean_soup.find_all("a"):
                href = link.get("href")
                if href and href.startswith("/wiki/") and not any(
                    invalid in href for invalid in [":", "#"]
                ):
                    return href

    return None


def fetch_page(title):
    try:
        search_url = f"{WIKI_BASE_URL}/wiki/{title.replace(' ', '_')}"
        response = requests.get(search_url)
        if response.status_code != 200:
            print("Error fetching the Wikipedia page.")
            sys.exit(1)
        return response
    except Exception as e:
        print(f"Connection error: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 roads_to_philosophy.py <search term>")
        return

    visited = []
    current_title = sys.argv[1]

    while True:
        response = fetch_page(current_title)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find canonical page title
        title = soup.find("h1").text.strip()

        if title in visited:
            print("It leads to an infinite loop !")
            return

        print(title)
        visited.append(title)

        if response.url.endswith(PHILOSOPHY_URL):
            print(f"{len(visited)} roads from {visited[0]} to philosophy !")
            return

        next_link = get_first_valid_link(soup)
        if not next_link:
            print("It's a dead end !")
            return

        current_title = unquote(next_link.split("/wiki/")[-1])


if __name__ == '__main__':
    main()