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
    json={"inputs": {"source_sentence": q1, "sentences": [q2]}},
    timeout=30
    )

    if not response.ok:
        print("Error:",response.text)
        return 0
    
    data = response.json()

    if type(data) == dict:
        print("API Error:",data.get('error'))
        return 0
    
    return float(data[0])

def final_score(q1,q2):
    base = get_similarity(q1, q2)

    words1 = set(clean(q1))
    words2 = set(clean(q2))
    common = words1 & words2

    boost = 0
    penalty = 0

    if len(common) >= 2:
        boost = 0.05
        base += boost

    neg_words = ["not", "no", "never", "don't"]
    if has_any(q1, neg_words) != has_any(q1, neg_words):
        penalty = 0.1
        base -= penalty
    
    final = max(0, min(1, base))

    return final, boost, penalty

def show(score, boost, penalty):
    percent = round(score * 100, 1)

    filled = int(score * 20)
    bar = "█" * filled + "░" * filled

    if score >= THRESHOLD:
        result = "✅DUPLICATE"
    elif score >= THRESHOLD - 0.05:
        result = "🤔CLOSE MATCH"
    else:
        result = "❌DIFFERENT"
    
    print("\n🎯 Similarity Score")
    print(f"[{bar}] {percent}%")
    print("Base + Boost - Penalty = Final")
    print(f"Boost: +{boost} | Penalty: -{penalty}")
    print("Result:",result)

while True:
    q1 = input("\nSentence-1:")
    if q1 == "exit":
        break

    q2 = input("\nSentence-2:")
    if q2 == "exit":
        break

    final, boost, penalty = final_score(q1, q2)
    show(final, boost, penalty)
