
# always play rock

class Bot:
  def __init__(self, playerid):
    self.name = 'rock'
    self.playerid = playerid

  def play(self, game_state=None):
    return 'r'

