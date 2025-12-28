'''
-------------------------------------------------------------------------------
Name:  CPT Milestone 4 - Blackjack Program - Michael Mondaini.py

Purpose: Developing and creating the worldwide game known as, "Blackjack" and the purpose 
of this program is to expand my knowledge of python code while helping assist  me in 
creating a functioning game people all around the world can enjoy.

Author: Michael Mondaini

Created:  1/20/2023
------------------------------------------------------------------------------
'''

#--==Imported Modules==--
#These imported modules assist the program allowing easy to use functions to be imported, such as reading keyboard key presses
from readchar import readchar
import time
import random
import os

#--==Local Variables==--
#These variables are dependent on the user and their actions, and will be used later throughout the program
user_rounds = 0
user_balance = 1500
saved_player_card_total = 0
saved_dealer_card_total = 0
player_card_total = 0
dealer_card_total = 0
rounds_completed = 0
round_ended = False
user_stats = {
  "total_user_rounds": 0,
  "total_user_wins": 0,
  "total_user_bet_wins": 0,
  "total_user_loses": 0,
  "total_user_bet_loses": 0
}

#--==Global Variables==--
#These variables are needed for the program to run, and don't require user action, and will be used later throughout the program
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

#--==Functions==--
#These functions are the core of the program and contain majority of the program code, and allow for multiple different functions to be stored for later use

#The clear output function allows for the console of the program to being cleared at anytime, when the function is called
def clear_output():
  #Clears the console by using the imported module
  os. system('clear')

#The game count function allows the user to decide how many rounds they would like to play
def game_count():
  global user_balance

  #Outputs the selection menu of how many rounds the user can decide from
  print("│  ╼Balance: $" + str(user_balance) + "╾".ljust(len(str(user_balance))) + "│".ljust(21), "\n│  ╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍".ljust(6) + "  │".ljust(21), "\n")
  print("Select number of rounds: ")
  print("│  1 - 5 Rounds".ljust(21), "│".ljust(21))
  print("│  2 - 10 Rounds".ljust(21), "│".ljust(21))
  print("│  3 - 25 Rounds".ljust(21), "│".ljust(21))
  print("│  4 - 50 Rounds".ljust(21), "│".ljust(21))
  print("│  5 - Custom Amount".ljust(21), "│".ljust(21))

  #Reads the user's input and add's the correct amount of rounds accordingly, with built it redundancy if the user selects a incorrect option
  global user_rounds
  user_rounds = readchar()
  if user_rounds == "1":
    clear_output()
    user_rounds = 5
    user_round_bet(user_rounds)
  elif user_rounds == "2":
    clear_output()
    user_rounds = 10
    user_round_bet(user_rounds)
  elif user_rounds == "3":
    clear_output()
    user_rounds = 25
    user_round_bet(user_rounds)
  elif user_rounds == "4":
    clear_output()
    user_rounds = 50
    user_round_bet(user_rounds)
  elif user_rounds == "5":
    clear_output()
    user_rounds = (input("Enter: "))
    while user_rounds.isdigit() != True:
      print("Invalid Input")
      time.sleep(2)
      clear_output()
      user_rounds = (input("Enter: "))
    user_round_bet(user_rounds)
  else:
    print("Invalid Input")
    time.sleep(2)
    clear_output()
    game_count()
  clear_output()

#The user round bet function allows the user to decide how much they would like to bet on the current rounds they are playing
def user_round_bet(rounds):
  global user_balance

  #Outputs the selection menu of how much the user would like to bet for user can decide from
  print("│  ╼Balance: $" + str(user_balance) + "╾".ljust(len(str(user_balance))) + "│".ljust(21), "\n│  ╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍".ljust(6) + "  │".ljust(21), "\n")
  print("Select bet size: ")
  print("│  1 - $25 Dollars".ljust(21), "│".ljust(21))
  print("│  2 - $50 Dollars".ljust(21), "│".ljust(21))
  print("│  3 - $100 Dollars".ljust(21), "│".ljust(21))
  print("│  4 - $250 Dollars".ljust(21), "│".ljust(21))
  print("│  5 - $500 Dollars".ljust(21), "│".ljust(21))
  print("│  6 - $1000 Dollars".ljust(21), "│".ljust(21))
  print("│  7 - Custom Amount".ljust(21), "│".ljust(21))
  
  #Reads the user's input and add's their correct bet size accordingly, with built it redundancy if the user selects a incorrect option
  global user_bet_choice
  user_bet_choice = readchar()
  global user_bet
  if user_bet_choice == "1":
    clear_output()
    user_bet = 25
    game(rounds, user_bet)
  elif user_bet_choice == "2":
    clear_output()
    user_bet = 50
    game(rounds, user_bet)
  elif user_bet_choice == "3":
    clear_output()
    user_bet = 100
    game(rounds, user_bet)
  elif user_bet_choice == "4":
    clear_output()
    user_bet = 250
    game(rounds, user_bet)
  elif user_bet_choice == "5":
    clear_output()
    user_bet = 500
    game(rounds, user_bet)
  elif user_bet_choice == "6":
    clear_output()
    user_bet = 1000
    game(rounds, user_bet)
  elif user_bet_choice == "7":
    clear_output()
    user_bet = (input("Enter: "))
    while user_bet.isdigit() != True:
      print("Invalid Input")
      time.sleep(2)
      clear_output()
      user_bet = (input("Enter: "))
    user_bet = int(user_bet)
    game(rounds, user_bet)
  else:
    print("Invalid Input")
    time.sleep(2)
    clear_output()
    user_round_bet(rounds)

#The calculate card function allows for a blackjack card to be entered and calculated for it's real value, then returning the result
def calculate_card(card):

  #Checking if the card is a King, Queen or Jack
  if "K" == card or "Q" == card or "J" == card:
    return 10

  #Checking if the card is an Ace
  if "A" == card:
    if player_card_total + 11 > 21:
      return 1
    else:
      return 11

  #Checking if the card is none of the above, and already has it's value displayed
  elif "1" == card or "2" == card or "3" == card or "4" == card or "5" == card or "6" == card or "7" == card or "8" == card or "9" == card or "10" == card:
    return int(card)

#The continue menu function allows the user to decide if they would like to continue to another round or quit to the main menu, or checking if all their rounds have finsihed
def continue_menu(rounds, user_bet, rounds_completed):
  global user_balance

  #Outputs the options for the player to choose from
  print("Select an option: ")
  print("│  1 - Next Round".ljust(21), "│".ljust(21))
  print("│  2 - Quit".ljust(21), "│".ljust(21))

  #Reads the user's input and decide if they should countine to the next round or quit to the main menu or are forced to quit as their rounds have finished
  countine_selection = readchar()

  #Decides if user would like to play another round and if they have finsihed their rounds
  if countine_selection == "1":
    if int(rounds_completed) < int(rounds):
      clear_output()
      game(rounds, user_bet)
    if int(rounds_completed) == int(rounds):
      clear_output()
      print("│  ╼Balance: $" + str(user_balance) + "╾".ljust(len(str(user_balance))) + "│".ljust(21), "\n│  ╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍".ljust(6) + "  │".ljust(21), "\n")
      print("Rounds Finished")
      print("━━━━━━━━━━━━━━━━━━━━")
      print("Redirecting to Menu")
      time.sleep(3)
      clear_output()
      main_menu()

  #Decides if the user would like to quit to the main menu
  if countine_selection == "2":
    rounds_completed = 0
    global round_ended
    round_ended = True
    clear_output()
    main_menu()
  else:
    print("Invalid Input")
    time.sleep(2)
    clear_output()
    continue_menu(rounds, user_bet, rounds_completed)

#The player bust function is used when the program detects that the user has busted (Gone over 21), and intern calls the continue menu function
def player_bust_function(rounds, bet_amount, user_balance):
  user_balance -= user_bet
  print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
  print("Player Bust")
  print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
  continue_menu(rounds, bet_amount, rounds_completed)

#The player stand function is called when the user decides they would like to stand (User stop collecting cards, and the stars dealer collecting cards) and alerts the dealer if they have won or not, and move them into the correct function
def player_stand_function(dealer_card_1, dealer_card_2, dealer_card_3, dealer_card_4, player_card_total, rounds, player_current_card, first_player_card, second_player_card, third_player_card, fourth_player_card, player_total, rounds_completed, bet_amount):
  global user_balance
  global user_bet
  decision_chosen = False
  clear_output()

  #Outputs the current user cards and dealer cards depending on their current card value
  print("│  ╼Balance: $" + str(user_balance) + "╾".ljust(len(str(user_balance))) + "│".ljust(21), "\n│  ╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍".ljust(6) + "  │".ljust(21), "\n")
  print("Round:", rounds_completed, "out of", rounds)
  print("━━━━━━━━━━━━━━━━━━━━")
  time.sleep(1.25)

  #Outputs 3 cards if the user is only holding 3 cards currently
  if player_current_card == 3:
    print("Player Card [1]:", str(first_player_card) + " " + str((random.choice(suits))) + "[" + str(calculate_card(first_player_card)) + "]")
    time.sleep(1.25)
    print("Player Card [2]:", str(second_player_card) + " " + str((random.choice(suits))) + "[" + str(calculate_card(second_player_card)) + "]")
    time.sleep(1.25)
    print("Player Card" + " [" + "Total" + "]: " + str(player_total))
    print("---------------------")
    time.sleep(2)

  #Outputs 4 cards if the user is only holding 4 cards currently
  if player_current_card == 4:
    print("Player Card [1]:", str(first_player_card) + " " + str((random.choice(suits))) + "[" + str(calculate_card(first_player_card)) + "]")
    time.sleep(1.25)
    print("Player Card [2]:", str(second_player_card) + " " + str((random.choice(suits))) + "[" + str(calculate_card(second_player_card)) + "]")
    time.sleep(1.25)
    print("Player Card [3]:", str(third_player_card) + " " + str((random.choice(suits))) + "[" + str(calculate_card(third_player_card)) + "]")
    time.sleep(1.25)
    print("Player Card" + " [" + "Total" + "]: " + str(player_total))
    print("---------------------")
    time.sleep(1.25)
  
  #Outputs the dealers current cards
  print("Dealer Card [1]:", str(dealer_card_1) + " " + str((random.choice(suits))) + "[" + str(dealer_card_1) + "]")
  time.sleep(1.25)
  print("Dealer Card [2]:", str(dealer_card_2) + " " + str((random.choice(suits))) + "[" + str(dealer_card_2) + "]")
  time.sleep(1.25)

  #Decides if the dealer has cards equally or surpassing the value of 16 and lower than or equal to the value of 21, and if not adding a card to the dealer
  if dealer_card_1 + dealer_card_2 >= 16 and dealer_card_1 + dealer_card_2 <= 21:
    decision_chosen = True

    #Decides if the user has a greater value of cards than the dealer, and if so outputting the the user has won and calling the continue menu function
    if player_card_total > dealer_card_1 + dealer_card_2:
      print("Dealer Card" + " [" + "Total" + "]: " + str(dealer_card_1 + dealer_card_2))
      time.sleep(1.25)
      print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
      print("Dealer Lost")
      print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
      print("Player Wins")
      print("------------")
      print("You have won $" + str(user_bet))
      print("------------")
      user_balance += user_bet
      (user_stats["total_user_wins"]) += 1
      (user_stats["total_user_bet_wins"]) += user_bet
      time.sleep(1.25)
      continue_menu(rounds, bet_amount, rounds_completed)
      
    #Decides if the dealer and the user have an eqaul value of cards, and if so outputting that the dealer pushed (Tied with player) and calling the continue menu function
    elif player_card_total == dealer_card_1 + dealer_card_2:
      print("Dealer Card" + " [" + "Total" + "]: " + str(dealer_card_1 + dealer_card_2 ))
      time.sleep(1.25)
      print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
      print("Dealer Push")
      print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
      time.sleep(1.25)
      continue_menu(rounds, bet_amount, rounds_completed)

    #Decides if the dealer has a greater value of cards than the user, and if so outputting the dealer has won and calling the continue menu function
    else:
      print("Dealer Card" + " [" + "Total" + "]: " + str(dealer_card_1 + dealer_card_2))
      time.sleep(1.25)
      print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
      print("Dealer Wins")
      print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
      user_balance -= user_bet
      (user_stats["total_user_loses"]) += 1
      (user_stats["total_user_bet_loses"]) -= user_bet
      time.sleep(1.25)
      continue_menu(rounds, bet_amount, rounds_completed)

  #Decides if the dealer has a greater value of cards than the 21, and if so outputting the  dealer has bust (Gone over 21) and calling the continue menu function
  elif dealer_card_1 + dealer_card_2 > 21 and decision_chosen == False:
    decision_chosen == True
    print("Dealer Card" + " [" + "Total" + "]: " + str(dealer_card_1 + dealer_card_2))
    time.sleep(1.25)
    print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
    print("Dealer Bust")
    print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
    print("Player Wins")
    print("------------")
    print("You have won $" + str(user_bet))
    print("------------")
    user_balance += user_bet
    (user_stats["total_user_wins"]) += 1
    (user_stats["total_user_bet_wins"]) += user_bet
    time.sleep(1.25)
    continue_menu(rounds, bet_amount, rounds_completed)

  #Decides if the dealer has less than 21 in the value of cards, and if so outputting the dealer's next card
  elif decision_chosen == False and not dealer_card_1 + dealer_card_2 > 21: 
    print("Dealer Card [3]:", str(dealer_card_3) + " " + str((random.choice(suits))) + "[" + str(dealer_card_3) + "]")
    time.sleep(1.25)

  #Decides if the dealer has cards equally or surpassing the value of 16 and lower than or equal to the value of 21, and if not adding a card to the dealer
  if dealer_card_1 + dealer_card_2 + dealer_card_3 >= 16 and dealer_card_1 + dealer_card_2 + dealer_card_3 <= 21 and decision_chosen == False:
      decision_chosen = True

      #Decides if the user has a greater value of cards than the dealer, and if so outputting the the user has won and calling the continue menu function
      if player_card_total > (dealer_card_1 + dealer_card_2 + dealer_card_3):
        print("Dealer Card" + " [" + "Total" + "]: " + str(dealer_card_1 + dealer_card_2 + dealer_card_3))
        time.sleep(1.25)
        print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
        print("Dealer Lost")
        print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
        print("Player Wins")
        print("------------")
        print("You have won $" + str(user_bet))
        print("------------")
        user_balance += user_bet
        (user_stats["total_user_wins"]) += 1
        (user_stats["total_user_bet_wins"]) += user_bet
        time.sleep(1.25)
        continue_menu(rounds, bet_amount, rounds_completed)
        
      #Decides if the dealer and the user have an eqaul value of cards, and if so outputting that the dealer pushed (Tied with player) and calling the continue menu function
      elif player_card_total == dealer_card_1 + dealer_card_2 + dealer_card_3:
        print("Dealer Card" + " [" + "Total" + "]: " + str(dealer_card_1 + dealer_card_2 + dealer_card_3))
        time.sleep(1.25)
        print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
        print("Dealer Push")
        print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
        time.sleep(1.25)
        continue_menu(rounds, bet_amount, rounds_completed)  

      #Decides if the dealer has a greater value of cards than the user, and if so outputting the dealer has won and calling the continue menu function
      else:
        print("Dealer Card" + " [" + "Total" + "]: " + str(dealer_card_1 + dealer_card_2 + dealer_card_3))
        time.sleep(1.25)
        print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
        print("Dealer Wins")
        print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
        user_balance -= user_bet
        (user_stats["total_user_loses"]) += 1
        (user_stats["total_user_bet_loses"]) -= user_bet
        time.sleep(1.25)
        continue_menu(rounds, bet_amount, rounds_completed)

  #Decides if the dealer has a greater value of cards than the 21, and if so outputting the  dealer has bust (Gone over 21) and calling the continue menu function
  elif dealer_card_1 + dealer_card_2 + dealer_card_3 > 21 and decision_chosen == False:
    decision_chosen == True
    print("Dealer Card" + " [" + "Total" + "]: " + str(dealer_card_1 + dealer_card_2 + dealer_card_3))
    time.sleep(1.25)
    print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
    print("Dealer Bust")
    print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
    print("Player Wins")
    print("------------")
    print("You have won $" + str(user_bet))
    print("------------")
    user_balance += user_bet
    (user_stats["total_user_wins"]) += 1
    (user_stats["total_user_bet_wins"]) += user_bet
    time.sleep(1.25)
    continue_menu(rounds, bet_amount, rounds_completed)

  #Decides if the dealer has less than 21 in the value of cards, and if so outputting the dealer's next card
  elif decision_chosen == False and not dealer_card_1 + dealer_card_2 + dealer_card_3 > 21: 
    print("Dealer Card [4]:", str(dealer_card_4) + " " + str((random.choice(suits))) + "[" + str(dealer_card_4) + "]")
    time.sleep(1.25)

  #Decides if the dealer has cards equally or surpassing the value of 16 and lower than or equal to the value of 21, and if not adding a card to the dealer
  if dealer_card_1 + dealer_card_2 + dealer_card_3 + dealer_card_4 >= 16 and dealer_card_1 + dealer_card_2 + dealer_card_3 + dealer_card_4 <= 21 and decision_chosen == False:

    #Decides if the user has a greater value of cards than the dealer, and if so outputting the the user has won and calling the continue menu function
    if player_card_total > dealer_card_1 + dealer_card_2 + dealer_card_3 + dealer_card_4:
      print("Dealer Card" + " [" + "Total" + "]: " + str(dealer_card_1 + dealer_card_2 + dealer_card_3 + dealer_card_4))
      time.sleep(1.25)
      print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
      print("Dealer Lost")
      print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
      print("Player Wins")
      print("------------")
      print("You have won $" + str(user_bet))
      print("------------")
      user_balance += user_bet
      (user_stats["total_user_wins"]) += 1
      (user_stats["total_user_bet_wins"]) += user_bet
      time.sleep(1.25)
      continue_menu(rounds, bet_amount, rounds_completed)
      
    #Decides if the dealer and the user have an eqaul value of cards, and if so outputting that the dealer pushed (Tied with player) and calling the continue menu function
    elif player_card_total == dealer_card_1 + dealer_card_2 + dealer_card_3 + dealer_card_4:
      print("Dealer Card" + " [" + "Total" + "]: " + str(dealer_card_1 + dealer_card_2 + dealer_card_3 + dealer_card_4))
      time.sleep(1.25)
      print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
      print("Dealer Push")
      print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
      time.sleep(1.25)
      continue_menu(rounds, bet_amount, rounds_completed)

    #Decides if the dealer has a greater value of cards than the user, and if so outputting the dealer has won and calling the continue menu function
    else:
      print("Dealer Card" + " [" + "Total" + "]: " + str(dealer_card_1 + dealer_card_2 + dealer_card_3 + dealer_card_4))
      time.sleep(1.25)
      print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
      print("Dealer Wins")
      print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
      user_balance -= user_bet
      (user_stats["total_user_loses"]) += 1
      (user_stats["total_user_bet_loses"]) -= user_bet
      time.sleep(1.25)
      continue_menu(rounds, bet_amount, rounds_completed)

  #Decides if the dealer has a greater value of cards than the 21, and if so outputting the  dealer has bust (Gone over 21) and calling the continue menu function
  elif decision_chosen == False:
      decision_chosen = True
      print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
      print("Dealer Bust")
      print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
      print("Player Wins")
      print("------------")
      print("You have won $" + str(user_bet))
      print("------------")
      user_balance += user_bet
      (user_stats["total_user_wins"]) += 1
      (user_stats["total_user_bet_wins"]) += user_bet
      time.sleep(1.25)
      continue_menu(rounds, bet_amount, rounds_completed)

#The game decision calculator function allows the user to decide if they would like to hit (Pick up a card) or stand (Let the dealer pick up a card) and doing actions accordingly
def game_decision_calculator(player_current_card, first_player_card, second_player_card, third_player_card, fourth_player_card, dealer_card_1, dealer_card_2, dealer_card_3, dealer_card_4, player_total, rounds, bet_amount, rounds_completed, user_balance):
    global game_decision

    #Outputs the selection menu that displays to the user what options they can pick from
    if player_total < 21:
      print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
      print("Select your game decision: ")
      print("│  1 - Hit".ljust(21), "│".ljust(21))
      print("│  2 - Stand".ljust(21), "│".ljust(21))

      #Allows the user to record a key press as a input
      game_decision = readchar()

      #Decides if the user's current card is a 3 and if they decide to hit, and if so clearing the output and proceeding to the "hit" section
      if game_decision == "1" and player_current_card == 3:
        clear_output()

        #Outputs the amount of rounds that are left and how many have been played
        print("│  ╼Balance: $" + str(user_balance) + "╾".ljust(len(str(user_balance))) + "│".ljust(21), "\n│  ╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍".ljust(6) + "  │".ljust(21), "\n")
        print("Round:", rounds_completed, "out of", rounds)
        print("━━━━━━━━━━━━━━━━━━━━")
        time.sleep(1.25)

        #Outputs the dealer's first card with it's total
        print("Dealer Card [1]:", str(dealer_card_1) + " " + str((random.choice(suits))) + "[" + str(calculate_card(dealer_card_1)) + "]")
        time.sleep(1.25)

        #Calculate player's total of current cards and outputs the result
        print("Dealer Card" + " [" + "Total" + "]: " + str(calculate_card(dealer_card_1)))
        print("---------------------")
        time.sleep(1.25)

        #Outputs the players's first and second card with their total and adds an addition third player card
        print("Player Card [1]:", str(first_player_card) + " " + str((random.choice(suits))) + "[" + str(calculate_card(first_player_card)) + "]")
        time.sleep(1.25)
        print("Player Card [2]:", str(second_player_card) + " " + str((random.choice(suits))) + "[" + str(calculate_card(second_player_card)) + "]")
        time.sleep(1.25)
        print("Player Card" + " [" + str(player_current_card) + "]: " + str(third_player_card) + " " + str((random.choice(suits))) + "[" + str(calculate_card(third_player_card)) + "]")
        time.sleep(1.25)
        
        #Calculate player's total of current cards and outputs the result and adds +1 to current card
        player_total += calculate_card(third_player_card)
        player_current_card += 1
        print("Player Card" + " [" + "Total" + "]: " + str(player_total))

        #Calculates if the player's card total is over 21, and if so calling the bust function
        if player_total > 21:
          time.sleep(1.25)
          player_bust_function(rounds, bet_amount, user_balance)

        #Calculates if the player's card total is equal to 21, and if so outputing "Blackjack" and prompting the continue menu
        if player_total == 21:
          time.sleep(1.25)
          print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
          print("Player Blackjack")
          print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
          print("Player Wins")
          print("------------")
          print("You have won $" + str(user_bet))
          print("------------")
          user_balance += user_bet
          (user_stats["total_user_wins"]) += 1
          (user_stats["total_user_bet_wins"]) += user_bet
          continue_menu(rounds, bet_amount, rounds_completed)

        #Calculates if the player's card total is less than 21, and if so calling the game decision calculator function
        if player_total < 21:
          time.sleep(1.25)
          game_decision_calculator(4, first_player_card, second_player_card, third_player_card, fourth_player_card, dealer_card_1, dealer_card_2, dealer_card_3, dealer_card_4, player_total, rounds, bet_amount, rounds_completed, user_balance)

      #Decides if the user's current card is a 4 and if they decide to hit, and if so clearing the output and proceeding to the "hit" section
      if game_decision == "1" and player_current_card == 4:
        clear_output()

        #Outputs the amount of rounds that are left and how many have been played
        print("│  ╼Balance: $" + str(user_balance) + "╾".ljust(len(str(user_balance))) + "│".ljust(21), "\n│  ╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍".ljust(6) + "  │".ljust(21), "\n")
        print("Round:", rounds_completed, "out of", rounds)
        print("━━━━━━━━━━━━━━━━━━━━")
        time.sleep(1.25)

        #Outputs the dealer's first card with it's total
        print("Dealer Card [1]:", str(dealer_card_1) + " " + str((random.choice(suits))) + "[" + str(calculate_card(dealer_card_1)) + "]")
        time.sleep(1.25)

        #Calculate player's total of current cards and outputs the result
        print("Dealer Card" + " [" + "Total" + "]: " + str(calculate_card(dealer_card_1)))
        print("---------------------")
        time.sleep(1.25)

        #Outputs the players's first, second and third card with their total and adds an addition fourth player card
        print("Player Card [1]:", str(first_player_card) + " " + str((random.choice(suits))) + "[" + str(calculate_card(first_player_card)) + "]")
        time.sleep(1.25)
        print("Player Card [2]:", str(second_player_card) + " " + str((random.choice(suits))) + "[" + str(calculate_card(second_player_card)) + "]")
        time.sleep(1.25)
        print("Player Card [3]:", str(third_player_card) + " " + str((random.choice(suits))) + "[" + str(calculate_card(third_player_card)) + "]")
        time.sleep(1.25)
        print("Player Card" + " [" + str(player_current_card) + "]: " + str(fourth_player_card) + " " + str((random.choice(suits))) + "[" + str(calculate_card(fourth_player_card)) + "]")
        time.sleep(1.25)

        #Calculate player's total of current cards and outputs the result
        player_total += calculate_card(fourth_player_card)
        print("Player Card" + " [" + "Total" + "]: " + str(player_total))

        #Calculates if the player's card total is over 21, and if so calling the bust function
        if player_total > 21:
            time.sleep(1.25)
            player_bust_function(rounds, bet_amount, user_balance)

        #Calculates if the player's card total is equal to 21, and if so outputing "Blackjack" and prompting the continue menu
        if player_total == 21:
            time.sleep(1.25)
            print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
            print("Player Blackjack")
            print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
            print("Player Wins")
            print("------------")
            print("You have won $" + str(user_bet))
            print("------------")
            user_balance += user_bet
            (user_stats["total_user_wins"]) += 1
            (user_stats["total_user_bet_wins"]) += user_bet
            continue_menu(rounds, bet_amount, rounds_completed)

        #Calculates if the player's card total is less than 21, and if so calling the game decision calculator function
        if player_total < 21:
            game_decision_calculator(4, first_player_card, second_player_card, third_player_card, fourth_player_card, dealer_card_1, dealer_card_2, dealer_card_3, dealer_card_4, player_total, rounds, bet_amount, rounds_completed, user_balance)

      #Decides if player selected to "Stand" and if player current card is 3, and if so calculates all dealer cards and calls the stand function
      if game_decision == "2" and player_current_card == 3:

        #Calculates all dealer cards
        dealer_card_1 = calculate_card(dealer_card_1)
        dealer_card_2 = calculate_card(dealer_card_2)
        dealer_card_3 = calculate_card(dealer_card_3)
        dealer_card_4 = calculate_card(dealer_card_4)

        #Calls the player stand function
        player_stand_function(dealer_card_1, dealer_card_2, dealer_card_3, dealer_card_4, player_total, rounds, player_current_card, first_player_card, second_player_card, third_player_card, fourth_player_card, player_total, rounds_completed, bet_amount)
        time.sleep(25) 

      #Decides if player selected to "Stand" and if player current card is 4, and if so calculates all dealer cards and calls the stand function
      if game_decision == "2" and player_current_card == 4:
        
        #Calculates all dealer cards
        dealer_card_1 = calculate_card(dealer_card_1)
        dealer_card_2 = calculate_card(dealer_card_2)
        dealer_card_3 = calculate_card(dealer_card_3)
        dealer_card_4 = calculate_card(dealer_card_4)

        #Calls the player stand function
        player_stand_function(dealer_card_1, dealer_card_2, dealer_card_3, dealer_card_4, player_total, rounds, player_current_card, first_player_card, second_player_card, third_player_card, fourth_player_card, player_total, rounds_completed, bet_amount)
        time.sleep(25)

      #Decides if an incorrect input is entered and re-calls the game decision calculator
      else:
        print("Invalid Input")
        time.sleep(2)
        clear_output()

        #Calls game decision calculator
        game_decision_calculator(player_current_card, first_player_card, second_player_card, third_player_card, fourth_player_card, dealer_card_1, dealer_card_2, dealer_card_3, dealer_card_4, player_total, rounds, bet_amount, rounds_completed, user_balance)
      clear_output()

#The game function, first starts the game by outputting user cards and calling the game decision calculator
def game(rounds, bet_amount):
  bet_amount = bet_amount
  global user_balance
  global round_ended
  global rounds_completed
  
  #Defines dealer cards from 1 to 4 in variables that are valued in a random card value
  dealer_card_1 = (random.choice(cards))
  dealer_card_2 = (random.choice(cards))
  dealer_card_3 = (random.choice(cards))
  dealer_card_4 = (random.choice(cards))

  #Defines player cards from 1 to 4 in variables that are valued in a random card value
  player_card_1 = (random.choice(cards)) 
  player_card_2 = (random.choice(cards))
  player_card_3 = (random.choice(cards))
  player_card_4 = (random.choice(cards))

  #Defines player and dealer cards for later use
  dealer_card_total = 0
  player_card_total = 0

  #Decides if players rounds have finished, and if so reseting rounds completed
  if round_ended == True:
    rounds_completed = 0
    round_ended = False

  #Adding a round to rounds that the user has completed, and adding this same information to user stats
  rounds_completed += 1
  (user_stats["total_user_rounds"]) += 1

  #Outputs the amount of rounds that are left and how many have been played
  print("│  ╼Balance: $" + str(user_balance) + "╾".ljust(len(str(user_balance))) + "│".ljust(21), "\n│  ╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍".ljust(6) + "  │".ljust(21), "\n")
  print("Round:", rounds_completed, "out of", rounds)
  print("━━━━━━━━━━━━━━━━━━━━")
  time.sleep(1.25)

  #Outputs the dealer's first card with it's total
  print("Dealer Card [1]:", str(dealer_card_1) + " " + str((random.choice(suits))) + "[" + str(calculate_card(dealer_card_1)) + "]")
  dealer_card_total += calculate_card(dealer_card_1)
  time.sleep(1.25)
  print("Dealer Card" + " [" + "Total" + "]: " + str(calculate_card(dealer_card_1)))
  time.sleep(1.25)
  print("-----------------")

  #Outputs the player's first and second cards with it's total
  print("Player Card [1]:", str(player_card_1) + " " + str((random.choice(suits))) + "[" + str(calculate_card(player_card_1)) + "]")
  player_card_total += calculate_card(player_card_1)
  time.sleep(1.25)
  print("Player Card [2]:", str(player_card_2) + " " + str((random.choice(suits))) + "[" + str(calculate_card(player_card_2)) + "]")
  player_card_total += calculate_card(player_card_2)
  time.sleep(1.25)
  print("Player Card" + " [" + "Total" + "]: " + str(player_card_total))

  #Calculates if the player's card total is equal to 21, and if so outputing "Blackjack" and prompting the continue menu
  if player_card_total == 21:
    time.sleep(1.25)
    print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
    print("Player Blackjack")
    print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
    print("Player Wins")
    print("------------")
    print("You have won $" + str(user_bet * 1.5))
    print("------------")
    user_balance += user_bet * 1.5
    (user_stats["total_user_wins"]) += 1
    (user_stats["total_user_bet_wins"]) += user_bet * 1.5
    continue_menu(rounds, bet_amount, rounds_completed)

  #Calculates if the player's card total is less than 21, and if so calling the game decision calculator function
  if player_card_total < 21:
    game_decision_calculator(3, player_card_1, player_card_2, player_card_3, player_card_4, dealer_card_1, dealer_card_2, dealer_card_3, dealer_card_4, player_card_total, rounds, bet_amount, rounds_completed, user_balance)

#The update balance function allows the user to add any amount to their balance from the main menu
def update_balance():
  global user_balance
  global temp_user_balance
  global user_balance_update
  
  #Outputs the selection menu of which the user can choose how much they would like to add to their balance, including a custom amount
  print("│  ╼Balance: $" + str(user_balance) + "╾".ljust(len(str(user_balance))) + "│".ljust(21), "\n│  ╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍".ljust(6) + "  │".ljust(21), "\n")
  print("Select amount to add:")
  print("│  1 - $25".ljust(21), "│".ljust(21))
  print("│  2 - $100".ljust(21), "│".ljust(21))
  print("│  3 - $250".ljust(21), "│".ljust(21))
  print("│  4 - $500".ljust(21), "│".ljust(21))
  print("│  5 - $1000".ljust(21), "│".ljust(21))
  print("│  6 - Custom Amount".ljust(21), "│".ljust(21))

  #Reads the user's input and add's the correct bet amount accordingly, with built it redundancy if the user selects a incorrect option, and then returns to the main menu
  user_balance_update = readchar()
  if user_balance_update == "1":
    user_balance += 25
    clear_output()
    main_menu()
  if user_balance_update == "2":
    user_balance += 100
    clear_output()
    main_menu()
  if user_balance_update == "3":
    user_balance += 250
    clear_output()
    main_menu()
  if user_balance_update == "4":
    user_balance += 500
    clear_output()
    main_menu()
  if user_balance_update == "5":
    user_balance += 1000
    clear_output()
    main_menu()
  if user_balance_update == "6":
    temp_user_balance = input("Enter: ")
    while temp_user_balance.isdigit() != True:
      print("Invalid Input")
      time.sleep(2)
      clear_output()
      temp_user_balance = 0
      temp_user_balance = (input("Enter: "))
    temp_user_balance = int(temp_user_balance)
    user_balance += temp_user_balance
    clear_output()
    main_menu()
  else:
    print("Invalid Input")
    time.sleep(2)
    clear_output()
    update_balance()

#The statistics function allows the user to view their total past statistics
def statistics():

  #Outputs the menu that displays to the user their total past statistics
  print("│  ╼Balance: $" + str(user_balance) + "╾".ljust(len(str(user_balance))) + "│".ljust(21), "\n│  ╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍".ljust(6) + "  │".ljust(21), "\n")
  print("Player Statistics:")
  print("│  Total User Rounds - " + str((user_stats["total_user_rounds"])).ljust(11), "│".ljust(21))
  print("│  Total User Wins - " + str((user_stats["total_user_wins"])).ljust(13), "│".ljust(21))
  print("│  Total User Betting Wins - $" + str((user_stats["total_user_bet_wins"])).ljust(4), "│".ljust(21))
  print("│  Total User Loses - " + str((user_stats["total_user_loses"])).ljust(12), "│".ljust(12))
  print("│  Total User Betting Loses - $" + str((user_stats["total_user_bet_loses"])).ljust(3), "│".ljust(21))

  #Outputs that the user needs to press "1" to return back to the main menu 
  print(" \n│  1 - Main Menu".ljust(2), "│".ljust(21))
 
  #Decides if user key pressed "1" and if so bringing the user back to the main menu
  main_menu_stats = readchar()
  if main_menu_stats == "1":
    clear_output()
    main_menu()

  #Decides if user made an incorrect key press input and reloading the statistics menu
  else:
    print("Invalid Input")
    time.sleep(2)
    clear_output()
    statistics()
  clear_output()
  main_menu()

#The credits function displays to the user the credits of the program
def credits():

  #Outputs the menu that displays to the user the program credits
  print("│  ╼Balance: $" + str(user_balance) + "╾".ljust(len(str(user_balance))) + "│".ljust(21), "\n│  ╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍".ljust(6) + "  │".ljust(21), "\n")
  print("Game Credits:")
  print("│  Project Lead & Developer - Michael Mondaini".ljust(21), "│".ljust(21))
  print("│  Game Author - Miguel de Cervantes".ljust(46), "│".ljust(30))

  #Outputs that the user needs to press "1" to return back to the main menu 
  print(" \n│  1 - Main Menu".ljust(2), "│".ljust(21))
  main_menu_credits = readchar()

  #Decides if user key pressed "1" and if so bringing the user back to the main menu
  if main_menu_credits == "1":
    clear_output()
    main_menu()

  #Decides if user made an incorrect key press input and reloading the credits menu
  else:
    print("Invalid Input")
    time.sleep(2)
    clear_output()
    credits()
  clear_output()
  main_menu()
  
#The main menu function outputs a selection menu where the user can select what they would like to do within the program
def main_menu():
  global user_balance

  #Outputs the selection menu of which the user can choose what they want to do within the program
  print("│  ╼Balance: $" + str(user_balance) + "╾".ljust(len(str(user_balance))) + "│".ljust(21), "\n│  ╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍".ljust(6) + "  │".ljust(21), "\n")
  print("│  1 - Play".ljust(21), "│".ljust(21))
  print("│  2 - Update Balance".ljust(21), "│".ljust(21))
  print("│  3 - Statistics".ljust(21), "│".ljust(21))
  print("│  4 - Credits".ljust(21), "│".ljust(21))
  print("│  5 - Exit".ljust(21), "│".ljust(21))

  #Reads the user's input and redirects the user to the correct place accordingly, with built it redundancy if the user selects a incorrect option
  main_menu = readchar()
  if main_menu == "1":
    clear_output()
    game_count()
  elif main_menu == "2":
    clear_output()
    update_balance()
  elif main_menu == "3":
    clear_output()
    statistics()
  elif main_menu == "4":
    clear_output()
    credits()
  elif main_menu == "5":
    clear_output()
    clear_output()
    exit()
  else:
    print("Invalid Input")
    time.sleep(2)
    clear_output()
    from main.py import main_menu
    print(main_menu)

#Outputs to the user a gretting, then calls the main menu function
    
print("Welcome to Blackjack!\n━━━━━━━━━━━━━━━━━━━━━━━━\nYour starting balance is $1500.\n━━━━━━━━━━━━━━━━━━━━━━━━\nGame will start shortly.")
time.sleep(5)
clear_output()
main_menu()
