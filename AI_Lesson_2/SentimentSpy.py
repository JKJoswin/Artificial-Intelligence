import colorama
from colorama import Fore,Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}🕵️ Welcome to Sentiment Spy! 🕵️{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Please Enter Your Name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mystery Agent"

conversation_history = []

print(f"{Fore.CYAN}Hello Agent {user_name}!{Style.RESET_ALL}")
print("Type a sentence and I will analyze your sentences with TextBlob and show you the sentiment")