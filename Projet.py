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

players = ["LUR","HSL"]
current = "LUR"
remaining = [4, 4]
positions = [0, 48]

target = 3

tile={
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
		"item" : None
	},
	1:{
		"N" : False,
		"E" : True,
		"S" : False,
		"W" : True,
		"item" : None
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
		"item" : None
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
		"item" : None
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
		"item" : None
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
		"item" : None
	},
	11:{
		"N" : True,
		"E" : True,
		"S" : False,
		"W" : False,
		"item" : None
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
		"item" : None
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
		"item" : None
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
		"item" : None
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
		"item" : None

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
		"item" : None
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
		"item" : None
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
		"item" : None
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
		"item" : None
	},
	36:{
		"N" : True,
		"E" : False,
		"S" : True,
		"W" : False,
		"item" : None
	},
	37:{
		"N" : False,
		"E" : True,
		"S" : True,
		"W" : False,
		"item" : None
	},
	38:{
		"N" : True,
		"E" : False,
		"S" : False,
		"W" : True,
		"item" : None
	},
	39:{
		"N" : True,
		"E" : False,
		"S" : True,
		"W" : False,
		"item" : None
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
		"item" : None
	},
	42:{
		"N" : True,
		"E" : True,
		"S" : False,
		"W" : False,
		"item" : None
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
		"item" : None
	},
	46:{
		"N" : True,
		"E" : True,
		"S" : False,
		"W" : True,
		"item" : None
	},
	47:{
		"N" : True,
		"E" : False,
		"S" : False,
		"W" : True,
		"item" : None
	},
	48:{
		"N" : True,
		"E" : False,
		"S" : False,
		"W" : True,
		"item" : None
	},
}
def new_board(board,tile,place):
	#crée les board avec les pièces qui ont bougé par rapport à un board (board) et l'emplacement souhaité (place)
	#pre le board et la tile en plus (tile)
	#post le board après mouvement et la nouvelle tile libre
	temp=tile
	if place==1:
		tile=board[43]
		board.update({43:board.get(36),36:board.get(29),29:board.get(22),22:board.get(15),15:board.get(8),8:board.get(1),1:temp})
	
	elif place==3:
		tile=board[45]
		board.update({45:board.get(38),38:board.get(31),29:board.get(24),24:board.get(17),17:board.get(10),10:board.get(3),3:temp})
	
	elif place==5:
		tile=board[47]
		board.update({47:board.get(40),40:board.get(33),33:board.get(26),26:board.get(19),19:board.get(12),12:board.get(5),5:temp})
	
	elif place==7:
		tile=board[13]
		board.update({13:board.get(12),12:board.get(11),11:board.get(10),10:board.get(9),9:board.get(8),8:board.get(7),7:temp})

	elif place==21:
		tile=board[27]
		board.update({27:board.get(26),26:board.get(25),25:board.get(24),24:board.get(23),23:board.get(22),22:board.get(21),21:temp})
	
	elif place==35:
		tile=board[41]
		board.update({41:board.get(40),40:board.get(39),39:board.get(38),38:board.get(37),37:board.get(36),36:board.get(35),35:temp})

	elif place==13:
		tile=board[7]
		board.update({7:board.get(8),8:board.get(9),9:board.get(10),10:board.get(11),11:board.get(12),12:board.get(13),13:temp})

	elif place==27:
		tile=board[21]
		board.update({21:board.get(22),22:board.get(23),23:board.get(24),24:board.get(25),25:board.get(26),26:board.get(27),27:temp})

	elif place==41:
		tile=board[35]
		board.update({35:board.get(36),36:board.get(37),37:board.get(38),38:board.get(39),39:board.get(40),40:board.get(41),41:temp})
	
	elif place==43:
		tile=board[1]
		board.update({1:board.get(8),8:board.get(15),15:board.get(22),22:board.get(29),29:board.get(36),36:board.get(43),43:temp})

	elif place==45:
		tile=board[3]
		board.update({3:board.get(10),10:board.get(17),17:board.get(24),24:board.get(31),31:board.get(38),38:board.get(45),45:temp})

	elif place==47:
		tile=board[5]
		board.update({5:board.get(12),12:board.get(19),19:board.get(26),26:board.get(33),33:board.get(40),40:board.get(47),47:temp})
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

current_nbr = players.index(current)
other_nbr = current_nbr -1

start_position_current = positions[current_nbr]
iteration = 0

@timeit
def BFS(start, target, board, tile, place, iteration):
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

	path = []
	actions = []

	while node is not None:
		path.append(node)
		node = parents[node]
		if place is not None:
			actions.append(place)

	if actions == [] and path == [] and iteration == 0:
		iteration += 1
		places = [1, 3, 5, 7, 13, 21, 27, 35, 41, 43, 45, 47]
		place = random.choice(places)
		board, tile = new_board(board, tile, place)
		return BFS(start_position_current, target, board, tile, place, iteration)
	
	actions.pop(-1)
	return (list(reversed(path)), list(reversed(actions)))

print(BFS(0, target, board, tile, None, iteration))
iteration = 0

def winner(remaining, current, players):
	current_nbr = players.index(current)
	other_nbr = current_nbr -1
	if remaining[current_nbr] == 0:
		return current
	elif remaining[other_nbr] == 0:
		return players[other_nbr]
	else:
	    return None
	
def gameOver(remaining, current, players):
	if winner(remaining, current, players) is not None:
		return True

def heuristic(remaining, player): # permet de dire à l'ia si le jeu s'arrête
	if gameOver(remaining):
		theWinner = winner(remaining)
		if theWinner is None:
			return 0
		if theWinner == player:
			return 1
		return -1

def moves(board, treasure_remaining): # nécessairee si on veut un peu de random
	res = []						  # + à changer si on veut que ça marche
	for i, elem in enumerate(board):
		if elem is None:
			res.append(i)
	
	random.shuffle(res)
	return res

def negamaxWithPruning(positions, target, board, remaining, player, players, tile, alpha=float('-inf'), beta=float('inf')):
	current_nbr = players.index(current)
	other_nbr = current_nbr -1
	start = positions[current_nbr]
	if gameOver(remaining):
		return -heuristic(remaining, player), None

	theValue, theMove = float('-inf'), None
	"for node in moves(board, remaining[current_nbr]):"
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
		final_pos = q.popleft()
		
		value, _ = negamaxWithPruning(positions, target, board, remaining, player%2+1, players, tile, -beta, -alpha)
		if value > theValue:
			theValue, theMove = value, node
		alpha = max(alpha, theValue)
		if alpha >= beta:
			break
	return -theValue, theMove

print(negamaxWithPruning(positions, target, board, remaining, current, players, tile))

def the_move_played():
    pass