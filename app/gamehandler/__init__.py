from flask_socketio import SocketIO
from flask_login import current_user

class Handler():
    def __init__(self):
        # initialize socketio class
        self.socketio = SocketIO()

        # add socketio event handlers
        self.socketio.on_event("connect", self.connected, namespace="/game")
        self.socketio.on_event("add_room", self.add_room, namespace="/game")

        # initialize rooms
        self.rooms = []

    def connected(self):
        print(str(current_user)+" connected to socket")

    def add_room(self, data):
        room_name = data["text"]
        if room_name not in self.rooms:
            self.rooms.append(room_name)

        self.socketio.emit("update_rooms", {"new_rooms": room_name}, namespace="/game")