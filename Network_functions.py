import socket
import threading
import json
import Util_fonctions
port = 6942
serverAddress = ('localhost', port)
#address = ('172.17.10.59', 3000)
address=('localhost',3000)
request = "subscribe"
name = "AI_of_the_dead"
matricules = ["22325","21006"]
state = {}

def inscription(address, request, port, name, matricules):
    with socket.socket() as s:
        s.connect(address)
        s.send(json.dumps({"request":request, "port": port, "name": name, "matricules": matricules}).encode())
        print({"request":"subscribe", "port": port, "name": name, "matricules": matricules})
def receiver(serverAddress, address):
    #while True: #pour les tests mock du socket et faire une fonction prossess/ le while doit etre en dehors sinon cela envoie plusieurs fois la meme chose
    with socket.socket() as s:
        s.bind(serverAddress)
        s.listen()
        client, address = s.accept() 
        received = json.loads(client.recv(100000).decode())
        print(received)
        if received.get("response")=="ok":
            print("Successful inscription")
        elif received.get("response")=="error":
            print(received.get("error"))
        elif received.get("request")=="ping":
            return ping_pong(address)
        elif received.get("request")=="play":
            lives = received.get("lives")
            errors = received.get("errors")
            state = received.get("state")
            Util_fonctions.random_moves(state.get("board"),state.get("tile"),state.get("positions"))
def receiver2(serverAddress, address):
    #while True: #pour les tests mock du socket et faire une fonction prossess / le while doit etre en dehors sinon cela envoie plusieurs fois la meme chose
        with socket.socket() as s:
            s.bind(serverAddress)
            s.listen()
            client, notaddress = s.accept() 
            received = json.loads(client.recv(10000).decode()) #str?
            print(received)
            process_receiver(received)

def process_receiver(received,address):
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

def ping_pong(address):
    with socket.socket() as s:
        s.connect(address)
        s.send(json.dumps({"response": "pong"}).encode())
        print("pong")

def giveup(address):
    with socket.socket() as s:
        s.connect(address)
        s.send(json.dumps({"response": "giveup"}).encode())

def move(address, the_move_played):
    with socket.socket() as s:
        s.connect(address)
        s.send(json.dumps({"response": "move", "move": the_move_played, "message": "I'm comming !"}).encode())
