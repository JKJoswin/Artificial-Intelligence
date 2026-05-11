import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame
import time

pygame.mixer.init()

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak in Tamil...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language="ta-IN")
    print(f"You said: {text}")
    translated = GoogleTranslator(source="ta", target="en").translate(text)
    print(f"Translated: {translated}")
    
    speech = gTTS(text=translated, lang="en")
    speech.save("english_voice.mp3")

    pygame.mixer.music.load("english_voice.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
except Exception as e:
    print("Error:",e)