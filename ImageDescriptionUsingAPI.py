from config import HF_API_KEY
import requests, base64, os, re, time
from PIL import Image

URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}", "Content-Type": "application/json"}
MODELS = [
    "Qwen/Qwen3-VL-8B-Instruct",
    "Qwen/Qwen3-VL-32B-Instruct",
    "Qwen/Qwen2.5-VL-32B-Instruct",
    "Qwen/Qwen2-VL-7B-Instruct"
]

def encode(path):
    return base64.b64encode(open(path, "rb").read()).decode()

img_path = input("Image Path:") or "test.jpg"

try:
    img = encode(img_path)
except:
    print("❌ File not found")
    exit()

for model in MODELS:
    payload = {
        "model": model,
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this image briefly"},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img}"}}
            ]
        }],
        "max_tokens": 100
    }

    r = requests.post(URL, headers=HEADERS, json=payload)

    if r.status_code == 200:
        try:
            cap = r.json()["choices"][0]["message"]["content"]
            if cap:
                print(f"✅ ({model})",cap)
                break
        except:
            pass
    else:
        print(f"❌ ({model})",r.text)
else:
    print("❌ All models failed")
