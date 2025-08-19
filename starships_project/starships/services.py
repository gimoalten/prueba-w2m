""" services.py """
import requests

SWAPI_URL = "https://swapi.dev/api/starships/"

def fetch_starship_data(name: str, model: str):
    """
    Busca una nave en SWAPI que coincida por nombre y modelo.
    Devuelve un dict con info extra o None.
    """
    try:
        response = requests.get(SWAPI_URL, params={"search": name}, timeout=5)
        response.raise_for_status()
        data = response.json()
        for starship in data.get("results", []):
            if starship["model"].lower() == model.lower():
                return {
                    "manufacturer": starship.get("manufacturer"),
                    "crew": starship.get("crew"),
                    "length": starship.get("length"),
                }
    except requests.RequestException:
        return None
