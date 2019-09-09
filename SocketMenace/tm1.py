import socketio
import pandas as pd

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')
    sio.emit('connect')

@sio.event
def message(data):
    df = pd.read_csv('https://perso.telecom-paristech.fr/eagan/class/igr204/data/cars.csv',sep=';')
    #print(df.head())
    sio.emit('response',data=df.to_json())

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://192.168.1.31:80')
sio.wait()