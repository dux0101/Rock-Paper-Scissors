import random


options = ["rock", "paper", "scissors"]


user_choice = input("Choose rock, paper or scissors: ".lower())

other_choice = input("Choose rock, paper or scissors: ".lower())

print("You Chose:", user_choice)
print("The Other Chose", other_choice)

if user_choice == other_choice:
    print("Its a tie")
elif user_choice == "rock" and other_choice == "scissors":
    print("You Win!")
elif user_choice == "paper" and other_choice == "rock":
    print("You Win!")
elif user_choice == "scissors" and other_choice == "paper":
    print("You Win!")
else:
    print("The other Wins!")
