import eventlet
eventlet.monkey_patch()
from app import app, handler

if __name__ == '__main__':
    handler.socketio.run(app, host="192.168.1.154", port=80, debug=True)
    #handler.socketio.run(app, port=80, debug=True)