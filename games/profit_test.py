
from profit import *
import unittest

class TestProfit(unittest.TestCase):

  def test_game(self):
    np.random.seed(44)
    game = Profit()
    bot0, bot1 = .5, .6
    while not game.is_done():
      game.play_round(bot0, bot1)
    print(game.state, game.prof, game.winner())
    self.assertEqual(game.winner(), 1)
    # check if (p, d) has negative corr
    corr = np.corrcoef(game.state[0].T)[0, 1]
    self.assertLess(corr, 0)


  def test_get_a_forbidden(self):
    game = Profit()
    with self.assertRaises(AttributeError):
      x = game.__a


if __name__ == '__main__':
  unittest.main()