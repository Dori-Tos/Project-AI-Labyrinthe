import socket

def inscription ():
    address = ('adressofserver', 80)
    request = "subscribe".encode()
    port = 6942
    name = "AI_of_the_dead".encode()
    matricules =["22325","21006"]
    with socket.socket() as s:
        s.connect(address)
        s.send(request)
        s.send(port)
        s.send(name)
        s.send(matricules)
        if s.recv(2048).decode()=="ok":
            return "ok"
            s.send("pong")
        elif s.recv(2048).decode() =="error":
            return print(error)
        
    
#   "request": "subscribe",
#   "port": 8888,
#   "name": "fun_name_for_the_client",
#   "matricules": ["12345", "67890"]
    

