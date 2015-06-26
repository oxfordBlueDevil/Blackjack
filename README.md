# Blackjack Game

We've implemented a multiplayer game of Blackjack.

We've created a simplified version of the game for this project:

1. You can play with 1 - 10 players and 1 Dealer
1. The player can only hit or stay (no split or double down).

Some notes on my implementation:

1. The dealer plays by the rules of hitting at 16 or lower, staying at 17 or higher.
1. The payout for Blackjack is 3:2.
1. The player starts with a fixed amount of money ($100), and is able to play until bankrupt or quitting.


## Code

* In `deck.py` there's a `Card` and a `Deck` class.

## How to test

* `blackjack.py`: Running `python blackjack.py` in the code directory should run a game. Enjoy!


## Further Step
* Implement double down and/or split
