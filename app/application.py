from os import getenv

from flask import Flask, render_template
from flask_socketio import SocketIO
from app.config import BROKER_URL

from app.handlers.morse import translate

app = Flask(__name__)
socket = SocketIO(app, message_queue=BROKER_URL[getenv("ENV")])

socket.on_event('translate', translate)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
