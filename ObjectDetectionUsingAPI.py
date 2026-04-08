import os, io, time, random, requests, mimetypes
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from config import HF_API_KEY

MODEL = "facebook/detr-resnet-101"
API = f"https://router.huggingface.co/hf-inference/models/{MODEL}"
ALLOWED, MAX_MB = {".jpg",".jpeg",".png",".bmp",".gif",".webp",".tiff"}, 8
EMOJI = {"person":"🧍","car":"🚗","truck":"🚚","bus":"🚌","bicycle":"🚲","motorcycle":"🏍️","dog":"🐶","cat":"🐱","bird":"🐦","horse":"🐴","sheep":"🐑","cow":"🐮","bear":"🐻","giraffe":"🦒","zebra":"🦓","banana":"🍌","apple":"🍎","orange":"🍊","pizza":"🍕","broccoli":"🥦","book":"📘","laptop":"💻","tv":"📺","bottle":"🧴","cup":"🥤"}

def font(sz=18):
    for f in ("DejaVuSans.ttf","arial.ttf"):
        try: return ImageFont.truetype(f, sz)
        except: pass
    return ImageFont.load_default()

def ask_image():
    print("\n🎯 Pick an image (JPG/PNG/WebP/BMP/TIFF ≤ 8MB) from this folder.")
    while True:
        