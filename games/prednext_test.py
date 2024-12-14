
from prednext import *

import unittest

class TestPredNext(unittest.TestCase):

  def test_full_game(self):
    np.random.seed(22)
    game = PredNext()
    bot0, bot1 = 5, 6
    while not game.is_done():
      game.play_round(bot0, bot1)
    print(game.state, game.total, game.winner())
    self.assertEqual(game.winner(), 1)

  def test_get_mu_forbidden(self):
    np.random.seed(22)
    game = PredNext()
    with self.assertRaises(AttributeError):
      x = game.__mu


if __name__ == '__main__':
  unittest.main()