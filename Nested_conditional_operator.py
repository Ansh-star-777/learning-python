user_input = input("Anime or Movies")

if user_input == "Anime":
    print("Good choice")
elif user_input == "Movies":
    print("Bad choice")
else:
    print("Not bad")

print("-----------------------------")


medical_cause = input("Do you have medical issues (y/n):")

if medical_cause == "y":
    print("You are allowed to give test")
else:
    attendance = int(input("What is your attendance"))
    if attendance >= 75 and attendance <= 100:
        print("You are allowed to give test")
    else:
        print("You are not allowed to give test") 
    
