import eventlet
eventlet.monkey_patch()
from app import app, handler

if __name__ == '__main__':
    handler.socketio.run(app, port=80, debug=True)