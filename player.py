import pygame
from bullet import bullet
class player:
    width = 50
    height = 25
    move_step = 5
    colour = (255, 255, 255)

    def __init__(self, x, y, screen):
        self.screen = screen
        self.x = x
        self.y = y


    def update(self):
        pass

    def show(self):
        square = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.colour, square)

    def move(self, direction):
        self.x += direction * self.move_step

    def shoot(self):
        return bullet(self.x+self.width/2, self.y+self.height/2, -1, self.colour, self.screen)
