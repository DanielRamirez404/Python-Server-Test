from flask import Flask
from server import *

app = Flask(__name__)

@app.route('/')
def program():
    runServer() 

if __name__ == '__main__':
    app.run()
