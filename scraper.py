import requests


def fetch_page(url, headers=None):
    default_headers = {"User-Agent": "Mozilla/5.0"}
    if headers:
        default_headers.update(headers)
    response = requests.get(url, headers=default_headers, timeout=10)
    response.raise_for_status()
    return response.text

from bs4 import BeautifulSoup


def parse_html(html):
    return BeautifulSoup(html, 'html.parser')


def extract_links(soup, base_url=""):
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.startswith('/') and base_url:
            href = base_url.rstrip('/') + href
        links.append({"text": a.get_text(strip=True), "url": href})
    return links


def extract_headings(soup):
    headings = []
    for tag in ['h1', 'h2', 'h3', 'h4']:
        for h in soup.find_all(tag):
            headings.append({"level": tag, "text": h.get_text(strip=True)})
    return headings
