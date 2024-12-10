
from rps import *

import unittest

class TestRPS(unittest.TestCase):

  def test_full_game(self):
    bot0, bot1 = 'r', 'p'
    game = RPS()
    while not game.is_done():
      game.play_round(bot0, bot1)
    # print(game.winner(), game.get_state(), game.wins)
    self.assertEqual(game.winner(), 1)


if __name__ == '__main__':
  unittest.main()