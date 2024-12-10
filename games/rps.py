
class RPS:
  def __init__(self):
    self.done = False
    self.wins = [0, 0] # bot0, bot1
    self.state = [[], []] # log of plays
    self.maxgames = 10 # avoid infinite ties

  def play_round(self, bot0, bot1):
    # return the winner
    self.state[0].append(bot0)
    self.state[1].append(bot1)
    if bot0 == bot1:
      return None # tie
    elif ((bot0 == 'r' and bot1 == 's') or (bot0 == 's' and bot1 == 'p') or (bot0 == 'p' and bot1 == 'r')):
      self.wins[0] += 1
      return 0
    else:
      self.wins[1] += 1
      return 1

  def is_done(self):
    if len(self.state[0]) == self.maxgames:
      self.done = True
    # best of 3
    if max(self.wins) == 2 and max(self.wins) > min(self.wins):
      self.done = True
    return self.done

  def winner(self):
    if self.done:
      if 2 in self.wins:
        return self.wins.index(2)
      else:
        return None

  def get_state(self):
    return self.state





