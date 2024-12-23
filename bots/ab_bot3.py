
# ad bids bot: bid high for the top n that likely convert, 0 otherwise

import numpy as np

class Bot:
  def __init__(self, playerid):
    self.name = ''
    self.playerid = playerid

  def play(self, game_state=None):
    mean_cvr = game_state[0].mean()
    n = len(game_state[0])
    users = (game_state[0] > mean_cvr)
    bid = np.zeros(n)
    bid[users] = game_state[1][users] * .5
    return np.maximum(.0001, bid)


