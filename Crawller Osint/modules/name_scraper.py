import requests
from bs4 import BeautifulSoup
import urllib.parse

HEADERS = {'User-Agent': 'Mozilla/5.0'}

SEARCH_ENGINES = {
    "Google": "https://www.google.com/search?q={}",
    "Bing": "https://www.bing.com/search?q={}"
}

DORKS = [
    'site:linkedin.com/in/',
    'site:twitter.com',
    'site:facebook.com',
    'site:github.com',
    'filetype:pdf',
    'site:pinterest.com'
]

def search_name(first_name, last_name):
    query_base = f'"{first_name} {last_name}"'
    results = {}

    for engine, base_url in SEARCH_ENGINES.items():
        results[engine] = []
        for dork in DORKS:
            query = f'{query_base} {dork}'
            encoded_query = urllib.parse.quote_plus(query)
            search_url = base_url.format(encoded_query)
            print(f"[{engine}] Searching: {query}")
            try:
                response = requests.get(search_url, headers=HEADERS, timeout=5)
                soup = BeautifulSoup(response.text, 'html.parser')

                for link in soup.find_all('a'):
                    href = link.get('href')
                    if href and 'http' in href:
                        results[engine].append(href)
            except Exception as e:
                results[engine].append(f"Error: {str(e)}")
    
    return results
