import random
option = ["Rock","Paper","Scissor"]

user_choice = input("Choose Rock, Paper or Scissor: ")
computer_choice = random.choice(option)
print()

print("YOU chose:", user_choice)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It,s a tie!")

elif user_choice == "Rock" and computer_choice =="Scissor":
    print("Rock smashes scissor! You win!")

elif user_choice == "Paper" and computer_choice =="Rock":
    print("Paper cover rock! You win!")

elif user_choice == "Scissor" and computer_choice =="Paper":
    print("Scissor cuts paper! You win!")

else:
    print("You lose!")