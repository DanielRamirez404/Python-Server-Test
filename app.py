from flask import Flask
from server import *
import socket

app = Flask(__name__)

@app.route('/')
def program():
    return socket.gethostname()
    //runServer() 

if __name__ == '__main__':
    app.run()
