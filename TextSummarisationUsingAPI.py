import requests
from config import HF_API_KEY
from colorama import Fore, Style, init

init(autoreset=True)


DEFAULT_MODEL = "google/pegasus-xsum"

def build_api_url(model_name):
    return f"https://router.huggingface.co/hf-inference/models/{model_name}"

def query(payload, model_name = DEFAULT_MODEL):
    api_url = build_api_url(model_name)
    headers = {"Authorization":f"Bearer {HF_API_KEY}"}
    response = requests.post(api_url, headers=headers, json=payload)

    return response.json()