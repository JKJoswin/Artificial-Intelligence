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
print(f"Type {Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN} or {Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}")

while True:
    user_input = input(f"{Fore.GREEN}>>{Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue
    
    if user_input.lower()=='exit':
        break

    elif user_input.lower()=='reset':
        conversation_history.clear()
        print(f"{Fore.CYAN}🔃 All conversation history cleared.{Style.RESET_ALL}")
    
    elif user_input.lower()=='history':
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📃 Conversation History:{Style.RESET_ALL}")
            for text, polarity, sentiment in conversation_history:
                print(f"- \"{text}\" → {sentiment} {polarity}")
        continue

    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
        color = Fore.GREEN
    elif polarity < 0:
        sentiment = "Negative 😞"
        color = Fore.RED
    else:
        sentiment = "Neutral 😐"
        color = Fore.YELLOW
    
    conversation_history.append((user_input,sentiment,polarity))
    print(f"{color}Sentiment:{sentiment} | Polarity_score:{polarity}{Style.RESET_ALL}")