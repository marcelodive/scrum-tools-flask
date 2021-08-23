from flask import Flask
from flask_socketio import SocketIO, join_room, leave_room
from flask import jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
socketio.run(app)

@socketio.on('room updated')
def message(room):
    print('room updated')
    socketio.emit('room updated', room, to = room['id'])

@socketio.on('new user enter poker room')
def message(newUserInfo):
    print('new user enter poker room')
    socketio.emit('new user enter poker room', newUserInfo, to = newUserInfo['roomId'])

@socketio.on('new user enter ballot room')
def message(newUserInfo):
    print('new user enter ballot room')
    socketio.emit('new user enter ballot room', newUserInfo, to = newUserInfo['roomId'])

@socketio.on('join room')
def on_join(roomId):
    print('join room')
    join_room(roomId)

@socketio.on('left room')
def on_left(userInfo):
    print('user left')
    leave_room(userInfo['roomId'])
    socketio.emit('user left the room', userInfo['username'], to = userInfo['roomId'])
    