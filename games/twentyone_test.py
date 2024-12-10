
from twentyone import *

import unittest

class TestTwentyOne(unittest.TestCase):

  def test_full_game(self):
    np.random.seed(22)
    game = TwentyOne()
    bot0, bot1 = 'card', 'card'
    while not game.is_done():
      game.play_round(bot0, bot1)
    print(game.state, game.total, game.winner())
    self.assertEqual(game.winner(), 1)


if __name__ == '__main__':
  unittest.main()