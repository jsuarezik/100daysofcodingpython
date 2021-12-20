from os import system
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the blind auction system.")
bidders = {}
should_stop = False
max_bid = 0
max_bidder = ""
while not should_stop:
  name = input("What's your name?\n")
  bid = int(input("What's your bid?\n$"))
  bidders[name] = bid
  if bid > max_bid:
    max_bidder = name
    max_bid = bid
  choice = input("Is there any other bidder? yes/no \n").lower()
  if choice == "no":
    should_stop = True
  system('clear')
  
print(f"The winner is {max_bidder} with ${max_bid}")
  


