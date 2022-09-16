import pygame
from sys import exit

class Game():

    def __init__(self, width, height, title='pygame'):
        pygame.init()
        
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.screen = pygame.display.set_mode((width, height))

        pygame.display.set_caption(title)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.update()

if __name__ == '__main__':
    game = Game(800, 400, 'Runner')
    game.run()