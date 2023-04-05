from Network_functions import state

remaining = state.get("remaining")
current = state.get("current")
players = state.get("players")
positions = state.get("positions")
board = state.get("board")

def lineValue(line, player):
	counters = {
		1: 0,
		2: 0,
		None: 0
	}

	for elem in line:
		counters[elem] += 1

	if counters[player] > counters[player%2+1]:
		return 1
	if counters[player] == counters[player%2+1]:
		return 0
	return -1

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
			return 2,5
		return -2,5
	res = 0
	for tile in board:
		res += lineValue([state[i] for i in tile], player)
	return res

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
	#C'ESt MAX go afficher
	directions = [1, -1, -7, 7]
	res = []
	for i in directions:
		dx = node+i
		if board[dx] in [' ', 'E']:
			res.append(dx)
	return res # Peut renvoyer jusqu'à 4 cases différentes

def the_move_played():
    pass