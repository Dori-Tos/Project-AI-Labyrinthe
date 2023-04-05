import time
from collections import defaultdict
import random

from Network_functions import state
from Network_functions import name

remaining = state.get("remaining")
current = state.get("current")
players = state.get("players")
positions = state.get("positions")
board = state.get("board")

players = name

def movemment_possible(tile):
	N = tile.get("N")
	E = tile.get("E")
	S = tile.get("S")
	W = tile.get("W")
	res = []

	if N == True:
		res.append(N)
	if E == True:
		res.append(E)
	if S == True:
		res.append(S)
	if W == True:
		res.append(W)
	

def distance_current(board, current, player, positions):
	position = positions[player]
	directions = [1, -1, 7, -7]
	
	for i in directions:
		position
	
	

def gameOver(state):
	if winner(state) is not None:
		return True
"""
	empty = 0
	for elem in state:
		if elem is None:
			empty += 1
	return empty == 0
"""
	
def winner(remaining):
	if remaining == 0:
		return players[current]
	else:
	    return None

def heuristic(state, player):
	if gameOver(state):
		theWinner = winner(state)
		if theWinner is None:
			return 0
		if theWinner == player:
			return 1
		return -1
	res = 0
	for tile in board:
		res += lineValue([state[i] for i in tile], player)
	return res

def moves(state):
	res = []
	for i, elem in enumerate(state):
		if elem is None:
			res.append(i)
	
	random.shuffle(res)
	return res

def apply(state, move):
	player = name
	res = list(state)
	res[move] = player
	return res

def negamax(state, player):
	if gameOver(state):
		return -heuristic(state, player), None

	theValue, theMove = float('-inf'), None
	for move in moves(state):
		successor = apply(state, move)
		value, _ = negamax(successor, player%2+1)
		if value > theValue:
			theValue, theMove = value, move
	return -theValue, theMove


def successors(node):
	"""laby = [
		"##########",
		"#        E",
		"# # ######",
		"# #      #",
		"# # # ####",
		"#####    #",
		"#   # ####",
		"# # # #  #",
		"# #      #",
		"##########",
	]"""

	directions = [1, -1, -7, 7]
	res = []
	for i in directions:
		dx = node+i
		if board[dx] in [' ', 'E']:
			res.append(dx)
	return res # Peut renvoyer jusqu'à 4 cases différentes

def the_move_played():
    pass