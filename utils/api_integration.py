# utils/api_integration.py
import requests
from credentials import API_KEY, BASE_URL

def get_data_from_api(endpoint: str, params: dict = None):
    """
    Makes a GET request to the external API.
    :param endpoint: API endpoint (e.g., "/exercise").
    :param params: Query parameters for the request.
    :return: Response JSON or None if the request fails.
    """
    
    headers = {
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com",
        "X-RapidAPI-Key": API_KEY,  # Replace with your actual RapidAPI key
    }
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", headers=headers, params=params)
        response.raise_for_status()  # Raise an error for HTTP errors
        return response.json()
    except requests.RequestException as e:
        print(f"API Request Error: {e}")
        return None
