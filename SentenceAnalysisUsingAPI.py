import requests, re, random
from config import HF_API_KEY

MODEL="sentence-transformers/all-MiniLM-L6-v2"
API=f"https://router.huggingface.co/hf-inference/models/{MODEL}"
HEAD={"Authorization":f"Bearer {HF_API_KEY}"}
THRESHOLD = 0.72

clean = lambda t:[w for w in (re.sub(r"[^a-z0-9]+", "", x.lower()) for x in t.split()) if w]
has_any = lambda t,arr:any(a in set(clean(t)) for a in arr)

def get_similarity(q1, q2):
    response = requests.post(
        API,
        headers=HEAD,
        json = {"input": {"source_sentence":q1, "sentences":[q2]}},
        timeout=30
    )