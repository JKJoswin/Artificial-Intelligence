import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
def get_random_technology_facts():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Did you know? {fact_data['text']}")
    else:
        print("Failed to fetch Fun Fact!")

while True:
    user_input = input("Press 'Enter' for a Random Technology Fact or enter 'q' to exit:")
    if user_input.lower() == 'q':
        break
    get_random_technology_facts()
