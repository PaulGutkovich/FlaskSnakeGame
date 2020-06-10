from app import app, handler

if __name__ == '__main__':
    handler.socketio.run(app)