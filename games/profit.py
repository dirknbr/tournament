
# we have an uncertain demand function
# we reveal 5 (price, demand) pairs
# bots set prices (blindly) and bot with highest profit wins

import numpy as np

class Profit:
  def __init__(self):
    self.done = False
    self.unit_cost = np.random.uniform(.1, .3)
    self.__a = np.random.uniform(.1, .9, 2)
    # publish random price and demand pairs 
    self.prices = np.random.uniform(.2, 1, 5)
    self.demand = self.__demand(self.prices)
    pd = np.zeros((5, 2))
    pd[:, 0] = self.prices
    pd[:, 1] = self.demand
    self.state = (pd, self.unit_cost)
    self.prof = [0, 0]

  def __demand(self, p):
    # noisy 
    return np.maximum(0, self.__a[0] * np.exp(- self.__a[1] * p) + np.random.normal(0, .2, len(p)))

  def play_round(self, bot0, bot1):
    # blow out single prices to 100 obs, so noise effect is reduced 
    assert bot0 > 0 and bot1 > 0
    p0 = np.ones(100) * bot0
    p1 = np.ones(100) * bot1
    d0 = self.__demand(p0)
    d1 = self.__demand(p1)
    self.prof[0] = sum(d0 * (p0 - self.unit_cost))
    self.prof[1] = sum(d1 * (p1 - self.unit_cost))
    self.done = True

  def is_done(self):
    return self.done

  def winner(self):
    return np.argmax(self.prof)

  def get_state(self):
    return self.state

