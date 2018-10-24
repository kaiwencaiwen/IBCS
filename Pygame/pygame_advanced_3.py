import pygame
from PIL import Image
# from PIL import ImageFilter
# blurfilt=ImageFilter.GaussianBlur(radius=2)
img = Image.open("pete.jpg", 'r')
# img=Image.filter(blurfilt)
pixel = img.load()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('peter picture')
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for xpos in range(400):
        for ypos in range(400):
            screen.fill(pixel[xpos, ypos], ((xpos, ypos), (1, 1)))
    pygame.display.update()
    clock.tick(30)
pygame.quit()
