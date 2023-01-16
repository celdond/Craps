import dice as d

class play_game:

  def __init__(self, x):
    self.dice = x
    self.point = None
    self.bankroll = 0

  def first_rolls(self) -> str:
    first_roll = self.dice.roll()
    if first_roll in [2, 3]:
      return 'Loss'
    elif first_roll == 12:
      return '12'
    elif first_roll in [7,11]:
      return 'Won'
    else:
      self.point = first_roll
      return 'Point'

  def sub_rolls(self) -> str:
    sub_roll = self.dice.roll()
    if sub_roll == self.point:
      value = 'Won'
      self.point = None
    elif sub_roll == 7:
      value = 'Loss'
      self.point = None
    else:
      value = 'Try'
    return value

  #This function uses the above two functions until full play is over
  def non_interactive(self):
    first = self.first_rolls()
    if first in ['Loss', '12', 'Won']:
      return first
    else:
      while True:
        sub = self.sub_rolls()
        if sub in ['Loss', 'Won']:
          break
      return sub

  #Only for probability of winning a pass bet
  def monte_carlo_pass(self):
    number_wins = 0
    for x in range(1000000):
      i = self.non_interactive()
      if i == 'Won':
        number_wins += 1
    return float(number_wins/1000000)
  
  #Only for probability of winning a no pass bet
  def monte_carlo_no_pass(self):
    number_losses = 0
    number_wins = 0
    for x in range(1000000):
      i = self.non_interactive()
      if i == 'Loss':
        number_losses += 1
      elif i == 'Won':
        number_wins += 1
    return float(number_losses/(number_losses + number_wins))
    
def interactive_game(play_game: play_game):

    print('Every chip is a dollar!')
    try:
      play_game.bankroll += int(input('How many do you want?\n'))
    except:
      print("No no, you must tell me a NUMBER.  Try again another time.\n")
      return

    if play_game.bankroll == 0:
      print('Alrighty. Come back to the table when you are ready.')
      return

    while True:
      x = True
      if play_game.bankroll == 0:
        print('Ah, you are out of chips.')
        print('Talk to me if you want more to keep playing.')
        break

      try:
        bet = int(input('Place your bets!\n'))
      except:
        print("Now that is not a number, now is it?\n")
        continue
      
      if bet == 0:
        print('Thanks for playing, come back anytime.')
        print('Remaining chips: {}\n'.format(play_game.bankroll))
        break

      input('Alright, go ahead and roll the die.\n')
      first_result = play_game.first_rolls()
      play_game.dice.display_die()

      if first_result == 'Won':
        print('Bet won!\n')
        play_game.bankroll += bet
        print('Current bankroll: {}'.format(play_game.bankroll))

      elif first_result == 'Loss' or first_result == '12':
        print('Ah, bet lost.\n')
        play_game.bankroll -= bet
        print('Current bankroll: {}'.format(play_game.bankroll))

      #Section is used after first roll, but similar concept
      else:
        while x == True:
          print('Trying for {}, go ahead and roll again.'.format(play_game.point))
          input('')
          sub_result = play_game.sub_rolls()
          play_game.dice.display_die()

          if sub_result == 'Won':
            print('Bet won!\n')
            play_game.bankroll += bet
            print('Current bankroll: {}'.format(play_game.bankroll))
            x = False

          elif sub_result == 'Loss':
            print('Ah, bet lost.')
            play_game.bankroll -= bet
            print('Current bankroll: {}\n'.format(play_game.bankroll))
            x = False