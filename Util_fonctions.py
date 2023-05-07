import time
from collections import defaultdict
from collections import deque
import random
import socket
import json
import threading

from tile_and_board import tile2
from tile_and_board import board2

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

def new_positions(place,positions):
	#Mets à jour les positions des joueurs en fonctions de la tile qui à été jouée
	#pre place l'endroit ou la tile a été insérée positions la positions des deux joueurs [14,9]
	#post l'emplacement des deux joueurs si ils on été déplacé

	position_joueur_1 = int(positions[0])
	position_joueur_2 = int(positions[1])

	if place=="A" and position_joueur_1==1 or position_joueur_1==8 or position_joueur_1==15 or position_joueur_1==22 or position_joueur_1==29 or position_joueur_1==36:
		position_joueur_1+=7
	elif place=="A" and position_joueur_1==43:
		position_joueur_1=1
	elif place=="A" and position_joueur_2==1 or position_joueur_2==8 or position_joueur_2==15 or position_joueur_2==22 or position_joueur_2==29 or position_joueur_2==36:
		position_joueur_2+=7
	elif place=="A" and position_joueur_2==43:
		position_joueur_2=1
	elif place=="B" and position_joueur_1==3 or position_joueur_1==10 or position_joueur_1==17 or position_joueur_1==24 or position_joueur_1==31 or position_joueur_1==38:
		position_joueur_1+=7
	elif place=="B" and position_joueur_1==45:
		position_joueur_1=3
	elif place=="B" and position_joueur_2==3 or position_joueur_2==10 or position_joueur_2==17 or position_joueur_2==24 or position_joueur_2==31 or position_joueur_2==38:
		position_joueur_2+=7
	elif place=="B" and position_joueur_2==45:
		position_joueur_2=3
	elif place=="C" and position_joueur_1==5 or position_joueur_1==12 or position_joueur_1==19 or position_joueur_1==26 or position_joueur_1==33 or position_joueur_1==40:
		position_joueur_1+=7
	elif place=="C" and position_joueur_1==47:
		position_joueur_1=5
	elif place=="C" and position_joueur_2==5 or position_joueur_2==12 or position_joueur_2==19 or position_joueur_2==26 or position_joueur_2==33 or position_joueur_2==40:
		position_joueur_2+=7
	elif place=="C" and position_joueur_2==47:
		position_joueur_2=5
	elif place=="D" and position_joueur_1==8 or position_joueur_1==9 or position_joueur_1==10 or position_joueur_1==11 or position_joueur_1==12 or position_joueur_1==13:
		position_joueur_1-=1
	elif place=="D" and position_joueur_1==7:
		position_joueur_1=13
	elif place=="D" and position_joueur_2==8 or position_joueur_2==9 or position_joueur_2==10 or position_joueur_2==11 or position_joueur_2==12 or position_joueur_2==13:
		position_joueur_2-=1
	elif place=="D" and position_joueur_2==7:
		position_joueur_2=13
	elif place=="E" and position_joueur_1==22 or position_joueur_1==23 or position_joueur_1==24 or position_joueur_1==25 or position_joueur_1==26 or position_joueur_1==27:
		position_joueur_1-=1
	elif place=="E" and position_joueur_1==21:
		position_joueur_1=27
	elif place=="E" and position_joueur_2==22 or position_joueur_2==23 or position_joueur_2==24 or position_joueur_2==25 or position_joueur_2==26 or position_joueur_2==27:
		position_joueur_2-=1
	elif place=="E" and position_joueur_2==21:
		position_joueur_2=27
	elif place=="F" and position_joueur_1==36 or position_joueur_1==37 or position_joueur_1==38 or position_joueur_1==39 or position_joueur_1==40 or position_joueur_1==41:
		position_joueur_1-=1
	elif place=="F" and position_joueur_1==35:
		position_joueur_1=41
	elif place=="F" and position_joueur_2==36 or position_joueur_2==37 or position_joueur_2==38 or position_joueur_2==39 or position_joueur_2==40 or position_joueur_2==41:
		position_joueur_2-=1
	elif place=="F" and position_joueur_2==35:
		position_joueur_2=41
	elif place=="G" and position_joueur_1==12 or position_joueur_1==19 or position_joueur_1==26 or position_joueur_1==33 or position_joueur_1==40 or position_joueur_1==47:
		position_joueur_1-=7
	elif place=="G" and position_joueur_1==5:
		position_joueur_1=47
	elif place=="G" and position_joueur_2==12 or position_joueur_2==19 or position_joueur_2==26 or position_joueur_2==33 or position_joueur_2==40 or position_joueur_2==47:
		position_joueur_2-=7
	elif place=="G" and position_joueur_2==5:
		position_joueur_2=47
	elif place=="H" and position_joueur_1==10 or position_joueur_1==17 or position_joueur_1==24 or position_joueur_1==31 or position_joueur_1==38 or position_joueur_2==45:
		position_joueur_1-=7
	elif place=="H" and position_joueur_1==3:
		position_joueur_1=45
	elif place=="H" and  position_joueur_2==10 or position_joueur_2==17 or position_joueur_2==24 or position_joueur_2==31 or position_joueur_2==38 or position_joueur_2==45:
		position_joueur_2-=7
	elif place=="H" and position_joueur_2==3:
		position_joueur_2=45
	elif place=="I" and position_joueur_1==8 or position_joueur_1==15 or position_joueur_1==22 or position_joueur_1==29 or position_joueur_1==36 or position_joueur_2==43:
		position_joueur_1-=7
	elif place=="I" and position_joueur_1==1:
		position_joueur_1=43
	elif place=="I" and position_joueur_2==8 or position_joueur_2==15 or position_joueur_2==22 or position_joueur_2==29 or position_joueur_2==36 or position_joueur_2==43:
		position_joueur_2-=7
	elif place=="I" and position_joueur_2==1:
		position_joueur_2=43
	elif place=="J" and position_joueur_1==35 or position_joueur_1==36 or position_joueur_1==37 or position_joueur_1==38 or position_joueur_1==39 or position_joueur_1==40:
		position_joueur_1+=1
	elif place=="J" and position_joueur_1==41:
		position_joueur_1=35
	elif place=="J" and position_joueur_1==35 or position_joueur_2==36 or position_joueur_2==37 or position_joueur_2==38 or position_joueur_2==39 or position_joueur_2==40:
		position_joueur_2+=1
	elif place=="J" and position_joueur_2==41:
		position_joueur_2=35
	elif place=="K" and position_joueur_1==21 or position_joueur_1==22 or position_joueur_1==23 or position_joueur_1==24 or position_joueur_1==25 or position_joueur_1==26:
		position_joueur_1+=1
	elif place=="K" and position_joueur_1==27:
		position_joueur_1=21
	elif place=="K" and position_joueur_2==21 or position_joueur_2==22 or position_joueur_2==23 or position_joueur_2==24 or position_joueur_2==25 or position_joueur_2==26:
		position_joueur_2+=1
	elif place=="K" and position_joueur_2==27:
		position_joueur_2=21
	elif place=="L" and position_joueur_1==7 or position_joueur_1==8 or position_joueur_1==9 or position_joueur_1==10 or position_joueur_1==11 or position_joueur_1==12:
		position_joueur_1+=1
	elif place=="L" and position_joueur_1==13:
		position_joueur_1=7
	elif place=="L" and position_joueur_1==7 or position_joueur_2==8 or position_joueur_2==9 or position_joueur_2==10 or position_joueur_2==11 or position_joueur_2==12:
		position_joueur_2+=1
	elif place=="L" and position_joueur_2==13:
		position_joueur_2=7
	positions=[position_joueur_1,position_joueur_2]
	return positions

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
	node = board.get(position)
	target_tile = target_finder(board, target)

	movements = successors(node, board)
	res = len(movements)
	return res
		
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

def tile_accessible(start, target, board):
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

	if q != 0:
		return target

def nearest_target(start, board):
	targets = []
	for i in range(len(board)):
		if board.get(i).get("item") != None:
			targets.append(i)

	accessible_targets = []
	for i in targets:
		accessible_targets.append(tile_accessible(start, i, board))
	
	q = deque()
	q.append(start)
	parents = {}
	parents[start] = None
	
	distances = []

	for target in accessible_targets:
		while q:
			node = q.popleft()
			if node == target_finder(board, target):
				break
			for successor in successors(node, board):
				if successor not in parents:
					parents[successor] = node
					q.append(successor)
			node = None
		distances.append(len(q))
	
	distances.sort()

	for i in range(len(distances)):
		list = [0]
		if distances[0] == distances[i]:
			list.append(i)
	n = random.choice(list)
	return distances[n]

def random_moves(board,tile,positions): 
	#fonction permmettant de jouer un coup aléatoire
	#pre le plateau (board), la tile libre (tile)
	#post le coup joué a envoyer au format du serveur
	place_possible=["A","B","C","D","E","F","G","H","I","J","K","L"]
	orientation_possible=[0,1,2,3]
	tile=tile_turner(tile,random.choice(orientation_possible))
	old_tile=dict(tile)
	gate=random.choice(place_possible)
	board,tile=new_board(board,tile,gate)
	directions_possible=movement_possible(positions[0],board)
	if directions_possible!=[]:
		direction=random.choice(directions_possible)
		if direction=="N":
			new_positions= positions[0]-7
		elif direction=="E":
			new_positions= positions[0]+1
		elif direction=="S":
			new_positions= positions[0]+7
		elif direction=="W":
			new_positions= positions[0]-1
		else:
			print("error")
	else:
		new_positions=positions[0]
	message_to_send={"tile": old_tile, "gate": gate, "new_position": new_positions}
	return message_to_send

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

old_remaining = list(remaining)

def heuristic(remaining, old_remaining, players, current): # permet de dire à l'ia si le jeu s'arrête
	theWinner = winner(remaining, current)
	other_nbr = (current-1)
	if old_remaining == remaining:
		return 0
	if theWinner == players[current]:
		return 9
	elif old_remaining[current] != remaining[current]:
		return 5
	elif old_remaining[other_nbr] != remaining[other_nbr]:
		return -5
	return -9

def moves_MAX(start, board, target, tile):
	rotations = [0, 1, 2, 3]
	rotation = random.choice(rotations)
	new_tile = tile_turner(tile, rotation)
	places = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
	place = random.choice(places)
	board, tile = new_board(board, new_tile, place)

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
	positions[current] = node

	return [node, tile, place]
	
def moves_MIN(start, board, tile):
	rotations = [0, 1, 2, 3]
	rotation = random.choice(rotations)
	new_tile = tile_turner(tile, rotation)
	places = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
	place = random.choice(places)
	board, tile = new_board(board, new_tile, place)
	
	q = deque()
	q.append(start)
	parents = {}
	parents[start] = None
		
	while q:
		node = q.popleft()
		if node == nearest_target(node, board):
			break
		for successor in successors(node, board):
			if successor not in parents:
				parents[successor] = node
				q.append(successor)
	positions[current] = node

	return [node, tile, place]

@timeit
def MAX(positions, target, board, remaining, current, tile, players, depth, theValue, theMove):
	start = int(positions[current])

	value = heuristic(remaining, old_remaining, players, current)
	
	for move in moves_MAX(start, board, target, tile):
		value, _ = MIN(positions, target, board, remaining, (current-1), tile, players, depth, theValue, theMove)
		if value > theValue:
			theValue, theMove = value, move
		return theValue, theMove

def MIN(positions, target, board, remaining, current, tile, players, depth, theValue, theMove):
	start = int(positions[current])

	value = heuristic(remaining, old_remaining, players, current)

	if depth == 0:
		return theValue, theMove

	for move in moves_MIN(start, board, tile):
		value, _ = MAX(positions, target, board, remaining, (current-1), tile, players, depth-1, theValue, theMove)
		if value < theValue:
			theValue, theMove = value, move
	return theValue, theMove

#print(MAX(positions, target, board2, remaining, current, tile2, players, 3, float('-inf'), None))

def the_move_played(address, request, port, name, matricules, board, tile, positions, current, players, remaining):
	with socket.socket() as s:
		s.connect(address)
		s.send(json.dumps({
			"response": "move",
			"move": random_moves(board,tile,positions),
			"message": "Are ya winning son ?"
			}).encode())
