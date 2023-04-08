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

tile2={
	"N" : True,
	"E" : True,
	"S" : False,
	"W" : True,
	"item" : 24
}

board={
	0:{
		"N" : False,
		"E" : True,
		"S" : True,
		"W" : False,
		"item" : 0
	},
	1:{
		"N" : False,
		"E" : True,
		"S" : False,
		"W" : True,
		"item" : 0
	},
	2:{
		"N" : False,
		"E" : True,
		"S" : True,
		"W" : True,
		"item" : 1
	},
	3:{
		"N" : False,
		"E" : True,
		"S" : False,
		"W" : True,
		"item" : 0
	},
	4:{
		"N" : False,
		"E" : True,
		"S" : True,
		"W" : True,
		"item" : 2
	},
	5:{
		"N" : False,
		"E" : True,
		"S" : False,
		"W" : True,
		"item" : 0
	},
	6:{
		"N" : False,
		"E" : False,
		"S" : True,
		"W" : True,
		"item" : 0
	},
	7:{
		"N" : False,
		"E" : True,
		"S" : True,
		"W" : False,
		"item" : 13
	},
	8:{
		"N" : True,
		"E" : False,
		"S" : True,
		"W" : False,
		"item" : 0
	},
	9:{
		"N" : False,
		"E" : True,
		"S" : True,
		"W" : False,
		"item" : 15
	},
	10:{
		"N" : False,
		"E" : False,
		"S" : True,
		"W" : True,
		"item" : 0
	},
	11:{
		"N" : True,
		"E" : True,
		"S" : False,
		"W" : False,
		"item" : 0
	},
	12:{
		"N" : False,
		"E" : False,
		"S" : True,
		"W" : True,
		"item" : 16
	},
	13:{
		"N" : True,
		"E" : True,
		"S" : False,
		"W" : False,
		"item" : 0
	},
	14:{
		"N" : True,
		"E" : True,
		"S" : True,
		"W" : False,
		"item" : 3
	},
	15:{
		"N" : False,
		"E" : False,
		"S" : True,
		"W" : True,
		"item" : 0
	},
	16:{
		"N" : True,
		"E" : True,
		"S" : True,
		"W" : False,
		"item" : 4
	},
	17:{
		"N" : True,
		"E" : False,
		"S" : False,
		"W" : True,
		"item" : 17
	},
	18:{
		"N" : False,
		"E" : True,
		"S" : True,
		"W" : True,
		"item" : 5
	},
	19:{
		"N" : True,
		"E" : False,
		"S" : True,
		"W" : False,
		"item" : 0
	},
	20:{
		"N" : True,
		"E" : False,
		"S" : True,
		"W" : True,
		"item" : 6
	},
	21:{
		"N" : False,
		"E" : False,
		"S" : True,
		"W" : True,
		"item" : 0
	},
	22:{
		"N" : True,
		"E" : True,
		"S" : False,
		"W" : False,
		"item" : 16
	},
	23:{
		"N" : False,
		"E" : True,
		"S" : True,
		"W" : True,
		"item" : 22
	},
	24:{
		"N" : True,
		"E" : False,
		"S" : True,
		"W" : False,
		"item" : 0
	},
	25:{
		"N" : True,
		"E" : True,
		"S" : True,
		"W" : False,
		"item" : 20
	},
	26:{
		"N" : True,
		"E" : True,
		"S" : False,
		"W" : False,
		"item" : 14
	},
	27:{
		"N" : True,
		"E" : False,
		"S" : True,
		"W" : True,
		"item" : 23
	},
	28:{
		"N" : True,
		"E" : True,
		"S" : True,
		"W" : False,
		"item" : 7
	},
	29:{
		"N" : False,
		"E" : True,
		"S" : False,
		"W" : True,
		"item" : 0
	},
	30:{
		"N" : True,
		"E" : True,
		"S" : True,
		"W" : False,
		"item" : 8
	},
	31:{
		"N" : False,
		"E" : True,
		"S" : True,
		"W" : True,
		"item" : 21
	},
	32:{
		"N" : True,
		"E" : False,
		"S" : True,
		"W" : True,
		"item" : 9
	},
	33:{
		"N" : False,
		"E" : True,
		"S" : False,
		"W" : True,
		"item" : 0
	},
	34:{
		"N" : True,
		"E" : False,
		"S" : True,
		"W" : True,
		"item" : 10
	},
	35:{
		"N" : False,
		"E" : False,
		"S" : True,
		"W" : True,
		"item" : 0
	},
	36:{
		"N" : True,
		"E" : False,
		"S" : True,
		"W" : False,
		"item" : 0
	},
	37:{
		"N" : False,
		"E" : True,
		"S" : True,
		"W" : False,
		"item" : 0
	},
	38:{
		"N" : True,
		"E" : False,
		"S" : False,
		"W" : True,
		"item" : 0
	},
	39:{
		"N" : True,
		"E" : False,
		"S" : True,
		"W" : False,
		"item" : 0
	},
	40:{
		"N" : False,
		"E" : False,
		"S" : True,
		"W" : True,
		"item" : 18
	},
	41:{
		"N" : False,
		"E" : True,
		"S" : False,
		"W" : True,
		"item" : 0
	},
	42:{
		"N" : True,
		"E" : True,
		"S" : False,
		"W" : False,
		"item" : 0
	},
	43:{
		"N" : True,
		"E" : True,
		"S" : False,
		"W" : True,
		"item" : 19
	},
	44:{
		"N" : True,
		"E" : True,
		"S" : False,
		"W" : True,
		"item" : 11
	},
	45:{
		"N" : False,
		"E" : True,
		"S" : False,
		"W" : True,
		"item" : 0
	},
	46:{
		"N" : True,
		"E" : True,
		"S" : False,
		"W" : True,
		"item" : 0
	},
	47:{
		"N" : True,
		"E" : False,
		"S" : False,
		"W" : True,
		"item" : 0
	},
	48:{
		"N" : True,
		"E" : False,
		"S" : False,
		"W" : True,
		"item" : 0
	},
}
def new_board(board,tile,place):
	#crée les board avec les pièces qui ont bougé par rapport à un board et l'emplacement souhaité
	#pre le board et la tile en plus
	#post le board après mouvement
	temp=tile
	if place==1:
		tile=board[43]
		#tester avec update plus propre 1 ligne pour chaque emplacement
		board[43]=board[36]
		board[36]=board[29]
		board[29]=board[22]
		board[22]=board[15]
		board[15]=board[8]
		board[8]=board[1]
		board[1]=temp
	elif place==3:
		tile=board[45]
		board[45]=board[38]
		board[38]=board[31]
		board[31]=board[24]
		board[24]=board[17]
		board[17]=board[10]
		board[10]=board[3]
		board[3]=temp
	elif place==5:
		tile=board[47]
		board[47]=board[40]
		board[40]=board[33]
		board[33]=board[26]
		board[26]=board[19]
		board[19]=board[12]
		board[12]=board[5]
		board[5]=temp
	elif place==7:
		tile=board[13]
		board[13]=board[12]
		board[12]=board[11]
		board[11]=board[10]
		board[10]=board[9]
		board[9]=board[8]
		board[8]=board[7]
		board[7]=temp

	elif place==21:
		tile=board[27]
		board[27]=board[26]
		board[26]=board[25]
		board[25]=board[24]
		board[24]=board[23]
		board[23]=board[22]
		board[22]=board[21]
		board[21]=temp
	
	elif place==35:
		tile=board[41]
		board[41]=board[40]
		board[40]=board[39]
		board[39]=board[38]
		board[38]=board[37]
		board[37]=board[36]
		board[36]=board[35]
		board[35]=temp

	elif place==13:
		tile=board[7]
		board[7]=board[8]
		board[8]=board[9]
		board[9]=board[10]
		board[10]=board[11]
		board[11]=board[12]
		board[12]=board[13]
		board[13]=temp

	elif place==27:
		tile=board[21]
		board[21]=board[22]
		board[22]=board[23]
		board[23]=board[24]
		board[24]=board[25]
		board[25]=board[26]
		board[26]=board[27]
		board[27]=temp

	elif place==41:
		tile=board[35]
		board[35]=board[36]
		board[36]=board[37]
		board[37]=board[38]
		board[38]=board[39]
		board[39]=board[40]
		board[40]=board[41]
		board[41]=temp
	
	elif place==43:
		tile=board[1]
		board[1]=board[8]
		board[8]=board[15]
		board[15]=board[22]
		board[22]=board[29]
		board[29]=board[36]
		board[36]=board[43]
		board[43]=temp

	elif place==45:
		tile=board[3]
		board[3]=board[10]
		board[10]=board[17]
		board[17]=board[24]
		board[24]=board[31]
		board[31]=board[38]
		board[38]=board[45]
		board[45]=temp

	elif place==47:
		tile=board[5]
		board[5]=board[12]
		board[12]=board[19]
		board[19]=board[26]
		board[26]=board[34]
		board[33]=board[40]
		board[40]=board[47]
		board[47]=temp
	else:
		return 
	return board,tile

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