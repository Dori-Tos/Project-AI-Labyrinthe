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

target = 1

board = {
	0 :{
	"N" : False,
	"E" : True,
	"S" : True,
	"W" : False,
	"item" : None
	},
	1 :{
	"N" : False,
	"E" : True,
	"S" : False,
	"W" : True,
	"item" : None
	},
	2 :{
	"N" : False,
	"E" : True,
	"S" : True,
	"W" : True,
	"item" : 1
	},
	3 :{
	"N" : False,
	"E" : True,
	"S" : True,
	"W" : False,
	"item" : 15
	},
	4 :{
	"N" : False,
	"E" : True,
	"S" : True,
	"W" : True,
	"item" : 2
	},
	5 :{
	"N" : True,
	"E" : False,
	"S" : False,
	"W" : True,
	"item" : None
	},
	6 :{
	"N" : False,
	"E" : False,
	"S" : True,
	"W" : True,
	"item" : 6
	},
	7 :{
	"N" : False,
	"E" : False,
	"S" : True,
	"W" : True,
	"item" : 16
	},
	8 :{
	"N" : False,
	"E" : True,
	"S" : False,
	"W" : True,
	"item" : None
	},
	9 :{
	"N" : False,
	"E" : False,
	"S" : True,
	"W" : True,
	"item" : None
	},
	10 :{
	"N" : True,
	"E" : False,
	"S" : True,
	"W" : False,
	"item" : None
	},
	11 :{
	"N" : True,
	"E" : False,
	"S" : True,
	"W" : False,
	"item" : None
	},
	12 :{
	"N" : True,
	"E" : False,
	"S" : True,
	"W" : False,
	"item" : None
	},
	13 :{
	"N" : False,
	"E" : True,
	"S" : False,
	"W" : True,
	"item" : None
	},
	14 :{
	"N" : True,
	"E" : True,
	"S" : True,
	"W" : False,
	"item" : 3
	},
	15 :{
	"N" : False,
	"E" : True,
	"S" : False,
	"W" : True,
	"item" : None
	},
	16 :{
	"N" : True,
	"E" : True,
	"S" : True,
	"W" : False,
	"item" : 4
	},
	17 :{
	"N" : False,
	"E" : False,
	"S" : True,
	"W" : True,
	"item" : None
	},
	18 :{
	"N" : False,
	"E" : True,
	"S" : True,
	"W" : True,
	"item" : 5
	},
	19 :{
	"N" : False,
	"E" : True,
	"S" : True,
	"W" : True,
	"item" : 24
	},
	20 :{
	"N" : True,
	"E" : False,
	"S" : True,
	"W" : True,
	"item" : 6
	},
}

def target_finder(board, target):
	for i in board:
		tile = board.get(i)
		if tile.get("item") != None:
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
		if board.get(tile_nbr-7) != None:
			if board.get(tile_nbr-7).get("S") == True:
				res.append("N")
	if E == True:
		if board.get(tile_nbr+1) != None:
			if board.get(tile_nbr+1).get("W") == True:
				res.append("E")
	if S == True:
		if board.get(tile_nbr+7) != None:
			if board.get(tile_nbr+7).get("N") == True:
				res.append("S")
	if W == True:
		if board.get(tile_nbr-1) != None:
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

def successors(node, board):
	directions = movement_possible(node, board)
	res = []
	for i in directions:
		if i == "N" :
			dx = node - 7
			res.append(dx)
		if i == "E" :
			dx = node + 1
			res.append(dx)
		if i == "S" :
			dx = node + 7
			res.append(dx) 
		if i == "W" :
			dx = node - 1
			res.append(dx)
	return res

from collections import deque

def timeit(fun):
	def wrapper(*args, **kwargs):
		start = time.time()
		res = fun(*args, **kwargs)
		print('Execute in {}s'.format(time.time() - start))
		return res
	return wrapper

@timeit
def BFS(start, target, board):
	q = deque()
	q.append(start)
	parents = {}
	parents[start] = None
	
	while q:
		node = q.popleft()
		if node == target_finder(board, target):
			break
		for successor in successors(node, board):
			if successor not in parents:
				parents[successor] = node
				q.append(successor)
		node = None
		
	res = []
	while node is not None:
		res.append(node)
		node = parents[node]

	return list(reversed(res))

print(BFS(0, target, board))
		
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


def the_move_played():
    pass