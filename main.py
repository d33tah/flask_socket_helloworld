from flask import Flask, render_template
from flask_sockets import Sockets

import time

app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/hello')
def echo_socket(ws):
    for i in range(10):
        ws.send('no czesc' + str(i))
        time.sleep(1.0)


@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
