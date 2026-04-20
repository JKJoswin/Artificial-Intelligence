from config import HF_API_KEY
import requests, base64

URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}
MODELS = [
    "Qwen/Qwen3-VL-8B-Instruct",
    "Qwen/Qwen2-VL-7B-Instruct"
]

def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def get_prompt(choice):
    if choice=="1":
        return "Give a caption for this image"
    elif choice=="2":
        return "Describe this image in one short sentence"
    elif choice=="3":
        return "Decribe this image in detail"
    else:
        return None

img_path = input("Enter image path:") or "test.jpg"

try:
    img_data = encode_image(img_path)
except:
    print("❌ Image not found")
    exit()

while True:
    print("\n--- MENU ---")
    print("1.Caption")
    print("2.Short Text")
    print("3.Long Text")
    print("4.Exit")

    choice = input("Select option:")

    if choice == "4":
        print("👋 Exiting...")
        break

    prompt = get_prompt(choice)

    if not prompt:
        print("❌ Invalid choice")
        continue

    for model in MODELS:
        payload = {
            "model":model,
            "messages":[{
                "role":"user",
                "context":[
                    {"type":"text","text":prompt},
                    {"type":"image_url",
                     "image_url":{"url":f"data:image/jpeg;base64,{img_data}"}}
                ]
            }]
        }

        response = requests.post(URL, headers=HEADERS, json=payload)
        if response.status_code == 200:
            try:
                result = response.json()["choices"][0]["message"]["content"]
                print(f"\n✅ Result ({model}):\n{result}")
                break
            except:
                print("⚠️ Error reading response")
        else:    
            print(f"❌ Failed: {model}")
        
    else:print("❌ All models failed")