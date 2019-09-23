import random
wallet = []

def wallet_balance():
    if wallet == []:
        try:
            balance = int(input("Your wallet is currently empty. You'll need some money to play. How much would you like to add?\n "))
            if balance >= 1:
                wallet.append(balance)
                user_function()
            else:
                print("Please enter a whole dollar amount.\n")
                wallet_balance()
        except ValueError:
            print("Please enter a whole dollar amount.")
            wallet_balance()
    else:
        print(f"Your wallet currently has a balance of {wallet}")

def user_function():
  try:
    user_wager = int(input("Are you ready to play Roulette? How much would you like to wager? "))
    wallet.append(user_wager * -1)
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
    else:
      print("You lost. Try again!\n")
  else:
    print("The card is black!\n")
    if user_pick == random_color:
      wallet.append(user_wager * 2)
      print("You win!\n")
    else:
      print("You lost. Try again!\n")




wallet_balance()
end_price = sum(wallet)
print(f"Your new balance is ${str(end_price)}")
