
# over 5 rounds bots guess what is the next number
# bot with lowest sum of abs differences wins

import numpy as np

class PredNext:
  def __init__(self):
    self.total = [0, 0]
    self.done = False
    # make mu and sigma private
    self.__mu = np.exp(np.random.normal(2, 1))
    self.__sigma = np.exp(np.random.normal(1, 1))
    self.state = [[], []]

  def play_round(self, bot0, bot1):
    x = np.random.normal(self.__mu, self.__sigma)
    pred = [bot0, bot1]
    for i in [0, 1]:
      self.total[i] += abs(pred[i] - x)
      self.state[i].append(pred[i])

  def is_done(self):
    if len(self.state[0]) == 5:
      self.done = True
    return self.done

  def winner(self):
    return self.total.index(min(self.total))

  def get_state(self):
    return {'total': self.total, 'state': self.state}

