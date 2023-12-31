"""
This file contains functions related to interacting with the EnvHub API.

Functions:
    get_var(name): Retrieves the value of a variable from the EnvHub API.
"""
import requests
from requests.exceptions import ConnectionError

def get_var(name):
    """
    Retrieves the value of a variable from the EnvHub API.

    Parameters:
        name (str): The name of the variable to retrieve.

    Returns:
        str: The value of the variable.

    Raises:
        ConnectionError: If the API request fails or returns an error.
    """
    r = requests.get('https://envhub.ryanbaig.vercel.app/api/vars?varName=' + name)
    if r.status_code == 200:
        return r.json()["value"]
    else:
        raise ConnectionError(r.json())