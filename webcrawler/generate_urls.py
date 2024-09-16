import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def generate_urls_from_duckduckgo(keywords, max_results=10):
    """
    Generate search result URLs using DuckDuckGo based on provided keywords.
    """
    base_url = 'https://html.duckduckgo.com/html/'
    urls = []

    for keyword in keywords:
        query = quote_plus(keyword)
        search_url = f'{base_url}?q={query}'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

        try:
            response = requests.get(search_url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract search result URLs
            for link in soup.find_all('a', {'class': 'result__a'}, limit=max_results):
                url = link.get('href')
                if url:
                    urls.append(url)
        except Exception as e:
            print(f"Failed to fetch URLs for {keyword}: {e}")

    return urls
