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

def target_finder(board, target):
	for i in board:
		tile = board[i].get(i)
		if tile.get("item") == target:
			return i
	return None

def movement_possible(tile_nbr, board):
	tile = board.get(tile_nbr)
	N = tile.get("N")
	E = tile.get("E")
	S = tile.get("S")
	W = tile.get("W")
	res = []

	if N == True:
		if board.get(tile_nbr-7).get("S") == True:
			res.append("N")
	if E == True:
		if board.get(tile_nbr+1).get("W") == True:
			res.append("E")
	if S == True:
		if board.get(tile_nbr+7).get("N") == True:
			res.append("S")
	if W == True:
		if board.get(tile_nbr-1).get("E") == True:
			res.append("W")
	return res
	
	
def distance_objective(board, target, current, positions):
	position = positions[current]
	directions = [1, -1, 7, -7]
	tile = board.get(position)
	target_tile = target_finder(board, target)

	if movement_possible(position, board) != None:
		for i in directions:
			new_position = position + directions[i]

		
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