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