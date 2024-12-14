
import numpy as np

class Bot:
  def __init__(self, playerid):
    self.name = ''
    self.playerid = playerid

  def play(self, game_state=None):
    return np.exp(np.random.normal(2, 1))


