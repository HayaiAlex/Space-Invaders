import pygame
from bullet import bullet
class invader:
    width = 25
    height = 20
    move_step = 2.5
    direction = 1
    colour = (255, 0, 100)

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen

    def update(self):
        self.x += self.direction * self.move_step
        if self.x > self.screen.get_width()-self.width-25:
            self.direction = -1
            self.y += self.height
        elif self.x < 25:
            self.direction = 1
            self.y += self.height


    def show(self):
        square = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.colour, square)

    def shoot(self):
        return bullet(self.x+self.width/2, self.y+self.height/2, 1, self.colour, self.screen)
