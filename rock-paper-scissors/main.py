import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choices = [rock, paper, scissors]
choices_label = ["ROCK", "PAPER", "SCISSORS"]

print("Rock, Paper, Scissors.")
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice = int(input("What's your choice?\n"))
print (f"You chose: {choices_label[choice]}\n{choices[choice]}")
computer_choice = random.randint(0,2)
print(f"Computer chose: {choices_label[computer_choice]}\n{choices[computer_choice]}")

if (choice == 0):
    if computer_choice == 1:
        print("YOU LOSE")
    elif computer_choice == 2:
        print("YOU WIN")
    else:
        print("DRAW")
elif choice == 1:
    if computer_choice == 2:
        print("YOU LOSE")
    elif computer_choice == 0:
        print("YOU WIN")
    else:
        print("DRAW")
else: 
    if computer_choice == 0:
        print("YOU LOSE")
    elif computer_choice == 1:
        print("YOU WIN")
    else:
        print("DRAW")