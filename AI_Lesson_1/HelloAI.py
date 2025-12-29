print("Hello! I am Chatbot24/7! What's your Name?")
name = input()

print(f"Hello {name}! How's your day?(good/bad)")
mood = input()

if mood.lower() == "good":
    print("Great to hear that! Have a nice day!")
elif mood.lower() == "bad":
    print("Oh no! I feel sorry for you!")
else:
    print("Yeah! I know! Sometimes its hard to express thoughts through words!")

print("It was nice chatting with you! Goodbye!")