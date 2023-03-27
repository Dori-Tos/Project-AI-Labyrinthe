from Network_functions import state

remaining = state.get("remaining")
current = state.get("current")
players = state.get("players")
positions = state.get("positions")


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
			return 9
		return -9
	res = 0
	for line in lines:
		res += lineValue([state[i] for i in line], player)
	return res

def successors(node):
	laby = [
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
	]

	directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	res = []
	l, c = node # y puis x
	for dl, dc in directions:
		nl = l + dl
		nc = c + dc
		if laby[nl][nc] in [' ', 'E']:
			res.append((nl, nc))
	return res # Peut renvoyer jusqu'à 4 cases différentes


def the_move_played():
    pass