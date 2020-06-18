import pygame
class block:
    width = 50
    height = 25

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen

    def update(self):
        pass

    def show(self):
        square = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, (255, 255, 255), square)
