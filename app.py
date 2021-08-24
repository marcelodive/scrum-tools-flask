from flask import Flask, send_from_directory
from flask_socketio import SocketIO, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
socketio.run(app)

@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
  print(path)
  return send_from_directory('./', path)

@app.route('/')
def root():
  return send_from_directory('./en-US', 'index.html')

@app.route('/en-US/')
def root_en():
  return send_from_directory('./en-US', 'index.html')

@socketio.on('room updated')
def room_updated(room):
    print('room updated')
    socketio.emit('room updated', room, to = room['id'])

@socketio.on('new user enter poker room')
def new_user_poker(newUserInfo):
    print('new user enter poker room')
    socketio.emit('new user enter poker room', newUserInfo, to = newUserInfo['roomId'])

@socketio.on('new user enter ballot room')
def new_user_ballot(newUserInfo):
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
    