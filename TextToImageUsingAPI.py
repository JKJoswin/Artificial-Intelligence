from huggingface_hub import InferenceClient
from datetime import datetime
from PIL import Image
from config import HF_API_KEY

MODELS = [
    "ByteDance/SDXL-Lightning",
    "stabilityai/stable-diffusion-xl-base-1.0",
    "stabilityai/sdxl-turbo",
    "runwaym/stable-diffusion-v1-5",
]

