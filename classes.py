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