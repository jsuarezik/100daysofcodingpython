import random
from os import system
from art import logo

def get_card():
  return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]) 

def deal_cards(number):
  cards = []
  for i in range(0, number):
    cards.append(get_card())
  return cards

def has_blackjack(cards):
  score = get_hand_score(cards)
  return score == 21

def get_hand_score(cards):
  score = sum(cards) 
  if score > 21 and 11 in cards:
    score -= 10
  return score

game_over = False
while not game_over:
  if input("Do you want to play a game of blackjack? [y/n] \n").lower() == "n":
    game_over = True
  else:
    system('clear')
    print(logo)
    player_cards = deal_cards(2)
    dealer_cards = deal_cards(2)
    if has_blackjack(dealer_cards):
        print("You Lose")
    elif has_blackjack(player_cards):
        print ("You Win")
    else:
        keep_dealing = True
    while(keep_dealing):
        player_score = get_hand_score(player_cards)
        dealer_score = get_hand_score(dealer_cards)
        print(f"Player cards: {player_cards} Player current score: {player_score}")
        print(f"Dealer first card: {dealer_cards[0]}")
        
        if player_score == 21:
            print("You Win")
            keep_dealing = False
        elif player_score > 21:
            print("You Lose")
            keep_dealing = False
        elif input("Do you want another card? [y/n]\n").lower() == "y":
            player_cards.append(get_card())
        else:
            keep_dealing = False
            while (dealer_score < 17):
                dealer_cards.append(get_card())
                dealer_score = get_hand_score(dealer_cards)
            print(f"Your final cards: {player_cards} Final score: {player_score}")
            print(f"Dealer final cards: {dealer_cards} Dealer Score: {dealer_score}")
            if dealer_score > 21:
                print("You Win")
            elif player_score > dealer_score:
                print("You Win")
            elif dealer_score > player_score:
                print("You Lose")
            else:
                print("It's a Draw")
        



    