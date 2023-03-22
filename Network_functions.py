import socket
import threading
import json

address = ('localhost', 3000)
request = "subscribe"
port = 6942
name = "AI_of_the_dead"
matricules = ["22325","21006"]

def inscription ():
    with socket.socket() as s:
        s.connect(address)
        s.send(json.dumps({"request": request, "port": port, "name": name, "matricules": matricules}).encode())
       
def receiver():
    while True:
        with socket.socket() as s:
            received = json.loads(s.recv(2048).decode()) #str?
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

thread = threading.Thread(target = receiver, daemon = True)

def ping_pong ():
    with socket.socket() as s:
        s.connect(address)
        s.send(json.dumps({"response": "pong"}).encode())

def giveup ():
    with socket.socket() as s:
        s.connect(address)
        s.send(json.dumps({"response": "giveup"}).encode())
