#Import the logo
#Import the data
#Import the vs ASCII
#Get a random choice from data for option A, and option B
#Compare option A and B
#Update Score if guess is correct
#Stop the loop if guess is wrong.

from art import logo, vs
from game_data import data
from os import system
import random

def get_random_choice():
  return random.choice(data)

def get_compare_string(data):
  return f"{data['name']}, {data['description']}, {data['country']}."

def get_winner_choice(a, b):
  if (a['follower_count'] >= b['follower_count']):
    return a
  else:
    return b


print(logo)
game_over = False
score = 0
choice_A = get_random_choice()
while not game_over:
  choice_B = get_random_choice()
  print(f"Compare A: {get_compare_string(choice_A)}")
  print(vs)
  print(f"Compare B: {get_compare_string(choice_B)}")
  guess = input("Who has more followers? A or B\n").lower()
  winner_choice = get_winner_choice(choice_A, choice_B)

  if (guess == "a"):
    guess = choice_A
  else:
    guess = choice_B

  if winner_choice['name'] == guess['name']:
    choice_A = choice_B
    score += 1
    system('clear')
    print(f"You're right curent score: {score}")
  else:
    print(f"You're wrong, your final score is : {score}")
    game_over = True



