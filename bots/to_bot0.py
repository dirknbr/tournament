
# draw until 17, then hold

class Bot:
  def __init__(self, playerid):
    self.name = ''
    self.playerid = playerid

  def play(self, game_state=None):
    if game_state['total'][self.playerid] < 17:
      return 'card'
    else:
      return 'hold'

