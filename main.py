from sre_constants import JUMP
import pygame
from sys import exit
from classes import *

class Game():

    MAIN_MENU = 0
    PLAYING = 1
    GAME_OVER = 2

    def __init__(self, width, height, title='pygame'):
        pygame.init()
        
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.screen = pygame.display.set_mode((width, height))

        pygame.display.set_caption(title)

        pygame.mouse.set_visible(False)

        self.clock = Clock(60)

        sky = Background('./images/background/sky.jpg', (0, 0), self.SCREEN_WIDTH)
        ground = Background('./images/background/ground.jpg', sky.rect.bottomleft, self.SCREEN_WIDTH)
        self.background = [sky, ground]

        gameName = Text(150, (self.SCREEN_WIDTH / 2, 100), 'Runner')
        start = Text(70, (self.SCREEN_WIDTH / 2, gameName.rect.bottom + 50), 'Start')
        exit = Text(70, (self.SCREEN_WIDTH / 2, start.rect.bottom + 50), 'Exit')
        self.startText = pygame.sprite.Group(gameName, start, exit)

        gameOver = Text(150, (self.SCREEN_WIDTH / 2, 100), 'Game Over', 'Red')
        restart = Text(70, (self.SCREEN_WIDTH / 2, gameOver.rect.bottom + 50), 'Restart')
        menu = Text(70, (self.SCREEN_WIDTH / 2, restart.rect.bottom + 50), 'Main Menu')
        self.loseText = pygame.sprite.Group(gameOver, restart, menu)

        self.states = [
            [start.rect, exit.rect],
            [],
            [restart.rect, menu.rect]
        ]
        self.current_state = self.MAIN_MENU

        self.arrows = TextArrows(self.states[self.current_state])

        self.player = pygame.sprite.GroupSingle( Player( (ground.rect.left + 50, ground.rect.top) ) )

    def quit(self):
        pygame.quit()
        exit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                elif self.current_state != self.PLAYING and event.type == pygame.KEYDOWN:
                    
                    self.background[0].speed = 1
                    self.background[1].speed = 1

                    if event.key == pygame.K_UP:
                        self.arrows.moveUp()

                    elif event.key == pygame.K_DOWN:
                        self.arrows.moveDown()

                    elif self.current_state == self.MAIN_MENU and event.key == pygame.K_RETURN and self.arrows.index:
                        self.quit()

                    elif self.current_state == self.GAME_OVER and event.key == pygame.K_RETURN and self.arrows.index:
                        self.current_state = self.MAIN_MENU
                        self.arrows.fillPositions(self.states[self.MAIN_MENU])

                    elif ( self.current_state == self.MAIN_MENU or self.current_state == self.GAME_OVER ) and event.key == pygame.K_RETURN and not self.arrows.index:
                        self.current_state = self.PLAYING
                        self.background[0].speed = 2
                        self.background[1].speed = 2
                
                elif self.current_state == self.PLAYING and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.player.update(jump=True)
        
            for bg in self.background:
                bg.update()
                bg.draw(self.screen)

            if self.current_state == self.MAIN_MENU:
                self.startText.draw(self.screen)
                self.arrows.draw(self.screen)
            
            elif self.current_state == self.GAME_OVER:
                self.loseText.draw(self.screen)
                self.arrows.draw(self.screen)
            
            else:
                self.player.update()
                self.player.draw(self.screen)

            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    game = Game(800, 400, 'Runner')
    game.run()