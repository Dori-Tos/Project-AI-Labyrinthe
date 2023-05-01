import time
from collections import defaultdict
from collections import deque
import random
import Network_functions
import socket
import json
import threading

from Network_functions import state
from Network_functions import name
from Network_functions import address
from Network_functions import request
from Network_functions import port
from Network_functions import matricules

from tile_and_board import tile2
from tile_and_board import board2

remaining = state.get("remaining")
current = state.get("current")
players = state.get("players")
positions = state.get("positions")
board = state.get("board")
tile = state.get("tile")

Network_functions.inscription(address, request, port, name, matricules)
thread = threading.Thread(target = Network_functions.receiver , args=(Network_functions.address, Network_functions.serverAddress), daemon = True)
thread.start()
#il faut threader receiver et pas the_move_played
print("thread started")