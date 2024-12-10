
# draw if own value below opp

class Bot:
  def __init__(self, playerid):
    self.name = ''
    self.playerid = playerid

  def play(self, game_state=None):
    own = game_state['total'][self.playerid]
    opp = game_state['total'][1 - self.playerid]
    if own < opp:
      return 'card'
    else:
      return 'hold'

