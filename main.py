import sys

import pygame

class Game:

    def __init__(self):

        self.screen = None

        self.game_init()


    def game_init(self):
        
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))


def main():
    game = Game()
    



if __name__ == "__main__":
    main()