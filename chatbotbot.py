
import re
import random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Hawaii"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["New York", "Paris", "Tokyo"]
}

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call a fake noodle? An impasta!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!"
]

currency_rates = {
    "usd": 0.017,
    "eur": 0.015,
    "jpy": 2.62
}


def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())


def recommend():
    print(Fore.CYAN + "What type of destination are you interested in? (Beaches, Mountains, Cities)")
    preference = normalize_input(input(Fore.YELLOW + "You: "))

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"Chatbot: I recommend visiting {suggestion}!")
        print(Fore.CYAN + "Do you like it? (yes/no)")
        answer = normalize_input(input(Fore.YELLOW + "You: "))

        if answer == "yes":
            print(Fore.GREEN + f"Chatbot: Great! I hope you have a wonderful trip in {suggestion}!")
        elif answer == "no":
            print(Fore.CYAN + "Chatbot: No worries! Let's try again.")
            recommend()
        else:
            print(Fore.RED + "Chatbot: Please answer with yes or no.")
    else:
        print(Fore.RED + "Chatbot: Please choose Beaches, Mountains, or Cities.")


def packing_tips():
    location = normalize_input(
        input(Fore.CYAN + "Chatbot: Where are you going?\n" + Fore.YELLOW + "You: ")
    )

    days = input(
        Fore.CYAN + "Chatbot: How many days will you be there?\n" + Fore.YELLOW + "You: "
    )

    try:
        days = int(days)

        if days <= 0:
            print(Fore.RED + "Chatbot: Please enter a positive number of days.")
            return

    except ValueError:
        print(Fore.RED + "Chatbot: Please enter a valid number of days.")
        return

    print(Fore.GREEN + f"Chatbot: For your {days}-day trip to {location}, pack:")
    print(Fore.GREEN + f"- About {days * 2} sets of clothes, including extras")
    print(Fore.GREEN + "- Toiletries and personal hygiene items")
    print(Fore.GREEN + "- Phone charger and power bank")
    print(Fore.GREEN + "- Travel documents and identification")
    print(Fore.GREEN + "- Check the weather forecast before leaving")


def tell_joke():
    print(Fore.YELLOW + f"Chatbot: {random.choice(jokes)}")


def budget_estimator():
    print(Fore.CYAN + "Chatbot: Let's estimate your travel budget!")

    try:
        days = int(input(Fore.YELLOW + "How many days is your trip? "))
        daily_budget = float(input(Fore.YELLOW + "Daily spending budget in PHP: "))
        transportation = float(input(Fore.YELLOW + "Total transportation cost in PHP: "))
        accommodation = float(input(Fore.YELLOW + "Accommodation cost per night in PHP: "))

        if days <= 0 or daily_budget < 0 or transportation < 0 or accommodation < 0:
            print(Fore.RED + "Chatbot: Enter positive days and non-negative costs.")
            return

        daily_total = daily_budget * days
        accommodation_total = accommodation * days
        total = daily_total + transportation + accommodation_total

        print(Fore.GREEN + "\n--- Travel Budget Estimate ---")
        print(Fore.GREEN + f"Daily expenses: PHP {daily_total:,.2f}")
        print(Fore.GREEN + f"Transportation: PHP {transportation:,.2f}")
        print(Fore.GREEN + f"Accommodation: PHP {accommodation_total:,.2f}")
        print(Fore.GREEN + f"Estimated total: PHP {total:,.2f}")
        print(Fore.GREEN + f"Budget with 10% extra: PHP {total * 1.10:,.2f}")

    except ValueError:
        print(Fore.RED + "Chatbot: Please enter valid numbers.")


def travel_checklist():
    checklist = [
        "Passport or valid identification",
        "Tickets and hotel reservations",
        "Clothes appropriate for the weather",
        "Phone, charger, and power bank",
        "Cash, bank cards, and travel budget",
        "Toiletries and personal medication, if needed",
        "Travel insurance and emergency contacts"
    ]

    print(Fore.CYAN + "\nChatbot: Here is your travel checklist!")

    for item in checklist:
        print(Fore.GREEN + "[ ] " + item)

    print(Fore.CYAN + "Make sure to check everything before leaving!")


def currency_converter():
    print(Fore.CYAN + "Chatbot: Currency Converter (PHP)")
    print(Fore.CYAN + "Available currencies: USD, EUR, JPY")

    currency = normalize_input(
        input(Fore.YELLOW + "Convert PHP to which currency? ")
    )

    if currency not in currency_rates:
        print(Fore.RED + "Chatbot: Please choose USD, EUR, or JPY.")
        return

    try:
        amount = float(input(Fore.YELLOW + "How many Philippine pesos (PHP)? "))

        if amount < 0:
            print(Fore.RED + "Chatbot: Please enter a non-negative amount.")
            return

        converted = amount * currency_rates[currency]

        print(
            Fore.GREEN
            + f"PHP {amount:,.2f} is approximately {converted:,.2f} {currency.upper()}."
        )
        print(Fore.YELLOW + "Note: These are example exchange rates, not live rates.")

    except ValueError:
        print(Fore.RED + "Chatbot: Please enter a valid amount.")


def show_help():
    print(Fore.MAGENTA + "\nChatbot: Here is what I can do!")
    print(Fore.GREEN + "- Recommend destinations (say recommendation)")
    print(Fore.GREEN + "- Give packing tips (say packing)")
    print(Fore.GREEN + "- Tell a joke (say joke)")
    print(Fore.GREEN + "- Estimate your travel budget (say budget)")
    print(Fore.GREEN + "- Show a travel checklist (say checklist)")
    print(Fore.GREEN + "- Convert PHP to foreign currencies (say currency)")
    print(Fore.GREEN + "- Show commands (say help)")
    print(Fore.GREEN + "- Exit the chatbot (say exit)")


def chat():
    print(Fore.CYAN + "Hello! I'm your Travel Chatbot.")

    name = input(Fore.YELLOW + "What is your name? ")
    print(Fore.CYAN + f"Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = normalize_input(
            input(Fore.YELLOW + f"\n{name}: ")
        )

        if "recommendation" in user_input or "recommend" in user_input:
            recommend()

        elif "packing" in user_input:
            packing_tips()

        elif "joke" in user_input:
            tell_joke()

        elif "budget" in user_input:
            budget_estimator()

        elif "checklist" in user_input:
            travel_checklist()

        elif "currency" in user_input or "convert" in user_input:
            currency_converter()

        elif "help" in user_input or "what can you do" in user_input:
            show_help()

        elif "exit" in user_input or "quit" in user_input:
            print(Fore.CYAN + "Chatbot: Goodbye! Have a great trip!")
            break

        else:
            print(
                Fore.RED
                + "Chatbot: Sorry, I didn't understand. Type 'help' to see the commands."
            )


if __name__ == "__main__":
    chat()


