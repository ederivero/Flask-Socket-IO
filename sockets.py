# pip install flask flask-socketio
from flask import Flask, request
from flask_socketio import SocketIO, emit, send
from engineio.payload import Payload
Payload.max_decode_packets = 500 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins =['http://127.0.0.1:5500','*'])
users=[]
colors=['#fcba03','#2ef290','#0c4fed','#ed15b4','#ed15b4']
@socketio.on('connect')
def conexion():
    users.append(request.args['t'])
    print("client connect: "+request.args['t'])

@socketio.on('disconnect')
def desconexion():
    print("client disconnect: "+request.args['t'])
    users.remove(request.args['t'])

@socketio.on('mouse')
def mouse_msg(message):
    print(request.args['t']) 
    color=''
    for index in range(0,len(users)):
        if users[index] == request.args['t']:
            print(index)
            color=colors[index]
            message['color']=color
    print(message)
    emit('mouse',message, broadcast=True, include_self=False)
if __name__ == '__main__':
    socketio.run(app,log_output=False,debug=True)