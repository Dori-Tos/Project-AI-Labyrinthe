import socket
import threading
import json
import Util_fonctions
port = 6942
#serverAddress = ('localhost', 3000)
#serverAddress = ('127.0.0.1', 3000)
serverAddress = ('0.0.0.0', 5050)
address=('localhost',port)
request = "subscribe"
name = "AI_of_the_dead"
matricules = ["22325","21006"]
state = {}

"""def inscription(address, request, port, name, matricules):
    with socket.socket() as s:
        s.connect(address)
        s.send(json.dumps({"request":"subscribe", "port": port, "name": name, "matricules": matricules}).encode())
        print({"request":"subscribe", "port": port, "name": name, "matricules": matricules})"""

"""def receiver(serverAddress, address):
    #while True: #pour les tests mock du socket et faire une fonction prossess / le while doit etre en dehors sinon cela envoie plusieurs fois la meme chose
        with socket.socket() as s:
            print("We are in receiver")
            s.bind(address)
            s.listen()
            client, address = s.accept() 
            received = json.loads(client.recv(10000).decode()) #str?
            print(received)
            process_receiver(received,address)
"""

def receiver(serverAddress, address):
    #while True: #pour les tests mock du socket et faire une fonction prossess / le while doit etre en dehors sinon cela envoie plusieurs fois la meme chose
        with socket.socket() as server_socket:
            server_socket.bind(serverAddress)
            server_socket.listen()
            client_socket, client_address = server_socket.accept() 
            received = json.loads(client_address.recv(10000).decode())
            
            client_socket.connect(address)
            client_socket.send(json.dumps({"request":"subscribe", "port": port, "name": name, "matricules": matricules}).encode())
            print({"request":"subscribe", "port": port, "name": name, "matricules": matricules})

            if received.get("response")=="ok":
                print("Successful inscription")
            elif received.get("response")=="error":
                print(received.get("error"))
            elif received.get("request")=="ping":
                with socket.socket() as s_2 :
                    s_2.connect(address)
                    s_2.send(json.dumps({"response": "pong"}).encode())
                    print({"response": "pong"})
            elif received.get("request")=="play":
                lives = received.get("lives")
                errors = received.get("errors")
                state = received.get("state")
                with socket.socket() as s_2 :
                    s_2.connect(address)
                    players = state.get("players")
                    current = state.get("current")
                    positions = state.get("positions")
                    target = state.get("target")
                    remaining = state.get("remaining")
                    tile = state.get("tile")
                    board = state.get("board")
                    move = Util_fonctions.apply(positions, target, board, remaining, current, tile, players)
                    s_2.send(json.dumps({"response": "move","move": move,"message": "Fun message"}))
                    print(move)
                    print("played succesfully")

receiver(serverAddress, address)

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
