# Tournament

This is a package where we have mulitple bots that can play in 2 player games. Each
bot is defined by a python function. The goal is to create a leaderboard of bots
where we rank bots with high win percentage.

In each game round we pass the game state to the bots.

Each game has the following methods: `play_round`, `winner`, `is_done`, `get_state`.

Each bot has the following method: `play`.

## Games

- rock paper scissors (best of 3)
- game of 21
- guess the next number 5 times, lowest abs diff wins
