
# profit bot: put unit cost

import numpy as np

class Bot:
  def __init__(self, playerid):
    self.name = ''
    self.playerid = playerid

  def play(self, game_state=None):
    return game_state[1]


