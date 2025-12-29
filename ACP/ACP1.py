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

print("Which country are you from?")
country = input()
print(f"I wish that I would live in {country}!")

print("How is the weather there?(cold/hot)")
weather = input()

if weather.lower() == "cold":
    print("I hope there is snow!")
elif weather.lower() == "hot":
    print("Too sweaty!")
else:
    print("Sounds great!")

print("What's your favourite sport?")
sport = input()
print(f"{sport} sounds fun!")

print("It was nice chatting with you! Goodbye!")