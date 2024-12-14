
# use the avg of previous pred

import numpy as np

class Bot:
  def __init__(self, playerid):
    self.name = ''
    self.playerid = playerid

  def play(self, game_state=None):
    if len(game_state['state'][0]) == 0: # first guess
      x = np.exp(np.random.normal(2, 1))
    else:
      preds = np.hstack((game_state['state'][0], game_state['state'][1]))
      x = preds.mean()
    return x


