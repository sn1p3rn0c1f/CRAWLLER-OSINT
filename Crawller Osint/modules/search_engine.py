import requests
from bs4 import BeautifulSoup
import urllib.parse
import time

HEADERS = {'User-Agent': 'Mozilla/5.0'}

SEARCH_ENGINES = {
    "Google": "https://www.google.com/search?q={query}&num=10",
    "Bing": "https://www.bing.com/search?q={query}"
}

DORKS = [
    'site:linkedin.com/in/',
    'site:twitter.com',
    'site:facebook.com',
    'site:github.com',
    'filetype:pdf',
    'site:pinterest.com',
    'site:about.me',
    'site:medium.com',
]

def generate_queries(first_name, last_name):
    """Génère les requêtes dorks avec nom + prénom"""
    base_query = f'"{first_name} {last_name}"'
    queries = [f'{base_query} {dork}' for dork in DORKS]
    return queries

def scrape_search_results(engine_url, query):
    """Scrape les résultats d’un moteur de recherche"""
    encoded_query = urllib.parse.quote_plus(query)
    search_url = engine_url.format(query=encoded_query)

    try:
        response = requests.get(search_url, headers=HEADERS, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []

        for a in soup.find_all('a', href=True):
            href = a['href']
            if "http" in href and not href.startswith('/'):
                links.append(href)

        return links

    except Exception as e:
        return [f"Error: {str(e)}"]

def search_name(first_name, last_name):
    """Lance la recherche sur tous les moteurs avec les dorks"""
    queries = generate_queries(first_name, last_name)
    all_results = {}

    for engine, url_template in SEARCH_ENGINES.items():
        print(f"\n[+] Searching on {engine}...")
        all_results[engine] = []

        for query in queries:
            print(f"    - Query: {query}")
            results = scrape_search_results(url_template, query)
            all_results[engine].extend(results)
            time.sleep(2)  

    return all_results
