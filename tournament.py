
import os
from games.rps import *
from games.twentyone import *
from games.prednext import *
from games.mastermind import *
import numpy as np

# get all the file names in the bots folder
# import each file and get the bot class
# choose 2 random players and let them play

ngames = 100

def read_py_files_in_folder(folder_path, prefix):
  py_files = []
  for filename in os.listdir(folder_path):
    if filename.endswith(".py") and filename.startswith(prefix):
      file_path = os.path.join(folder_path, filename)
      py_files.append(file_path)
  return py_files

def read_file_make_bot(file_name):
  with open(file_name, 'r') as f:
    code = f.read()
  return code
  
# change prefix
files = read_py_files_in_folder('bots/', 'pn')
print(files)

stats = {f: [0, 0, 0] for f in files} # [wins, ties, games]

for g in range(ngames):
  print(g)
  np.random.shuffle(files)

  code = read_file_make_bot(files[0])
  exec(code)
  bot0 = Bot(0)

  code = read_file_make_bot(files[1])
  exec(code)
  bot1 = Bot(1)

  # choose game
  # game = TwentyOne()
  # game = RPS()
  game = PredNext()
  # game = Mastermind()

  while not game.is_done():
    game_state = game.get_state()
    game.play_round(bot0.play(game_state), bot1.play(game_state))
    # print(game_state)

  winner = game.winner()
  if winner is not None:
    stats[files[winner]][0] += 1
  else: # it's a tie
    stats[files[0]][1] += 1
    stats[files[1]][1] += 1

  stats[files[0]][2] += 1
  stats[files[1]][2] += 1

for k in stats.keys():
  # calc win %
  print(k, stats[k], stats[k][0] / stats[k][2])
