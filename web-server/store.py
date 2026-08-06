import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    r.raise_for_status()  # Raise an exception if the request was unsuccessful
    return r.json()
