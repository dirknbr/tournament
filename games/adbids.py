
# get vector of pcvr and pvalue, both bids submit bid vector
# bigger bid wins the user
# max sum profit wins

import numpy as np

class AdBids:
  def __init__(self):
    self.done = False
    self.n = 100
    self.pcvr = np.random.uniform(.1, .5, self.n) # avg .3
    self.pvalue = np.maximum(0, 2 + self.pcvr + np.random.normal(0, 1, self.n)) 
    self.state = (self.pcvr, self.pvalue)

  def play_round(self, bot0, bot1):
    # bids exceed 0
    assert np.all(bot0 > 0) and np.all(bot1 > 0)
    assert len(bot0) == self.n and len(bot1) == self.n
    conv = np.random.binomial(1, self.pcvr)
    value = np.maximum(0, np.random.normal(self.pvalue, .5))
    # in case of tie no win
    users0 = [i for i in range(self.n) if bot0[i] > bot1[i]]
    users1 = [i for i in range(self.n) if bot1[i] > bot0[i]]
    cost0 = sum(bot0[users0])
    cost1 = sum(bot1[users1])
    rev0 = sum((conv * value)[users0])
    rev1 = sum((conv * value)[users1])
    self.profit = [rev0 - cost0, rev1 - cost1]
    self.done = True

  def is_done(self):
    return self.done

  def winner(self):
    return np.argmax(self.profit)

  def get_state(self):
    return self.state

