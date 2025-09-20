import os

from dotenv import load_dotenv

def load_api_key():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    return api_key