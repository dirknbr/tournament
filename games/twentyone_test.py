
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

  def test_correct_winner(self):
    game = TwentyOne()
    game.total = [10, 10]
    winner = game.winner()
    self.assertEqual(winner, None)
    game.total = [21, 10]
    winner = game.winner()
    self.assertEqual(winner, 0)
    game.total = [22, 22]
    winner = game.winner()
    self.assertEqual(winner, None)
    game.total = [22, 20]
    winner = game.winner()
    self.assertEqual(winner, 1)



if __name__ == '__main__':
  unittest.main()
