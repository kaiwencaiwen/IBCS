import pygame
import random
import math
import itertools
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Spiral')
clock = pygame.time.Clock()
running = True


def radialdraw(radgree, distance):
    xpos = int(distance * math.cos(radgree))
    ypos = int(distance * math.sin(radgree))
    pygame.draw.circle(screen, (255 - 0.2 * distance, 200 - 0.3 * distance, 255 - 0.2 * distance),
                       (xpos + 300, ypos + 300), int(4 + distance / 50), 0)
    # pygame.draw.line(screen, (255 - 0.2 * distance, 200 - 0.3 * distance, 255 - 0.2 * distance), (xpos+300, ypos+300), (300, 300), 3)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for n in range(400):
        radialdraw(n, n)

    pygame.display.update()
    clock.tick(30)
pygame.quit()
