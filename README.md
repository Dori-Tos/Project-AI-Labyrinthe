# Project-AI-Labyrinthe

This code alllows to run an ai that solves a game of labyrinthe round after round.

## Used dependencies

To download them, type in the console : pip install <dependence_name>

socket
threading
json
time
collections
random

## How the ai works

The (very basic) ai needs the following data to work :

the board, the (free) tile, the positions of the 2 players, the remainig treasures to find for each player,     the target (treasure) of the player and who plays at the moment

With these datas it uses a sequence of funcions to represents itself the game.
Then it iteratively tries multiple moves to see wich suits the situation the best, and with the help of an heuristic it selects wich is, at the same time, the best move for himself and the worst for his adversary.
It does all of the above using the model of the Min Max function.

To send and receive the data it uses a premade server.

## Thank you for using our code !