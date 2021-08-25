from flask import Flask, send_from_directory
from flask_socketio import SocketIO, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

if __name__ == '__main__':
  socketio.run(app)

@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
  return send_from_directory('./', path)

@app.route('/')
def root():
  return send_from_directory('./en-US', 'index.html')

@app.route('/en-US/')
def root_en():
  return send_from_directory('./en-US', 'index.html')

@socketio.on('room updated')
def room_updated(room):
    socketio.emit('room updated', room, to = room['id'])

@socketio.on('new user enter poker room')
def new_user_poker(newUserInfo):
    socketio.emit('new user enter poker room', newUserInfo, to = newUserInfo['roomId'])

@socketio.on('new user enter ballot room')
def new_user_ballot(newUserInfo):
    socketio.emit('new user enter ballot room', newUserInfo, to = newUserInfo['roomId'])

@socketio.on('join room')
def on_join(roomId):
    join_room(roomId)

@socketio.on('left room')
def on_left(userInfo):
    leave_room(userInfo['roomId'])
    socketio.emit('user left the room', userInfo['username'], to = userInfo['roomId'])
    