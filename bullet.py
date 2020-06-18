import math
import pygame
class bullet:
    radius = 5
    move_step = 3

    def __init__(self, x, y, direction, colour, screen):
        self.x = x
        self.y = y
        self.direction = direction
        self.colour = colour
        self.screen = screen

    def update(self):
        self.y += self.direction*self.move_step

    def show(self):
        pygame.draw.circle(self.screen, self.colour, (int(self.x), int(self.y)), self.radius)

    def get_touching(self, entity):
        if self.y + self.radius < entity.y + entity.height and self.y + self.radius > entity.y:
            # within entity's y axis
            if self.x + self.radius > entity.x and self.x - self.radius < entity.x + entity.width:
                # also within entity's x axis
                return True
        return False
