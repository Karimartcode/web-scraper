import time
import requests
from typing import Optional


def fetch_with_retry(url: str, max_retries: int = 3,
                     backoff: float = 2.0,
                     timeout: int = 10) -> Optional[requests.Response]:
    """Fetch URL with exponential backoff retry."""
    for attempt in range(max_retries):
        try:
            resp = requests.get(url, timeout=timeout,
                                headers={"User-Agent": "Mozilla/5.0"})
            resp.raise_for_status()
            return resp
        except requests.RequestException as e:
            wait = backoff ** attempt
            print(f"Attempt {attempt+1} failed: {e}. Retrying in {wait:.1f}s...")
            time.sleep(wait)
    return None
