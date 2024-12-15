
import numpy as np

class Bot:
  def __init__(self, playerid):
    self.name = ''
    self.playerid = playerid

  def play(self, game_state=None):
    return ''.join(map(str, list(np.random.randint(0, 10, 4))))


