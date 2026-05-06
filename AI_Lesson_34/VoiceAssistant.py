import speech_recognition as sr
import pyttsx3
from datetime import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("???? Speak Now ????")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print(f"✅ You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("❌ Couldn't Understand...")
        except sr.RequestError as e:
            print(f"❌ API Error: {e}")
    return ""

def respond_to_command(command):
    if "hello" in command:
        speak("Hi there! How can I help you?")
    elif "your name" in command:
        speak("I am your Python Voice Assistant!")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"It is {now} now.")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False
    else:
        speak("I am not sure how to help you with that.")
    return True

def main():
    speak("Voice Assistant Activated! Say something.")

    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break

if __name__ == "__main__":
    main()