
import numpy as np

# play randomly

class Bot:
  def __init__(self, playerid):
    self.name = 'random'
    self.playerid = playerid

  def play(self, game_state=None):
    p = np.random.choice(['r', 'p', 's'])
    return p

