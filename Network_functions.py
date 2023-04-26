import socket
import threading
import json

port = 6942
serverAddress = ('', port)
address = ('172.17.10.59', 3000)
request = "subscribe"
name = "AI_of_the_dead"
matricules = ["22325","21006"]
state = {}

def inscription(address, request, port, name, matricules):
    with socket.socket() as s:
        s.connect(address)
        s.send(json.dumps({"request": request, "port": port, "name": name, "matricules": matricules}).encode())
       
def receiver(serverAddress, address):
    while True: #pour les tests mock du socket et faire une fonction prossess
        with socket.socket() as s:
            s.bind(serverAddress)
            s.listen()
            client, notaddress = s.accept() 
            received = json.loads(client.recv(2048).decode()) #str?
            print(received)
            if received.get("response")=="ok":
                print("Successful inscription")
            elif received.get("response")=="error":
                print(received.get("error"))
            elif received.get("request")=="ping":
                print("we are in ping")
                return ping_pong(address)
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
