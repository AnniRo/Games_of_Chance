import random

# Current amount of money
money = 100


# 1st game of chance: flip coin
def flip_coin():
  
  print('\nGame: Coin Flip\n')

  # Setting bet
  while True:
    bet = input('Set your bet. How much?: ')

    global money

    if int(bet) <= 0:
      print('Negative amount of money or no money is no bet! Set your bet right.')
      continue

    elif int(bet) > money:
      print('You played more money than you have.')
      continue 

    else:
      break

  # Request user to guess
  while True:    
    guess = input('Heads or Tails? Type 1 for Heads or type 2 for Tails: ')

    if int(guess) > 2 or int(guess) == 0:
      print(' You typed an incorrect value. Try again.\n')
      continue

    else:
      break  

  flip = random.randint(1, 2)

  if guess == str(flip):
      print('You won %s!' % bet)
      money += int(bet)
      return 'Your current amount of money is %s. \n' % money

  else:
      print('You lost -%s.' % bet)
      money -= int(bet)
      return 'Your current amount of money is %s. \n' % money



# 2nd game of chance: Cho-Han
def cho_han():

  print('\nGame: Cho-Han\n')

  # Setting bet
  while True:
    bet = input('Set your bet. How much?: ')

    global money

    if int(bet) <= 0:
      print('Negative amount of money or no money is no bet! Set your bet right.')
      continue

    elif int(bet) > money:
      print('You played more money than you have.')
      continue 

    else:
      break

  # Request user to guess   
  guess = input('Even or Odd?: ')

  guess.lower() 

  roll_dice1 = random.randint(1, 6)
  roll_dice2 = random.randint(1,6)

  result = roll_dice1 + roll_dice2

  if result % 2 == 0 and guess == 'even':
    print('Result of dice rolls: %s.' % result)
    print('You won %s!' % bet)
    money += int(bet)
    return 'Your current amount of money is %s.\n' % money

  elif result % 2 != 0 and guess == 'odd':
    print('Result of dice rolls: %s.' % result)
    print('You won %s!' % bet)
    money += int(bet)
    return 'Your current amount of money is %s.\n' % money

  else:
    print('Result of dice rolls: %s.' % result)
    print('You lost -%s.' % bet)
    money -= int(bet)
    return 'Your current amount of money is %s.\n' % money



#3d game of chance: Pick a card
def pick_a_card():
  
  print('\nGame: Pick a card\n')

  print('The higher card wins.\n')

  global money

  # Setting bet
  while True:
    your_bet = input('Set your bet. How much?: ')

    if int(your_bet) <= 0:
      print('Negative amount of money or no money is no bet! Set your bet right.')
      continue

    elif int(your_bet) >= money:
      print('You played more money than you have.')
      continue  

    else:
      break

  # Define an empty list to append the drawn cards
  drawn_cards = []
  # Create a 52-card deck
  card_number = list(range(1,14))*4
  card_type = ['diamonds', 'clubs', 'hearts', 'spades']*13
  deck = list(zip(card_number, card_type))

  # Pick a random card from the deck and append it to the drawn cards list
  card_1 = random.randint(0, len(deck) - 1)
  drawn_cards.append(deck[card_1])
  # Remove the card from the deck
  del(deck[card_1])

  # Repeat the above for the second player
  card_2 = random.randint(0, len(deck) - 1)
  drawn_cards.append(deck[card_2])
  del(deck[card_2])

  your_pick = drawn_cards[0]
  player2_pick = drawn_cards[1]   
  
  print('\nYou picked: {card1}\n\nPlayer 2 picked: {card2}\n'.format(card1=your_pick,card2=player2_pick))

   
  if your_pick > player2_pick:
      print('You won %s!' % your_bet)
      money += int(your_bet)
      return 'Your current amount of money is %s.\n' % money

  elif your_pick < player2_pick:
      print('You lost -%s.' % your_bet) 
      money -= int(your_bet)
      return 'Your current amount of money is %s.\n' % money

  else:
      print('It\'s a tie!')
      return 0
            


#4th game of chance: Roulette
def roulette():

  print('\nGame: Roulette\n')

  # Setting bet
  while True:
    bet = input('Set your bet. How much?: ')

    global money

    if int(bet) <= 0:
      print('Negative amount of money or no money is no bet! Set your bet right.')
      continue

    elif int(bet) > money:
      print('You played more money than you have.')
      continue 

    else:
      break

  # Request user to guess   
  guess = input('Even or Odd? or Choose number: ')

  guess.lower() 

  number = random.randint(1, 37)

  if number == 37:
    print('\nThe ball landed on 00\n')
  else:  
    print('\nThe ball landed on number %s.\n' % number)

  if number % 2 == 0 and guess == 'even' and number != 0:
    print('You won %s!' % bet)
    money += int(bet)
    return 'Your current amount of money is %s.\n' % money

  elif number % 2 != 0 and guess == 'odd' and number != 37:
    print('You won %s!' % bet)
    money += int(bet)
    return 'Your current amount of money is %s.\n' % money

  elif number == guess:
    bet = 2 * int(bet)
    print('You won double the bet! You won: %s!' % bet)
    money += int(bet)
    return 'Your current amount of money is %s.\n' % money

  else:
    print('You lost -%s.' % bet)
    money -= int(bet)
    return 'Your current amount of money is %s.\n' % money



# Define function to select a game
def choose_game():

  global money

  while True:
      selection = input(('Select Game: \n' 
                        'Type 1 to play Flip Coin \n' 
                        'Type 2 to play Cho-Han \n'  
                        'Type 3 to play Pick a card \n'
                        'Type 4 to play Roulette \n'
                        'Type anything else to leave \n'))                  

      if selection == '1':
        print(flip_coin())
        continue
                        
      elif selection == '2':
        print(cho_han())
        continue

      elif selection == '3':
        print(pick_a_card())
        continue
        
      elif selection == '4':
        print(roulette())
        continue
    
      else:
        return 'See yaa!!'
      
       
print(choose_game())        
  