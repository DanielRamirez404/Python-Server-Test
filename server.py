import socket

def runServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(5)

    print(socket.gethostname())

    while True:
        clientsocket, adress = s.accept()
        print(f"{adress}, has connected")
        clientsocket.send(bytes("You\'ve been connected to 404\'s computer", "utf-8"))
