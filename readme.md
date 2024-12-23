# Tournament

This is a package where we have mulitple bots that can play in 2 player games. Each
bot is defined by a python function. The goal is to create a leaderboard of bots
where we rank bots with high win percentage.

In each game round we pass the game state to the bots.

Each game has the following methods: `play_round`, `winner`, `is_done`, `get_state`.

Each bot has the following method: `play`.

In `tournament.py` relevant bots are paired and games are played to determine the overall
win percentage.

## Games

- rock paper scissors (best of 3)
- game of 21
- guess the next number 5 times, lowest abs diff total wins
- guess a 4 digit pin
- set price to maximise profit (given 5 noisy price and demand pairs)
- ad bids given (pcvr, pvalue), highest bid wins user, highest sum profit wins game
