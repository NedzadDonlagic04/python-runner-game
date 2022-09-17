import pygame
import math

class Clock():
    def __init__(self, fps):
        self.FPS = fps
        self.clock = pygame.time.Clock()

    def tick(self):
        self.clock.tick(self.FPS)

class Background():
    def __init__(self, path, pos, SCREEN_WIDTH):
        super().__init__()
        self.image = pygame.image.load(path).convert()
        self.rect = self.image.get_rect( topleft = pos )

        self.count = math.ceil( SCREEN_WIDTH / self.image.get_width() ) + 1
        self.scroll = 0
        self.speed = 1

    def update(self):
        self.scroll -= self.speed

        if self.scroll < self.image.get_width() * -1:
            self.scroll = 0

    def draw(self, screen):
        for i in range(0, self.count):
            screen.blit(self.image, (i * self.image.get_width() + self.scroll, self.rect.top))
        

class Text(pygame.sprite.Sprite):
    def __init__(self, font_size, pos, text, color='Black'):
        super().__init__()

        self.text_font = pygame.font.Font('./fonts/Pixeltype.ttf', font_size)
        self.image = self.text_font.render(text, False, color)
        self.rect = self.image.get_rect( center = pos )

class TextArrows():
    def __init__(self, text_rects):
        self.positions = None
        self.fillPositions(text_rects)

        self.sound = pygame.mixer.Sound('./sounds/optionChange.mp3')

    def fillPositions(self, text_rects):
        self.positions = []
        for pos in self.generatePositions(text_rects):
            self.positions.append(pos)
        
        self.index = 0
        self.posLen = len(self.positions)

    def generatePositions(self, text_rects):
        for rect in text_rects:
            x1, y1 = rect.topleft
            x1 -= 40

            x2 = x1
            y2 = rect.bottomleft[1]
            y2 -= 10

            x3 = x1 + 20
            y3 = (y2 + y1) / 2

            yield [(x1, y1), (x2, y2), (x3, y3)]

    def draw(self, screen):
        pos = self.positions[self.index]
        pygame.draw.polygon(screen, (0, 0, 0), [
            pos[0], pos[1], pos[2]
        ])
    
    def moveUp(self):
        if self.index - 1 < 0:
            self.index = self.posLen - 1
        else:
            self.index -= 1
        self.sound.play()

    def moveDown(self):
        if self.index + 1 == self.posLen:
            self.index = 0
        else:
            self.index += 1
        self.sound.play()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.walk1 = pygame.image.load('./images/player/player_walk_1.png').convert_alpha()
        self.walk2 = pygame.image.load('./images/player/player_walk_2.png').convert_alpha()
        self.jump = pygame.image.load('./images/player/jump.png').convert_alpha()
        self.fall = pygame.image.load('./images/player/fall.png').convert_alpha()

        self.image = self.walk1
        self.rect = self.image.get_rect( bottomleft = pos)

        self.count = 0
        self.originalPos = self.rect.bottom
        self.gravity = 0
        self.jumpState = False

    def update(self, jump=False):
        if jump and self.jumpState == False:
            self.gravity = -22
            self.jumpState = True
            self.image = self.jump

        if not self.jumpState:
            self.count += 1
            if self.count == 8:
                self.count = 0
                self.image = self.walk1 if self.image != self.walk1 else self.walk2
        else:
            self.gravity += 1
            self.rect.bottom += self.gravity

            if self.gravity > 0:
                self.image = self.fall

            if self.rect.bottom > self.originalPos:
                self.jumpState = False
                self.rect.bottom = self.originalPos

