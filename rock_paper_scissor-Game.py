import random

print("Welcome to the Rock, Paper, Sissors Game !!")

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

available_options = [rock,paper,scissors]

user_choice = int(input("Enter 1 for Rock, 2 for Paper and 3 for Sissors: "))
if user_choice == 1:
    user_choice = rock
    print(f"Your Choice:\n{rock}")
elif user_choice == 2:
    user_choice = paper
    print(f"Your Choice:\n{paper}")

elif user_choice == 3:
    user_choice = scissors
    print(f"Your Choice:\n{scissors}")
else:
    print("Wrong coice buddy")
 
mac_choice = random.choice(available_options)

print(f"Computer Choice: {mac_choice}")

if user_choice == mac_choice:
    print("It is Draw!!")
elif (user_choice == rock and mac_choice == scissors) or (user_choice == scissors and mac_choice == paper) or (user_choice == paper and mac_choice == rock):
    print("You Won the Game!!")
else:
    print("You Lost It!!")
