
from adbids import *
import unittest

class TestAdBids(unittest.TestCase):

  def test_game(self):
    np.random.seed(44)
    game = AdBids()
    bot0, bot1 = .5 * np.ones(100), .6 * np.ones(100)
    while not game.is_done():
      game.play_round(bot0, bot1)
    print(game.profit, game.winner())
    self.assertEqual(game.winner(), 0)

  def test_wrong_array_raises_error(self):
    game = AdBids()
    bot0, bot1 = .5 * np.ones(2), .6 * np.ones(100)
    with self.assertRaises(AssertionError):
      game.play_round(bot0, bot1)



if __name__ == '__main__':
  unittest.main()