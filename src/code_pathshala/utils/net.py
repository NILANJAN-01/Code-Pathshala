"""
Network helpers using the requests library.
"""
import requests
from typing import Any

DEFAULT_TIMEOUT = 10

def get_json(url: str) -> dict[str, Any]:
    """Send GET request and return JSON response."""
    response = requests.get(url, timeout=DEFAULT_TIMEOUT, headers={"Accept": "application/json"})
    response.raise_for_status()
    return response.json()
