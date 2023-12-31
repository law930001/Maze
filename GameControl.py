import sys

import pygame
from pygame.locals import QUIT

from GameSettings import COLOR, WINDOW_ATTRIBUTE
from GameObjects import GameObjects

class GameControl:

    def __init__(self):

        self.screen = None
        self.game_objects = GameObjects()

        self.init_window()
        self.init_objects()

        # pygame.key.set_repeat(400, 200)

    def init_window(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode(
            [WINDOW_ATTRIBUTE["window_size"][1], WINDOW_ATTRIBUTE["window_size"][0]]
        )
        pygame.display.set_caption("Hello world!")
        self.screen.fill(COLOR["light_gray"])

    def init_objects(self):
        self.game_objects.initialize()

    def update_objects(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.game_objects.object[self.game_objects.player[0] - 1][self.game_objects.player[1]] != 2:
                    self.game_objects.player[0] -= 1
            if event.key == pygame.K_DOWN:
                if self.game_objects.object[self.game_objects.player[0] + 1][self.game_objects.player[1]] != 2:
                    self.game_objects.player[0] += 1
            if event.key == pygame.K_RIGHT:
                if self.game_objects.object[self.game_objects.player[0]][self.game_objects.player[1] + 1] != 2:
                    self.game_objects.player[1] += 1
            if event.key == pygame.K_LEFT:
                if self.game_objects.object[self.game_objects.player[0]][self.game_objects.player[1] - 1] != 2:
                    self.game_objects.player[1] -= 1

    def draw_objects(self):
        # draw maze
        for r in range(self.game_objects.raw_object_count):
            for c in range(self.game_objects.col_object_count):
                if self.game_objects.object[r][c] == 1: # space
                    pygame.draw.rect(
                        surface=self.screen, 
                        color=COLOR["light_gray"], 
                        rect=[[self.game_objects.rects[r][c][1], self.game_objects.rects[r][c][0]], WINDOW_ATTRIBUTE["object_size"]],
                        width=0
                    )
                elif self.game_objects.object[r][c] == 2: # wall
                    pygame.draw.rect(
                        surface=self.screen, 
                        color=COLOR["blue_green"], 
                        rect=[[self.game_objects.rects[r][c][1], self.game_objects.rects[r][c][0]], WINDOW_ATTRIBUTE["object_size"]],
                        width=0
                    )
                elif self.game_objects.object[r][c] == 3: # solution path
                    pygame.draw.rect(
                        surface=self.screen, 
                        color=COLOR["yellow"], 
                        rect=[[self.game_objects.rects[r][c][1], self.game_objects.rects[r][c][0]], WINDOW_ATTRIBUTE["object_size"]],
                        width=0
                    )
                elif self.game_objects.object[r][c] == 4: # start point
                    pygame.draw.rect(
                        surface=self.screen, 
                        color=COLOR["light_red"], 
                        rect=[[self.game_objects.rects[r][c][1], self.game_objects.rects[r][c][0]], WINDOW_ATTRIBUTE["object_size"]],
                        width=0
                    )
                elif self.game_objects.object[r][c] == 5: # end point
                    pygame.draw.rect(
                        surface=self.screen, 
                        color=COLOR["light_orange"], 
                        rect=[[self.game_objects.rects[r][c][1], self.game_objects.rects[r][c][0]], WINDOW_ATTRIBUTE["object_size"]],
                        width=0
                    )
        # draw player
        player_pos = self.game_objects.rects[self.game_objects.player[0]][self.game_objects.player[1]]
        player_pos = [
            player_pos[0] + WINDOW_ATTRIBUTE["object_size"][0] // 2,
            player_pos[1] + WINDOW_ATTRIBUTE["object_size"][1] // 2
        ]
        pygame.draw.circle(
            surface=self.screen,
            color=COLOR["deep_blue"],
            center=[player_pos[1], player_pos[0]],
            radius=WINDOW_ATTRIBUTE["object_size"][0] // 3,
            width=0
        )

    def loop_run(self):

        while True:
            # loop to handle game event
            for event in pygame.event.get():
                # exit when closing window
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                # update objects
                self.update_objects(event)

            # draw objects
            self.draw_objects()
            # update pygame
            pygame.display.update()