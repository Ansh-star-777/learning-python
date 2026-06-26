import colorama
from colorama import Fore,Style
from textblob import TextBlob

colorama.init()
print(f"{Fore.CYAN}Welcome to Sentiment Spy{Style.RESET_ALL}")

user_name = input(f"{Fore.GREEN}What your name Lad{Style.BRIGHT}").strip()
if not user_name:
    user_name = "Rhino67"

conversation_history = []
print(f"{Fore.CYAN}Hello, Agent {user_name}")
print("Write a sentence and I will analyze your sentiment")
print(f"Type {Fore.YELLOW}reset{Fore.CYAN}, {Fore.YELLOW}history{Fore.CYAN}, "
f"or {Fore.YELLOW}exit{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

while True:
    user_input = input("Enter your sentence").strip()
    if not user_input:
        print("Please enter a some valid text")
        continue
    if user_input.lower() == "exit":
        break

    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0.25:
        sentiment_type = "Positive"
        colour = Fore.GREEN
    elif polarity < -0.25:
        sentiment_type = "Negative"
        colour = Fore.RED
    else:
        sentiment_type = "Neutral"
        colour = Fore.YELLOW
    
    print(f"{colour} {sentiment_type} Sentiment Detected!")
    
    
