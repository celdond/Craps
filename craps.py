import dice

class play_game:

  def __init__(self, dice):
    self.dice = dice
    self.point = None
    self.bankroll = 0

  def first_rolls(self):
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

  def sub_rolls(self):
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
