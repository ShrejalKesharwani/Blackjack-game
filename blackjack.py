import os
import random
# import click
# from replit import clear
from blackjack_art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clrscr():
  os.system('cls')

play = input("Do you want to play a game of 'Blackjack'? Type 'y' or 'n':")
if play == 'n' or play == 'N':
    print("""\nIt's alright. Come again, if you want to CHALLENGE me 😎😏""")

while play == 'y':
  clrscr()
  print(logo)
  your = random.choices(cards, k=2)
  print(f'  Your cards: {your}, current score {sum(your)}')
  comp = random.choices(cards, k=2)
  print(f'  Computer\'s first card: {comp[0]}')

  get_card = input("\nType 'y' to get another card, type 'n' to pass: ")
  while get_card == 'y':
    another_card = random.choices(cards, k=1)
    if another_card[0] not in your: 
      your.extend(another_card)
      if sum(your) > 21 and 11 in your:
        for i in range(0, len(your)):
         if your[i] == 11:
           your[i] = 1
      print(f'  Your cards: {your}, current score {sum(your)}')
      if sum(your) > 21:
        break
      get_card = input("\nType 'y' to get another card, type 'n' to pass: ")
  
# user don't want another card    
  print(f'\nYour final hand: {your}, total score: {sum(your)}' )
  while sum(comp) < 17:
    a_card = random.choices(cards, k=1)
    if a_card[0] not in comp:
      comp.extend(a_card)
      
  print(f'Computer\'s final hand: {comp}, total score: {sum(comp)}\n')
  if sum(your) <= 21 and sum(comp) <= 21:
    if sum(your) > sum(comp):
      print("You WIN 🤩. THIS TIME I WAS LINIENT, THAT'S WHY YOU WON🥰")
    elif sum(your) < sum(comp):
      print("You LOSE😭. BETTER LUCK NEXT TIME DUDE🤪😁 ")
    else: 
      print("Draw 🙄. WAIT AND WATCH FOR THE NEXT TIME ☹")
  elif sum(your) > 21:
    print("You LOSE 😭. BETTER LUCK NEXT TIME DUDE 🤪😁")
  else:
    print("You WIN 🤩. THIS TIME I WAS LINIENT, THAT'S WHY WON 😡😡")
  
  play = input("\nDo you want to play a game of 'Blackjack'? Type 'y' or 'n':")
  if play == 'n' or play == 'N':
    print("""\nThank you for playing with me🤩🤩\n
COME SOON, I'LL BE WAITING...🥰""")

