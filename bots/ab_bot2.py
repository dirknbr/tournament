
# ad bids bot: 90% of cvr * value

import numpy as np

class Bot:
  def __init__(self, playerid):
    self.name = ''
    self.playerid = playerid

  def play(self, game_state=None):
    x = game_state[0] * game_state[1]
    return np.maximum(.00001, x * .9)


