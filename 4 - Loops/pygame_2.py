# Q5
import pygame
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('STUFF')
clock = pygame.time.Clock()

running = True
size = 50

rectsize = 5


def rectdraw(color, xpos, ypos):
    pygame.draw.rect(screen, color, (xpos, ypos, rectsize, rectsize), 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    starty = 0
    startr = 255
    startg = 255
    startb = 255
    height = 100
    for r in range(height):
        startr = 255
        startx = rectsize * (height - 1 - r)
        for k in range(2 * r + 1):
            rectdraw([startr, startg, startb], startx, starty)
            startx += rectsize
            startr -= 1
        starty += rectsize
        startg -= 2

    pygame.display.update()
    clock.tick(60)
pygame.quit()
