
# ad bids bot: p60 of the cvr * conv distribution

import numpy as np

class Bot:
  def __init__(self, playerid):
    self.name = ''
    self.playerid = playerid

  def play(self, game_state=None):
    x = game_state[0] * game_state[1]
    n = len(game_state[0])
    p60 = np.percentile(x, 60)
    return p60 * np.ones(n)


