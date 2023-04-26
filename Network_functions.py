import socket
import threading
import json

port = 6942
serverAddress = ('localhost', 3000)
address = ('172.17.10.59', port)
request = "subscribe"
name = "AI_of_the_dead"
matricules = ["22325","21006"]
state = {}

def inscription(address, request, port, name, matricules):
    with socket.socket() as s:
        s.connect(address)
        s.send(json.dumps({"request": request, "port": port, "name": name, "matricules": matricules}).encode())
       
def receiver(serverAddress):
    while True: #mock du socket et faire une fonction prossess
        with socket.socket() as s:
            s.bind(serverAddress)
            s.listen()
            client, address = s.accept()
            received = json.loads(client.recv(2048).decode()) #str?
            if received.get("response")=="ok":
                print("Successful inscription")
            elif received.get("response")=="error":
                print(received.get("error"))
            elif received.get("request")=="ping":
                return ping_pong()
            elif received.get("request")=="play":
                lives = received.get("lives")
                errors = received.get("errors")
                state = received.get("state")

#thread = threading.Thread(target = receiver, daemon = True)

def ping_pong(address):
    with socket.socket() as s:
        s.connect(address)
        s.send(json.dumps({"response": "pong"}).encode())

def giveup(address):
    with socket.socket() as s:
        s.connect(address)
        s.send(json.dumps({"response": "giveup"}).encode())

def move(address, the_move_played):
    with socket.socket() as s:
        s.connect(address)
        s.send(json.dumps({"response": "move", "move": the_move_played, "message": "I'm comming !"}).encode())
