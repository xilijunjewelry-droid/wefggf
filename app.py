from flask import Flask, request, jsonify, session
from flask_socketio import SocketIO

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong secret key

socketio = SocketIO(app)

# Session management
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    session['username'] = username
    return jsonify({'message': 'Logged in successfully'})

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return jsonify({'message': 'Logged out successfully'})

# Chat API routes
@app.route('/message', methods=['POST'])
def send_message():
    message = request.json.get('message')
    socketio.emit('new_message', {'message': message})
    return jsonify({'message': 'Message sent'})

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)
