import random
wallet = []


def wallet_balance():
  if wallet == [] or wallet == 0:
    try:
      balance = int(input("Your wallet is currently empty. You'll need some money to play. How much would you like to add?\n "))
      
      if balance >= 1:
        wallet.append(balance)
        user_function()
      
      else:
        print("Please enter a whole dollar amount.\n")
        wallet_balance()
    
    except ValueError:
      print("Please enter a whole dollar amount.\n")
      wallet_balance()
  else:
    if sum(wallet) > 0:
      user_input = input("Would you like to continue with, add to, or cashout out your wallet? 1.Continue, 2.Add, 3.Cashout\n")
      
      if user_input == "1":
        user_function()

      elif user_input == "2":
        add_to_function()

      else:
        print(f"Here is what you are leaving with: ${sum(wallet)}\n")
        



def user_function():
  try:
    user_wager = int(input("Are you ready to play Roulette? How much would you like to wager?\n"))

    if user_wager <= sum(wallet):
      wallet.append(user_wager * -1)

    else:
      print("You do not have enough to wager that amount.\n")
      user_function()
  
  except ValueError:
    print("Please enter a whole number to wager\n")
    user_function()

  if user_wager > 0:
    user_validation(user_wager)

  else:
    print("Please enter an ammount greater than zero.\n")
    user_function()


def user_validation(user_wager): 
  user_input = input("Choose a color to bet on: 1 = red, 2 = black...\n ")
  if user_input == "1":
    guess_checker(user_input, user_wager)

  elif user_input == "2":
    guess_checker(user_input, user_wager)

  else:
    print("Please choose 1 or 2.\n")
    user_validation(user_wager)


def guess_checker(user_choice, user_wager):
  random_color = random.randrange(1, 3)
  user_pick = int(user_choice)

  if random_color == 1:
    print("The card is red!\n")

    if user_pick == random_color:
      wallet.append(user_wager * 2)
      print("You win!\n")
      balance_display()


    else:
      print("You lost. Try again!\n")
      balance_display()


  else:
    print("The card is black!\n")

    if user_pick == random_color:
      wallet.append(user_wager * 2)
      print("You win!\n")
      balance_display()

    else:
      print("You lost. Try again!\n")
      balance_display()


def balance_display():
  end_price = sum(wallet)
  print(f"Your new balance is ${str(end_price)}\n")
  wallet_balance()

def add_to_function():
  try:
      user_input = int(input("How much would you like to add to your wallet?"))
      
      if user_input >= 1:
        wallet.append(user_input)
        user_function()
      
      else:
        print("Please enter a whole dollar amount.\n")
        add_to_function()
    
  except ValueError:
    print("Please enter a whole dollar amount.\n")
    add_to_function()


wallet_balance()

