import requests
import base64

API_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {
    "Authorization": "HF_API_KEY",
    "Content-Type": "application/json"
}
MODEL = "Qwen/Qwen2-VL-7B-Instruct:together"

def encode_image(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def caption_image():