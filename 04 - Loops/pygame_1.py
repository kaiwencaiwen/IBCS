# Q4
import pygame
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('STUFF')
clock = pygame.time.Clock()

running = True
size = 50

white = (255, 255, 255)
black = (0, 0, 0)


def rectdraw(color, xpos, ypos):
    pygame.draw.rect(screen, color, (xpos, ypos, 100, 100), 0)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    startx = 0
    starty = 0
    for n in range(5):
        if n % 2:
            chcolor = white
        else:
            chcolor = black
        for q in range(5):
            rectdraw(chcolor, startx, starty)
            startx += 100
            if chcolor == black:
                chcolor = white
            else:
                chcolor = black
        startx = 0
        starty += 100
    pygame.display.update()
    clock.tick(60)
pygame.quit()
