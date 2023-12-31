import random
import time

class Agent:

    def __init__(self, game_objects):
        self.game_objects = game_objects
        pass

    def run(self):
        self.random_walk()

    def random_walk(self):
        four_dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        x, y = random.choice(four_dir)
        new_x, new_y = self.game_objects.player[0] + x, self.game_objects.player[1] + y
        if self.game_objects.object[new_x][new_y] != 2: # not wall
            self.game_objects.player = [new_x, new_y]
