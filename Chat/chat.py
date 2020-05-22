from flask import Flask
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY']='secret'
socketio = SocketIO(app, cors_allowed_origins ='*')

@app.route('/')
def inicio():
    return 'la api funciona'

@socketio.on('message')
def recibir_mensaje(mensaje):
    print("El mensaje es: "+mensaje)
    send(mensaje,broadcast=True)

if __name__ =="__main__":
    socketio.run(app,debug=True)
 