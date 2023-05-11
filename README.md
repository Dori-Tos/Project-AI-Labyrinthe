# Project-AI-Labyrinthe

This code alllows to run an ai that solves a game of labyrinthe round after round.

## Used dependencies

To download them, type in the console : pip install <dependence_name>

- socket
- threading
- json
- time
- collections
- random

## How the ai works

The (very basic) ai needs the following data to work :

the board, the (free) tile, the positions of the 2 players, the remainig treasures to find for each player,     the target (treasure) of the player and who plays at the moment

With these datas it uses a sequence of funcions to represents itself the game.
Then it iteratively tries multiple moves to see wich suits the situation the best, and with the help of an heuristic it selects wich is, at the same time, the best move for himself and the worst for his adversary.
It does all of the above using the model of the Min Max function.

The best move for itself is found by randomly putting the free tile in each gate, then it selects the best move by finding wich gate allows him to go to his target in the minimum of rounds.

The worst move (the best of its adversary) is determined by finding where the closest treasure is to its ennemy, then by iteration finds wich moves blocks the most the way to it.

We also have created a random AI.This other AI is very dumb and places the tile randomly and also randomly moves.

To send and receive the data it uses a premade server.

To use our AI be sure that the tournament server is open and then Run Runner.py and select wich IA you what to use.

## Thank you for using our code !