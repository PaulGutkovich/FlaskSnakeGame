from flask_socketio import SocketIO, join_room, leave_room, emit, send
from flask_login import current_user

class Handler():
    def __init__(self):
        # initialize socketio class
        self.socketio = SocketIO()

        # add socketio event handlers
        self.socketio.on_event("connect", self.connected, namespace="/lobby")
        self.socketio.on_event("add_room", self.add_room, namespace="/lobby")
        self.socketio.on_event("join", self.on_join, namespace="/lobby")

        # initialize rooms array
        self.rooms = []

        # initialize players dict

    def connected(self):
        print(str(current_user)+" connected to socket")

    def add_room(self, data):
        room_name = data["text"]
        if room_name not in self.rooms and room_name != "":
            self.rooms.append(room_name)

            self.socketio.emit("update_rooms", {"new_rooms": self.rooms}, broadcast=True, namespace="/lobby")

    def on_join(self, data):
        room = data["room"]
        if room in self.rooms:
            join_room(room)
            send("You joined the room "+room)