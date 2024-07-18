import requests


def fetch_page(url, headers=None):
    default_headers = {"User-Agent": "Mozilla/5.0"}
    if headers:
        default_headers.update(headers)
    response = requests.get(url, headers=default_headers, timeout=10)
    response.raise_for_status()
    return response.text
