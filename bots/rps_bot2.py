
# play what your opponent played last

class Bot:
  def __init__(self, playerid):
    self.name = 'parrot'
    self.playerid = playerid

  def play(self, game_state):
    if len(game_state[0]) == 0:
      return 'p'
    else:
      return game_state[1 - self.playerid][-1]



