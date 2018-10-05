from PIL import Image
import random
img = Image.new("RGB", (500, 500), "black")


antx = 250
anty = 250
direction = 3


def antstep():
    global antx,anty,direction
    if direction == 1:
        anty -= 1
    elif direction == 2:
        antx += 1
    elif direction == 3:
        anty += 1
    elif direction == 4:
        antx -= 1


while antx < 499 and antx > 0 and anty < 499 and anty > 0:
    pixel = img.load()
    if pixel[antx, anty] == (0, 0, 0):
        pixel[antx, anty] = (255, 255, 255)
        if direction == 4:
            direction = 1
        else:
            direction += 1
    elif pixel[antx, anty]== (255, 255, 255):
        pixel[antx,anty]=(0,0,0)
        if direction==1:
            direction=4
        else:
            direction-=1
    antstep()
img.save("ant.jpg")
img.show()
