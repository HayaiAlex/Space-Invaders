import random
import pygame
import pygame.freetype
from invader import invader
from player import player
from block import block
from bullet import bullet

pygame.init()
myfont = pygame.freetype.SysFont("Arial", 20)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Space Invaders")

player = player(SCREEN_WIDTH/2-player.width/2, SCREEN_HEIGHT - 50, screen)

blocks = []
num_of_blocks = 6
spacing = SCREEN_WIDTH/(num_of_blocks+1)
for i in range(0, num_of_blocks):
    x = i*spacing + spacing - block.width/2
    y = SCREEN_HEIGHT - 100
    blocks.append(block(x, y, screen))

invaders = []
num_of_invaders = 10
spacing = SCREEN_WIDTH/(num_of_invaders+1)
for i in range(0, num_of_invaders):
    x = i*spacing + spacing - invader.width/2
    y = 50
    invaders.append(invader(x, y, screen))


bullets = []

RUNNING = True
clock = pygame.time.Clock()
while RUNNING:
    clock.tick(60)


    screen.fill((255, 150, 255))

    # TEXT = "Score: "
    # text_surface, rect = myfont.render(TEXT, (255, 255, 255))
    # screen.blit(text_surface, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            RUNNING = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append(player.shoot())
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        player.move(1)
    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        player.move(-1)


    for block in blocks:
        block.show()

    for bullet in bullets:
        bullet.update()
        bullet.show()

        # if touching an invader
        for invader in invaders:
            if bullet.colour != invader.colour:
                if bullet.get_touching(invader):
                    bullets.remove(bullet)
                    invaders.remove(invader)
        
        if bullet.colour != player.colour:
            if bullet.get_touching(player):
                bullets.remove(bullet)
                print("You died")
        

        # if touching a block remove
        for block in blocks:
            if bullet.get_touching(block):
                bullets.remove(bullet)

        # if offscreen remove
        if bullet.y < 0 or bullet.y > SCREEN_HEIGHT:
            bullets.remove(bullet)

    for invader in invaders:
        invader.update()
        invader.show()
        
        shoot_chance = random.random()
        if shoot_chance > 0.99:
            bullets.append(invader.shoot())
            

    player.show()


    if len(invaders) == 0:
        print("You win")

    pygame.display.update()
