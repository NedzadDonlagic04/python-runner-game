import pygame

class Clock():
    def __init__(self, fps):
        self.fps = fps
        self.clock = pygame.time.Clock()

    def tick(self):
        self.clock.tick(self.fps)

class Background(pygame.sprite.Sprite):
    def __init__(self, path, pos):
        super().__init__()
        self.image = pygame.image.load(path).convert()
        self.rect = self.image.get_rect( topleft = pos )

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
        

