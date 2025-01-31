import random
from termcolor import colored
N=int(input("\033[1;34m Number of Try \033[0m"))
choices=["rock","paper","scissors"]
for _ in range(N):
    user_choice=input("Enter you choice [ rock, paper , scissors ] :").lower()

    if user_choice not in choices:
        print(colored("Invalid choice! Please enter rock, paper, or scissors.", "red"))
        continue

    computer_choice=random.choice(choices)
    if(computer_choice=="rock" and user_choice=="paper" or 
       computer_choice=="paper" and user_choice=="scissors"or  
       computer_choice=="scissors" and user_choice=="rock"):
        print(f"Computer choice: {computer_choice}")
        print("\033[32m You Win \033[0m")
    
    elif(computer_choice=="rock" and user_choice=="rock" or 
       computer_choice=="paper" and user_choice=="paper"or  
       computer_choice=="scissors" and user_choice=="scissors"):
        print(f"Computer choice: {computer_choice}")
        print("\033[1;34m Draw , try again :)\033[0m")
    
    else:
        print(f"Computer choice: {computer_choice}")
        print("\033[31m You Lose , Computer Win \033[0m")
