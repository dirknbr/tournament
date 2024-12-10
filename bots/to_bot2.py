
# draw two cards

class Bot:
  def __init__(self, playerid):
    self.name = ''
    self.playerid = playerid

  def play(self, game_state=None):
    if len(game_state['state'][self.playerid]) < 2:
      return 'card'
    else:
      return 'hold'

