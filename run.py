from app import app, handler
import threading
import time

def thread():
    while True:
        print("Players: ", handler.players)
        print("Room names: ", handler.room_names)
        print("Rooms: ", handler.rooms)
        time.sleep(1.)

if __name__ == '__main__':
    threading.Thread(target=thread).start()
    handler.socketio.run(app, debug=True)