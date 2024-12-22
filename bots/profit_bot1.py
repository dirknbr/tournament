
# profit bot: put price where demand is highest

import numpy as np

class Bot:
  def __init__(self, playerid):
    self.name = ''
    self.playerid = playerid

  def play(self, game_state=None):
    high_demand = np.argmax(game_state[0][:, 1])
    return game_state[0][high_demand, 0]


