import sys
import random

import pygame
from pygame.locals import QUIT

COLOR = {
    "deep_blue" : (0, 50, 100),
    "light_gray": (188, 188, 188),
    "light_red": (200, 0 ,0),
    "blue_green": (0, 106, 128)
}

WINDOW_ATTRIBUTE = {
    "window_size": (800, 800),
    "object_size": (40, 40)
}

class GameObjects:

    def __init__(self):

        self.raw_object_count = WINDOW_ATTRIBUTE["window_size"][0] // WINDOW_ATTRIBUTE["object_size"][0]
        self.col_object_count = WINDOW_ATTRIBUTE["window_size"][1] // WINDOW_ATTRIBUTE["object_size"][1]

        self.rects = [[[0] * 2 for _ in range(self.raw_object_count)] for _ in range(self.col_object_count)]
        self.object = [[0] * self.raw_object_count for _ in range(self.col_object_count)]
        self.start_point = None
        self.end_point = None

    def initialize(self):
        
        for r in range(self.raw_object_count):
            for c in range(self.col_object_count):
                # init rects position
                self.rects[r][c] = [r * WINDOW_ATTRIBUTE["object_size"][0], c * WINDOW_ATTRIBUTE["object_size"][1]]
                # init object
                self.object[r][c] = random.choice([0,1,2]) # 0: space, (1,2): wall
        pass

class Game:

    def __init__(self):

        self.screen = None
        self.game_objects = GameObjects()

        self.init_window()
        self.init_objects()

    def init_window(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_ATTRIBUTE["window_size"])
        pygame.display.set_caption("Hello world!")
        self.screen.fill(COLOR["light_gray"])

    def init_objects(self):
        self.game_objects.initialize()

    def update_objects(self):
        pass

    def draw_objects(self):
        for r in range(self.game_objects.raw_object_count):
            for c in range(self.game_objects.col_object_count):
                if self.game_objects.object[r][c] == 0: # space
                    pygame.draw.rect(
                        surface=self.screen, 
                        color=COLOR["light_gray"], 
                        rect=[self.game_objects.rects[r][c], WINDOW_ATTRIBUTE["object_size"]],
                        width=0
                    )
                elif self.game_objects.object[r][c] == 1: # wall
                    pygame.draw.rect(
                        surface=self.screen, 
                        color=COLOR["blue_green"], 
                        rect=[self.game_objects.rects[r][c], WINDOW_ATTRIBUTE["object_size"]],
                        width=0
                    )

    def run(self):

        while True:
            # loop to handle game event
            for event in pygame.event.get():
                # exit when closing window
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # update objects
            self.update_objects()
            # draw objects
            self.draw_objects()
            # update pygame
            pygame.display.update()


def main():
    game = Game()
    game.run()



if __name__ == "__main__":
    main()