from flask_socketio import SocketIO, join_room, leave_room, emit, send
from flask_login import current_user
from app.snake import *
from threading import Thread
import time

g = Game()

class Handler():
    def __init__(self):
        # initialize socketio class
        self.socketio = SocketIO(async_mode = "eventlet")

        # add lobby socketio event handlers
        self.socketio.on_event("connect", self.lobby_connected, namespace="/lobby")
        self.socketio.on_event("disconnect", self.lobby_disconnected, namespace="/lobby")
        self.socketio.on_event("add_room", self.add_room, namespace="/lobby")
        self.socketio.on_event("join", self.on_join, namespace="/lobby")

        # add game socketio event handlers
        self.socketio.on_event("connect", self.game_connected, namespace="/game")
        self.socketio.on_event("disconnect", self.game_disconnected, namespace="/game")
        self.socketio.on_event("entrance_check_response", self.check_player, namespace="/game")
        self.socketio.on_event("dir_change", self.change_dir, namespace="/game")

        # initialize rooms array and dict
        self.room_names = []
        self.rooms = {}

        # initialize players dict
        self.players = {}

        t1 = Thread(target=self.thread)
        t1.start()

    def lobby_connected(self):
        username = current_user.username
        self.socketio.emit("update_rooms", {"new_rooms": self.room_names}, namespace="/lobby")
        print(username + " entered the lobby", flush=True)

    def game_connected(self):
        username = current_user.username
        if username not in self.players:
            emit("kick")
            return 0

        room = self.players[username]
        join_room(room)
        if room not in self.rooms:
            self.rooms[room] = Game()

        game = self.rooms[room]

        if username not in game.snakes:
            self.rooms[room].new_snake(username)

        print(username + " entered game room " + room, flush=True)


    def lobby_disconnected(self):
        username = current_user.username
        print(username + " exited the lobby", flush=True)

    def game_disconnected(self):
        username = current_user.username
        if username in self.players:
            room = self.players[username]
            self.players.pop(username)
            self.rooms[room].snakes.pop(username)
            self.socketio.emit("entrance_check", room=room, namespace="/game")
            if len(self.rooms[room].snakes) == 0:
                self.room_names.remove(room)
                self.socketio.emit("update_rooms", {"new_rooms": self.room_names}, namespace="/lobby")

            print(username + " exited game room " + room, flush=True)

    def add_room(self, data):
        room_name = data["text"]
        username = current_user.username
        if room_name not in self.room_names and room_name != "":
            if username not in self.players:
                self.room_names.append(room_name)

                self.socketio.emit("update_rooms", {"new_rooms": self.room_names}, broadcast=True, namespace="/lobby")

    def on_join(self, data):
        username = current_user.username
        room = data["room"]
        if room in self.room_names:
            if username not in self.players:
                self.players[username] = room
                emit("game")
            else:
                current_room = self.players[username]
                if current_room == room:
                    emit("game")
                else:
                    send("You can not join this room because you are already in room "+current_room)

    def check_player(self):
        username = current_user.username
        if username not in self.players:
            emit("kick")

    def change_dir(self, data):
        username = current_user.username
        room = self.players[username]

        self.rooms[room].snakes[username].dir = data["dir"]

    def update(self):
        for room in self.rooms:
            self.rooms[room].update()
            game = self.rooms[room]

            data = []
            for username in game.snakes:
                snake = game.snakes[username]
                data.append(snake.blocks.tolist())

            self.socketio.emit("snakes", {"blocks": data}, namespace="/game")

    def thread(self):
        while True:
            self.update()
            time.sleep(0.1)