import Network_functions
import socket
import threading
import json

message = None
def server_receiver():
    s = socket.socket()
    serverAddress = ('0.0.0.0', 3000)
    s.bind(serverAddress)
    s.listen()
    client, address = s.accept()
    message = client.recv(2048).decode()
    print(message)

thread = threading.Thread(target = server_receiver, daemon = True)

def test_inscription():
    with socket.socket() as s:
        serverAddress = ('0.0.0.0', 3000)
        s.bind(serverAddress)
        s.listen()
        client, address = s.accept()
        message = client.recv(2048).decode()
        address = ('localhost', 3000)
        request = Network_functions.request
        port = Network_functions.port
        name = Network_functions.name
        matricules = Network_functions.matricules
        message_sent = json.dumps({"request": request, "port": port, "name": name, "matricules": matricules})
        assert message_sent == message 

def test_receiver():
    pass

def test_ping_pong ():
    pass

def testgiveup ():
    pass

def test_move():
    pass