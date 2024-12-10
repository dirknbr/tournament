
# game of 21, whoever gets 21 or has higher wins
# if you are over 21 you lose

import numpy as np

class TwentyOne:
  def __init__(self):
    self.total = [0, 0]
    self.cards = [i for i in range(2, 12)] + [10, 10, 10]
    self.state = [[], []]
    self.done = False

  def play_round(self, bot0, bot1):
    cards = np.random.choice(self.cards, 2)
    self.state[0].append(bot0)
    self.state[1].append(bot1)
    # actions are (card, hold)
    if bot0 == 'card':
      self.total[0] += cards[0]
    if bot1 == 'card':
      self.total[1] += cards[1]

  def is_done(self):
    # if one is bust or both are hold
    if len(self.state[0]) == 0:
      return False
    if max(self.total) > 21 or (self.state[0][-1] == 'hold' and self.state[1][-1] == 'hold'):
      self.done = True
    return self.done

  def winner(self):
    maxnum = max(self.total)
    minnum = min(self.total)
    # if same or both bust, no winner
    if (maxnum == minnum or minnum > 21):
      return None
    elif maxnum > minnum and maxnum <= 21:
      return self.total.index(maxnum)
    elif maxnum > 21 and minnum <= 21:
      return self.total.index(minnum)

  def get_state(self):
    return {'total': self.total, 'state': self.state}

