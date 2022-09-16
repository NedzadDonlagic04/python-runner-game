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

        pygame.mouse.set_visible(False)

        self.clock = Clock(60)

        sky = Background('./images/sky.png', (0, 0))
        ground = Background('./images/ground.png', sky.rect.bottomleft)
        self.background = pygame.sprite.Group(sky ,ground)

        gameName = Text(150, (self.SCREEN_WIDTH / 2, 100), 'Runner')
        start = Text(70, (self.SCREEN_WIDTH / 2, gameName.rect.bottom + 50), 'Start')
        exit = Text(70, (self.SCREEN_WIDTH / 2, start.rect.bottom + 50), 'Exit')
        self.startText = pygame.sprite.Group(gameName, start, exit)

        self.arrows = TextArrows([start.rect, exit.rect])

    def quit(self):
        pygame.quit()
        exit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.arrows.moveUp()
                    elif event.key == pygame.K_DOWN:
                        self.arrows.moveDown()
                    elif event.key == pygame.K_RETURN and self.arrows.index:
                        self.quit()
                        

            self.background.draw(self.screen)

            self.startText.update()
            self.startText.draw(self.screen)
            
            self.arrows.draw(self.screen)

            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    game = Game(800, 400, 'Runner')
    game.run()