import re, random
from colorama import Fore, init

init(autoreset=True)

destinations ={"Beaches":["Bali", "Maldives", "Hawaii"],
               "Mountains":["Swiss Alps", "Rocky Mountains", "Himalayas"],
               "Cities":["New York", "Paris", "Tokyo"]}
jokes ={"Why don't scientists trust atoms? Because they make up everything!", "What do you call a fake noodle? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"}

def normalize_input(text):
    return re.sub(r"\s+"," ", text.strip().lower())


def recommend():
    print(Fore.CYAN + "What type of destination are you interested in? (Beaches, Mountains, Cities)")
    preference = input(Fore.YELLOW+"You: ")
    preference = normalize_input(preference)
    if preference in destinations:
        suggestions= random.choice(destinations[preference])
        print(Fore.GREEN + f"Chatbot: I recommend visiting {suggestions}!")
        print(Fore.CYAN + "Do you like it? (yes/no)")
        answer = input(Fore.YELLOW+"You: ").lower()

        if answer == "yes":
            print(Fore.GREEN+ "Chatbot: Great! I hope you have a wonderful trip in {suggestions}!")
        elif answer == "no":
            print(Fore.CYAN + "Chatbot: No worries! Let's try again.")
            recommend()
        else:
            print(Fore.RED + "Chatbot: I didn't understand that. Please answer with 'yes' or 'no'.")
            recommend()
    else:
        print(Fore.RED + "Chatbot: Sorry, I don't have recommendations for that type of destination. Please choose from Beaches, Mountains, or Cities.")
        recommend()

def packing_tips():
    print(Fore.CYAN + "Chatbot: WHere to?")
    location = normalize_input(input(Fore.YELLOW+"You: "))
    print(Fore.CYAN+f"Chatbot: How many days will you be there?")
    days = input(Fore.YELLOW+"You: ")

    print(Fore.GREEN + f"Chatbot: For a trip to {location} for {days} days, I recommend packing the following items:")
    print(Fore.GREEN +"Pack good clothes")
    print(Fore.GREEN +"Pack charger")
    print(Fore.GREEN +"Check Weather")

def tell_joke():
    print(Fore.YELLOW + f"Chatbot: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA+"Chatbot: I can ")
    print(Fore.GREEN+"- Recommend travel destination(say reccomendation)")
    print(Fore.GREEN+"- Give packing tips(say packing)")
    print(Fore.GREEN+"- Tell a joke(say joke)")
    print(Fore.GREEN+"to Exit (Say Exit)")

def chat():
    print(Fore.CYAN+ "Hello Im Chatbot")
    name = input(Fore.YELLOW+"What is your name? ")
    print(Fore.CYAN+f"Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW+f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommendation" in user_input or "recommend" in user_input:
            recommend()
        elif "packing" in user_input or "packing tips" in user_input:
            packing_tips()
        elif "joke" in user_input or "tell me a joke" in user_input:
            tell_joke()
        elif "help" in user_input or "what can you do" in user_input:
            show_help()
        elif "exit" in user_input or "quit" in user_input:
            print(Fore.CYAN + "Chatbot: Goodbye! Have a great day!")
            break
        else:
            print(Fore.RED+"Chatbot: Sorry please try again")
if __name__ == "__main__":
    chat()
    

