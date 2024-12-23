
# ad bids bot: bid conv * cvr + noise

import numpy as np

class Bot:
  def __init__(self, playerid):
    self.name = ''
    self.playerid = playerid

  def play(self, game_state=None):
    x = game_state[0] * game_state[1]
    n = len(game_state[0])
    return np.maximum(.0001, np.random.normal(x, .1, n))


