import numpy as np
import random

rows = 23
cols = 32

def random_block():
    x = random.randint(0, cols-1)
    y = random.randint(0, rows-1)

    return np.array([x, y])

def random_dir():
    dir = np.array([0, 0])
    i = random.randint(0, 1)
    sign = random.randint(0, 1)*2-1
    dir[i] = sign
    return dir

class Game:
    def __init__(self):
        self.snakes = {}
        self.dead = []
        self.board = np.zeros((cols, rows))
        self.food = self.empty_block()
    
    def empty_block(self):
        while True:
            block = random_block()
            if self.board[block[0]][block[1]] == 0:
                return block

    def fill_board(self):
        self.board = np.zeros((cols, rows))
        for username in self.snakes:
            snake = self.snakes[username]
            for block in snake.blocks:
                self.board[block[0]][block[1]] = 1

    def new_snake(self, username):
        head = self.empty_block()
        snake = Snake(head[0], head[1])
        self.snakes[username] = snake
        self.board[head[0]][head[1]] = 1

    def remove_snake(self, username):
        self.snakes.pop(username)

    def check_ate(self, snake):
        if snake.head[0] == self.food[0]:
            if snake.head[1] == self.food[1]:
                return True

    def auto_collide(self, snake):
        head = snake.head
        l = snake.blocks.shape[0]
        if l < 3:
            return False

        else:
            i = 1
            while True:
                if i == l:
                    return False

                block = snake.blocks[i]
                if block[0] == head[0]:
                    if block[1] == head[1]:
                        return True

                i += 1

    def check_dead(self, snake):
        if self.auto_collide(snake):
            return True
        if self.collide(snake):
            return True
        if snake.check_border():
            return True

        return False

    def collide(self, snake):
        head = snake.head
        for user2 in self.snakes:
            snake2 = self.snakes[user2]
            if snake == snake2:
                continue

            for block in snake2.blocks:
                if block[0] == head[0]:
                    if block[1] == head[1]:
                        return True
        return False
    
    def update(self):
        for username in self.snakes:
            snake = self.snakes[username]
            tail = snake.blocks[-1]
            ate = self.check_ate(snake)

            if ate:
                snake.update(True)
                head = snake.head
                self.food = self.empty_block()
                try:
                    self.board[head[0]][head[1]] = 1
                except:
                    pass

            else:
                snake.update(False)
                head = snake.head
                try:
                    self.board[head[0]][head[1]] = 1
                    self.board[tail[0]][tail[1]] = 0
                except:
                    pass

        dead = []
        for username in self.snakes:
            snake = self.snakes[username]
            if self.check_dead(snake):
                dead.append(username)

        for username in dead:
            self.snakes.pop(username)
            self.dead.append(username)


class Snake:
    def __init__(self, x, y):
        self.head = np.array([x, y])
        self.blocks = np.array([[x, y]])
        self.dir = random_dir()
        self.alive = True

    def update(self, ate):
        new_head = self.head + self.dir
        if not ate:
            self.blocks = self.blocks[:-1]

        self.blocks = np.concatenate((new_head.reshape(1, 2), self.blocks), axis=0)
        self.head = new_head

    def check_border(self):
        if self.head[0] < 0 or self.head[0] >= cols:
            self.alive = False

        if self.head[1] < 0 or self.head[1] >= rows:
            self.alive = False

    