import Util_fonctions
from tile_and_board import board2 as board2
from tile_and_board import tile2 as tile2
import json

def test_new_board():
    tile = {"N" : True,"E" : True, "S" : False, "W" : True, "item" : 24}
    tile2 = {"N" : False, "E" : True, "S" : False, "W" : True, "item" : None}
    new_board, tile_test = Util_fonctions.new_board(board2, tile, "I")
    assert tile2 == tile_test

def test_new_position():
    positions_1 = [1, 9]
    positions_0 = [8, 9]
    assert positions_1 == Util_fonctions.new_positions("I", positions_0)

def test_target_finder():
    target = 3
    assert 14 == Util_fonctions.target_finder(board2, target)

def test_movement_possible():
    res = ["E"]
    assert res == Util_fonctions.movement_possible(0, board2)

def test_successors():
    res = [1]
    assert res == Util_fonctions.successors(0, board2)

def test_tile_turner():
    res = tile2={"N" : True, "E" : True, "S" : True, "W" : False, "item" : 24}
    assert res == Util_fonctions.tile_turner(tile2, 1)

def test_nearest_target():
    assert Util_fonctions.nearest_target(48, board2) == 10 or 12

def test_random_moves():
    assert type(Util_fonctions.random_moves(board2, tile2, [0, 48])) == dict

def test_winner():
    remaining = [0,2]
    current = 0
    assert current == Util_fonctions.winner(remaining, current)

def test_gameOver():
    remaining = [0,2]
    current = 0
    True == Util_fonctions.gameOver(remaining, current)

def test_heuristic():
    remaining = [1,2]
    new_remaining = [1,1]
    current = 0
    players = ['me', 'you']
    assert -5 == Util_fonctions.heuristic(remaining, new_remaining, players, current)