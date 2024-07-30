from flask import Flask, render_template
import threading
import time
from websocket import create_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def send_message():
    ws = create_connection("ws://localhost:7100/ws")
    while True:
        time.sleep(10)
        ws.send({'status': 0, 'msj': 'Hola mundo socketio'})

if __name__ == '__main__':
    threading.Thread(target=send_message).start()
    app.run(debug=True)