from flask_socketio import SocketIO, join_room, leave_room, emit, send
from flask_login import current_user
import _thread as t

class Handler():
    def __init__(self):
        # initialize socketio class
        self.socketio = SocketIO(ping_interval=10)

        # add lobby socketio event handlers
        self.socketio.on_event("connect", self.lobby_connected, namespace="/lobby")
        self.socketio.on_event("disconnected", self.lobby_disconnected, namespace="/lobby")
        self.socketio.on_event("add_room", self.add_room, namespace="/lobby")
        self.socketio.on_event("join", self.on_join, namespace="/lobby")

        # add game socketio event handlers
        self.socketio.on_event("connect", self.game_connected, namespace="/game")
        #self.socketio.on_event("disconnect", self.game_disconnected, namespace="/game")

        # initialize rooms array and dict
        self.room_names = []
        self.rooms = {}

        # initialize players dict
        self.players = {}

    def lobby_connected(self):
        print(current_user.username+" entered the lobby")
        self.players[current_user.username] = None
        self.socketio.emit("update_rooms", {"new_rooms": self.room_names}, broadcast=True, namespace="/lobby")

    def game_connected(self):
        username = current_user.username
        if username not in self.players:
            emit("lobby")
            return 0

        room = self.players[username]
        join_room(room)

        print(self.players)
        print(username+" entered game room "+room)


    def lobby_disconnected(self):
        print(current_user.username+" exited the lobby")

    def add_room(self, data):
        room_name = data["text"]
        if room_name not in self.room_names and room_name != "":
            self.room_names.append(room_name)

            self.socketio.emit("update_rooms", {"new_rooms": self.room_names}, broadcast=True, namespace="/lobby")

    def on_join(self, data):
        print(data)
        username = current_user.username
        room = data["room"]
        if room in self.room_names:
            self.players[username] = room