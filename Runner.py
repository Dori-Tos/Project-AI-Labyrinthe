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
from Network_functions import serverAddress
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
AI=input("Wich AI,random or max ?")
Network_functions.inscription(address, port, name, matricules)
Network_functions.receiver(serverAddress,address,AI)
