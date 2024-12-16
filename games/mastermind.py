

import numpy as np

class Mastermind:
  def __init__(self):
    self.done = False
    self.__pin = ''.join(map(str, list(np.random.randint(0, 10, 4))))
    self.guesses = 0
    self.state = [[], []]

  def __count(self, guess):
    # return bulls for exact and cows for right num in wrong pos
    bulls, cows = 0, 0
    for i in range(4):
      if self.__pin[i] == guess[i]:
        bulls += 1
      elif guess[i] in self.__pin:
        cows += 1
    return bulls, cows

  def play_round(self, bot0, bot1):
    # check both are 4 digits long
    assert len(bot0) == 4 and len(bot1) == 4
    b0, c0 = self.__count(bot0)
    b1, c1 = self.__count(bot1)
    if b0 == 4 or b1 == 4: # success
      self.done = True
    self.state[0].append([bot0, b0, c0]) # also record the guess
    self.state[1].append([bot1, b1, c1])
    self.guesses += 1

  def is_done(self):
    # allow up to 8 guesses
    if self.guesses >= 8:
      self.done = True
    return self.done

  def winner(self):
    # assume match happens in last move
    if self.done:
      if self.state[0][-1][1:] == [4, 0] and self.state[1][-1][1:] != [4, 0]:
        return 0
      elif self.state[0][-1][1:] != [4, 0] and self.state[1][-1][1:] == [4, 0]:
        return 1
    # print(self.__pin)
    return None # can be tie

  def get_state(self):
    return self.state

