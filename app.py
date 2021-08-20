from flask import Flask
from flask_socketio import SocketIO
from flask import jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
socketio.run(app)

@socketio.on('room updated')
def message(room):
    socketio.emit('room updated', room)
    print(room)

@socketio.on('new user enter poker room')
def message(newUserInfo):
    socketio.emit('new user enter poker room', newUserInfo)
    print(newUserInfo)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route('/room', methods=['GET', 'POST'])
# def create_room():
#     return jsonify('ckaei93')

    # EC67pEiPD67RF4h