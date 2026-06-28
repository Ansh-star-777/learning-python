import re,random
from colorama import Fore,init

init(autoreset=True)

destinations = {
    "beaches" : ["Bali","Maldives","Phoket"],
    "mountains" : ["Himyalas","Rocky Mountains","Swiss Alphes"],
    "cities" : ["Tokoyo","Paris","New York"]
}
jokes = [ "Why don't programmers like nature? Too many bugs!", "Why did the computer go to the doctor? Because it had a virus!", "Why do travelers always feel warm? Because of all their hot spots!" ]

def normalise_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    print(Fore.CYAN + "Travelbot: beaches, mountains, or cities?")
    user_choice = input(Fore.YELLOW + "You: ")
    user_choice = normalise_input(user_choice)
    
    if user_choice in destinations:
        suggestion = random.choice(destinations[user_choice])
        print(Fore.GREEN + f"Travelbot: How about {suggestion}")
        print(Fore.CYAN + "Travelbot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()
        
        if answer == "yes":
            print(Fore.GREEN + f"Travelbot: Awsome! enjoy {suggestion}")
        elif answer == "no":
            print(Fore.RED + "Travelbot: let's try again")
            recommend()
        else:
            print(Fore.RED + "Travelbot: i will suggest again")
    else:
        print(Fore.RED + "Travelbot: Sorry, i don't have that type of destination")
        recommend()
    

if __name__ == "__main__":
    recommend()
