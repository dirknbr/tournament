
from mastermind import *

import unittest

class TestMastermind(unittest.TestCase):

  def test_correct_guess(self):
    np.random.seed(22)
    game = Mastermind()
    bot0, bot1 = '0123', '5404'
    while not game.is_done():
      game.play_round(bot0, bot1)
    print(game.state, game.winner())
    self.assertEqual(game.winner(), 1)

  def test_wrong_guess(self):
    game = Mastermind()
    bot0, bot1 = '0123', '2345'
    while not game.is_done():
      game.play_round(bot0, bot1)
    print(game.state, game.winner())
    self.assertEqual(game.winner(), None)
    self.assertEqual(len(game.get_state()[0]), 8)

  def test_get_pin_forbidden(self):
    game = Mastermind()
    with self.assertRaises(AttributeError):
      x = game.__pin

  def test_get_check_forbidden(self):
    game = Mastermind()
    with self.assertRaises(AttributeError):
      game.__check('0000')

if __name__ == '__main__':
  unittest.main()