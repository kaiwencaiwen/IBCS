import pygame
import random
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Wanderer')
clock = pygame.time.Clock()
running = True
wanderpos = [300, 300]


def pixel():
    screen.fill((255, 255, 255), (wanderpos, (1, 1)))


wandermove = (1, 0)


def changedir():
    choiceset = []
    if wandermove != (0, 1) and wandermove != (0, -1):
        if screen.get_at((wanderpos[0], wanderpos[1] + 1)) != (255, 255, 255, 255):
            choiceset.append(0)
        if screen.get_at((wanderpos[0], wanderpos[1] - 1)) != (255, 255, 255, 255): 
            choiceset.append(1)
    elif wandermove != (1, 0) and wandermove != (-1, 0):
        if screen.get_at((wanderpos[0]+1, wanderpos[1])) != (255, 255, 255, 255): 
            choiceset.append(2)
        if screen.get_at((wanderpos[0]-1, wanderpos[1])) != (255, 255, 255, 255): 
            choiceset.append(3)
    try:
        return [(0, 1), (0, -1), (1, 0), (-1, 0)][random.choice(choiceset)]
    except:
        pathclear=False
        return(0,0)

def collide():
    if screen.get_at((wanderpos[0] + wandermove[0], wanderpos[1] + wandermove[1])) == (255, 255, 255, 255):
        return True
    else:
        return False


stepcount = 0
pathlength = random.randint(10, 50)
wandering = True
wandermove = changedir()
pathclear=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # path length reached or collide
    if pathclear and wanderpos[0]>1 and wanderpos[0]<599 and wanderpos[1]>1 and wanderpos[0]<599:
        if pathlength == stepcount or collide():
            stepcount = 0
            pathlength = random.randint(10, 50)
            wandermove = changedir()
        # move a step
        pixel()
        #print(wandermove)
        wanderpos[0] += wandermove[0]
        wanderpos[1] += wandermove[1]
        stepcount += 1
    pygame.display.update()
    clock.tick(300)
pygame.quit()
