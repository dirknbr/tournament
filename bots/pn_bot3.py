
# guess 0 and then 40 and then take the mean

import numpy as np

class Bot:
  def __init__(self, playerid):
    self.name = ''
    self.playerid = playerid
    self.max = np.random.normal(np.exp(2), np.exp(1), 1000).max()

  def play(self, game_state=None):
    if len(game_state['state'][0]) == 0: # first guess
      return 0
    elif len(game_state['state'][0]) == 1: # second
      return self.max
    else:
      p0 = game_state['state'][self.playerid][0]
      p1 = self.max - game_state['state'][self.playerid][1]
      return (p0 + p1) / 2


