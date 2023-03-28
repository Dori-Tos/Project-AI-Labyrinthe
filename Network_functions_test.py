import Network_functions
import socket
import threading
import json

message = None

def test_inscription():
    with socket.socket() as s:
        serverAddress = ('0.0.0.0', 3000)
        s.bind(serverAddress)
        s.listen()
        address = ('localhost', 3000)
        thread = threading.Thread(target = Network_functions.inscription, daemon = True, args=(address,))
        thread.start()
        client, address = s.accept()
        message = client.recv(2048).decode()
        request = Network_functions.request
        port = Network_functions.port
        name = Network_functions.name
        matricules = Network_functions.matricules
        message_sent = json.dumps({"request": request, "port": port, "name": name, "matricules": matricules})
        assert message_sent == message

def test_receiver():
    with socket.socket() as s:
        address = ('localhost', 3000)
        thread = threading.Thread(target = Network_functions.receiver, daemon = True)
        s.connect(address)
        s.send(json.dumps({"players": ["LUR", "HSL"],"current": 0,"positions": [6, 47],"target": 3,
                            "remaining": 4,"tile":None,"board":None}).encode())  
        message_sent = json.dumps({"players": ["LUR", "HSL"],"current": 0,"positions": [6, 47],"target": 3,
                            "remaining": 4,"tile":None,"board":None})
        
        assert message_sent == received

def test_ping_pong ():
    with socket.socket() as s:
        serverAddress = ('0.0.0.0', 3000)
        s.bind(serverAddress)
        s.listen()
        address = ('localhost', 3000)
        thread = threading.Thread(target = Network_functions.ping_pong, daemon = True, args=(address,))
        thread.start()
        client, address = s.accept()
        message = client.recv(2048).decode()
        message_sent = json.dumps({"response": "pong"})
        assert message_sent == message

def test_giveup ():
    with socket.socket() as s:
        serverAddress = ('0.0.0.0', 3000)
        s.bind(serverAddress)
        s.listen()
        address = ('localhost', 3000)
        thread = threading.Thread(target = Network_functions.giveup, daemon = True, args=(address,))
        thread.start()
        client, address = s.accept()
        message = client.recv(2048).decode()
        message_sent = json.dumps({"response": "giveup"})
        assert message_sent == message

def test_move():
    with socket.socket() as s:
        serverAddress = ('0.0.0.0', 3000)
        s.bind(serverAddress)
        s.listen()
        address = ('localhost', 3000)
        the_move_played = None
        thread = threading.Thread(target = Network_functions.move, daemon = True, args=(address, the_move_played))
        thread.start()
        client, address = s.accept()
        message = client.recv(2048).decode()
        message_sent = json.dumps({"response": "move", "move": the_move_played, "message": "I'm comming !"})
        assert message_sent == message