import socket
import threading
import json
import Util_fonctions
import random
port = 6942
#port = int(input("port:"))
#serverAddress = ('localhost', 3000)
#serverAddress = ('127.0.0.1', 3000)
serverAddress = ('localhost', port)
address=('localhost', 3000)
request = "subscribe"
#name=input("name:")
name = "AI_of_the_dead"
#matricules = input("matricule :")
matricules = ["22325","21006"]
state = {}

def inscription(address, port, name, matricules):   
    with socket.socket() as s:
        s.connect(address)
        s.send(json.dumps({"request": "subscribe", "port": port, "name": name, "matricules": matricules}).encode())
        print({"request":"subscribe", "port": port, "name": name, "matricules": matricules})


def receiver(serverAddress, address,AI):
    while True: #pour les tests mock du socket et faire une fonction prossess / le while doit etre en dehors sinon cela envoie plusieurs fois la meme chose
            server_socket = socket.socket()
            server_socket.bind(serverAddress)
            server_socket.listen()
            client_socket, client_address = server_socket.accept()
            received = json.loads(client_socket.recv(10000).decode())
            print("What we received")
            print("---------------------------------------------------------------------------------------------")
            print(received)
            print("---------------------------------------------------------------------------------------------")
            if received.get("response")=="ok":
                print("Successful inscription")
            elif received.get("response")=="error":
                print(received.get("error"))
            elif received.get("request")=="ping":
                client_socket.send(json.dumps({"response": "pong"}).encode())
                print({"response": "pong"})
            elif received.get("request")=="play":
                lives = received.get("lives")
                errors = received.get("errors")
                state = received.get("state")

                players = state.get("players")
                current = state.get("current")
                positions = state.get("positions")
                target = state.get("target")
                remaining = state.get("remaining")
                tile = state.get("tile")
                board = state.get("board")
                fun_messages=["J'arrive !","I'm comming for you","You can't hide","I wan't all treasures"]
                move = Util_fonctions.apply(positions, target, board, remaining, current, tile, players,AI)
                client_socket.send(json.dumps({"response": "move","move": move,"message": random.choices(fun_messages)}).encode())
                print("---------------------------------------------------------------------------------------------")
                print(move)


def process_receiver(received,address):
    print("We are in proccess receiver")
    if received.get("response")=="ok":
        print("Successful inscription")
    elif received.get("response")=="error":
        print(received.get("error"))
    elif received.get("request")=="ping":
        ping_pong(address)
    elif received.get("request")=="play":
        lives = received.get("lives")
        errors = received.get("errors")
        state = received.get("state")
        random_move(address)
            
def random_move(address):
    with socket.socket() as s:
            s.connect(address)
            move=Util_fonctions.random_moves(state.get("board"),state.get("tile"),state.get("positions"))
            s.send(json.dumps({"response": "move","move": move,"message": "Fun message"}))
            print("played")

def ping_pong(address):
    with socket.socket() as s:
        s.connect(('localhost',3000))
        s.send(json.dumps({"response": "pong"}).encode())
        print({"response": "pong"})

def giveup(address):
    with socket.socket() as s:
        s.connect(address)
        s.send(json.dumps({"response": "giveup"}).encode())

def move(address, the_move_played):
    with socket.socket() as s:
        s.connect(address)
        s.send(json.dumps({"response": "move", "move": the_move_played, "message": "I'm comming !"}).encode())
