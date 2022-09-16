import pygame
from sys import exit
from classes import *

class Game():

    def __init__(self, width, height, title='pygame'):
        pygame.init()
        
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.screen = pygame.display.set_mode((width, height))

        pygame.display.set_caption(title)

        self.clock = Clock(60)

        sky = Background('./images/sky.png', (0, 0))
        ground = Background('./images/ground.png', sky.rect.bottomleft)

        self.background = pygame.sprite.Group(sky ,ground)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.background.draw(self.screen)

            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    game = Game(800, 400, 'Runner')
    game.run()