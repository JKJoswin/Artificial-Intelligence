from googletrans import Translator
from gtts import gTTS
from playsound import playsound

languages = {
    "1":("Hindi", "hi"),
    "2":("Tamil", "ta"),
    "3":("Telugu","te"),
    "4":("Bengali","bn"),
    "5":("Marathi ","mr"),
    "6":("Gujarati" ,"gu"),
    "7":("Malayalam" ,"ml"),
    "8":("Punjabi" ,"pa"),
    "9":("Spanish" ,"es"),
    "10":("Japanese" ,"ja"),
}

print("Available Languages 🌎:")
for key,(name,code) in languages.items():
    print(f"{key}.{name} ({code})")

choice = input("Choose the Language(1-10):")

if choice in languages:
    lang_name, lang_code = languages[choice]
else:
    print("⚠️Invalid Choice! Defaulting to Tamil.")
    lang_name, lang_code = ("Tamil","ta")

text = input("Enter the input in English:")
translator = Translator()
result = translator.translate(text, dest= lang_code)
translated_text = result.text

print(f"{lang_name}:",translated_text)

tts = gTTS(text=translated_text,lang=lang_code)
tts.save("output.mp3")
playsound("output.mp3")