from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app)

connections = []

response = None

@app.route('/')
@app.route('/index')
def index():
    return '<h1> Socket Server Running </h1>'

@app.route('/api')
def api():
    activity = request.args.get('activity')
    if activity == 'add':
        add()
    return response

@socketio.on('response')
def respond(data):
    global response
    #print (response)
    response = data

@socketio.on('connect')
def connect():
    connections.append(request.sid)

def add():
    data = 'getdata'
    send(data,room = connections[0])


if __name__ == '__main__':
    socketio.run(app, host = '192.168.1.31',port = 80)