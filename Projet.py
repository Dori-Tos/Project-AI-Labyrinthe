import time
from collections import defaultdict
import random

import Network_functions
import socket
import json
import threading

from Network_functions import state
from Network_functions import name
from tile_and_board import tile
from tile_and_board import board

remaining = state.get("remaining")
current = state.get("current")
players = state.get("players")
positions = state.get("positions")
board = state.get("board")

players = ["LUR","HSL"]
current = 0
remaining = [4, 4]
positions = [0, 48]

target = 3

def new_board(board,tile,place):
	#crée les board avec les pièces qui ont bougé par rapport à un board (board) et l'emplacement souhaité (place)
	#pre le board et la tile en plus (tile)
	#post le board après mouvement et la nouvelle tile libre
	temp=tile
	if place == "A":
		tile=board[43]
		board.update({43:board.get(36),36:board.get(29),29:board.get(22),22:board.get(15),15:board.get(8),8:board.get(1),1:temp})
	
	elif place == "B":
		tile=board[45]
		board.update({45:board.get(38),38:board.get(31),29:board.get(24),24:board.get(17),17:board.get(10),10:board.get(3),3:temp})
	
	elif place == "C":
		tile=board[47]
		board.update({47:board.get(40),40:board.get(33),33:board.get(26),26:board.get(19),19:board.get(12),12:board.get(5),5:temp})
	
	elif place == "L":
		tile=board[13]
		board.update({13:board.get(12),12:board.get(11),11:board.get(10),10:board.get(9),9:board.get(8),8:board.get(7),7:temp})

	elif place == "K":
		tile=board[27]
		board.update({27:board.get(26),26:board.get(25),25:board.get(24),24:board.get(23),23:board.get(22),22:board.get(21),21:temp})
	
	elif place == "J":
		tile=board[41]
		board.update({41:board.get(40),40:board.get(39),39:board.get(38),38:board.get(37),37:board.get(36),36:board.get(35),35:temp})

	elif place == "D":
		tile=board[7]
		board.update({7:board.get(8),8:board.get(9),9:board.get(10),10:board.get(11),11:board.get(12),12:board.get(13),13:temp})

	elif place == "E":
		tile=board[21]
		board.update({21:board.get(22),22:board.get(23),23:board.get(24),24:board.get(25),25:board.get(26),26:board.get(27),27:temp})

	elif place == "F":
		tile=board[35]
		board.update({35:board.get(36),36:board.get(37),37:board.get(38),38:board.get(39),39:board.get(40),40:board.get(41),41:temp})
	
	elif place == "I":
		tile=board[1]
		board.update({1:board.get(8),8:board.get(15),15:board.get(22),22:board.get(29),29:board.get(36),36:board.get(43),43:temp})

	elif place == "H":
		tile=board[3]
		board.update({3:board.get(10),10:board.get(17),17:board.get(24),24:board.get(31),31:board.get(38),38:board.get(45),45:temp})

	elif place == "G":
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

def tile_turner(tile, rotation): # tourne de 90° degrés vers la droite autant de fois que le nbr rotation le demande
	if rotation == 0:
		return tile
	else:
		n = 0
		while n < rotation:
			temp = dict(tile)
			tile.update({"E": temp.get("N")})
			tile.update({"S": temp.get("E")})
			tile.update({"W": temp.get("S")})
			tile.update({"N": temp.get("W")})
			n += 1
	return tile

from collections import deque

def timeit(fun):
	def wrapper(*args, **kwargs):
		start = time.time()
		res = fun(*args, **kwargs)
		print('Execute in {}s'.format(time.time() - start))
		return res
	return wrapper

other_nbr = current -1

start_position_current = positions[current]
iteration = 0

#@timeit
def BFS(start, target, board, tile, place):
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

	if actions == [] and path == []:
		places = [1, 3, 5, 7, 13, 21, 27, 35, 41, 43, 45, 47]
		place = random.choice(places)
		board, tile = new_board(board, tile, place)
		return BFS(start_position_current, target, board, tile, place, iteration)
	
	actions.pop(-1)
	return ("bonjour")

#print(BFS(0, target, board, tile, None, iteration))
iteration = 0

def winner(remaining, current):
	other_nbr = (current+1)%2
	if remaining[current] == 0:
		return current
	elif remaining[other_nbr] == 0:
		return other_nbr
	else:
	    return None
	
def gameOver(remaining, current):
	if winner(remaining, current) is not None:
		return True
	else:
		return None

def heuristic(remaining, new_remaining, players, current): # permet de dire à l'ia si le jeu s'arrête
	if gameOver(remaining, current):
		theWinner = winner(remaining, current)
		other_nbr = (current+1)%2
		if new_remaining == remaining:
			return 0
		if theWinner == players[current]:
			return 9
		elif new_remaining[current] != remaining[current]:
			return 5
		elif new_remaining[other_nbr] != remaining[other_nbr]:
			return -5
		return -9

def moves(board, treasure_remaining): # nécessairee si on veut un peu de random
	res = []						  # + à changer si on veut que ça marche
	for i, elem in enumerate(board):
		if elem is None:
			res.append(i)
	
	random.shuffle(res)
	return res

def negamaxWithPruning(positions, targets, board, remaining, current, players, tile, alpha=float('-inf'), beta=float('inf')):
	print(positions)
	print(current)
	print(tile)
	print(alpha)
	print(beta)
	target = targets[current]
	other_nbr = (current+1)%2
	start = positions[current]
	if gameOver(remaining, current,) == True:
		return -heuristic(remaining, current), None

	theValue, theMove = float('-inf'), None
	#for node in moves(board, remaining[current_nbr]):
	while True:
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
		
		action = None

		if q == []:
			rotations = [0, 1, 2, 3]
			rotation = random.choice(rotations)
			tile = tile_turner(tile, rotation)
			places = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
			place = random.choice(places)
			action = place
			board, tile = new_board(board, tile, place)

		value, _ = negamaxWithPruning(positions, targets, board, remaining, (current+1)%2, players, tile, -beta, -alpha)
		if value > theValue:
			theValue, theMove = value, node
		alpha = max(alpha, theValue)
		if alpha >= beta:
			break
	last_pos = q.popleft()
	return last_pos, tile, action

def MAX(positions, target, board, remaining, current, tile, depth = 3):
	other_nbr = (current+1)%2
	start = positions[current]
	new_remaining = int(remaining)
	
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

	action = None

	rotations = [0, 1, 2, 3]
	rotation = random.choice(rotations)
	tile = tile_turner(tile, rotation)
	places = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
	place = random.choice(places)
	action = int(place)
	board, tile = new_board(board, tile, place)
	
	if heuristic(remaining, new_remaining, players, current) >= 0:
		return action, positions[current], tile

thread = threading.Thread(target = Network_functions.receiver(Network_functions.serverAddress), daemon = True)
thread.start()
											
def the_move_played(address, request, port, name, matricules):
	Network_functions.inscription(address, request, port, name, matricules)
	print("subs")
	with socket.socket() as s:
		s.connect(address)
		s.send(json.dumps({
			"response": "move",
			"move": "bonjour",
			"message": "Are ya winning son ?"
			}).encode())

thread = threading.Thread(target = the_move_played , args=(Network_functions.address, Network_functions.request, Network_functions.port, Network_functions.name, Network_functions.matricules), daemon = True)
thread.start()
print("thread started")
Network_functions.receiver(Network_functions.serverAddress, Network_functions.address)

while True:
	print("")