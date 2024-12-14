
import numpy as np

class Bot:
  def __init__(self, playerid):
    self.name = ''
    self.playerid = playerid
    # self.pred = []
    self.total = np.zeros(2) # so we can do a diff

  def play(self, game_state=None):
    if len(game_state['state'][0]) == 0: # first guess
      x = np.exp(np.random.normal(2, 1))
    else:
      # get the last round error
      total_diff = list(game_state['total'] - np.array(self.total))
      minid = total_diff.index(min(total_diff))
      # guess around the last best pred
      x = np.random.normal(game_state['state'][minid][-1], 1)
    # pred.append(x)
    self.total = game_state['total']
    return x


