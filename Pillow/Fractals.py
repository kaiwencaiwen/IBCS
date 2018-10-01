from PIL import Image
import random
img = Image.new("RGB", (5000, 5000), "black")
pixel = img.load()

centerx = 2500
centery = 2500
size = 1250


def square(cx, cy, cs):
    for x in range(cx - cs, cx + cs):
        for y in range(cy - cs, cy + cs):
            pixel[x, y] = (255, 255, 255)


square(centerx, centery, size)


def fractalstep(fcx, fcy, fsize):
    square(fcx, fcy, fsize)
    nsize = int(fsize/2)
    if nsize >= 1:
        fractalstep(fcx + 2 * nsize, fcy + 2 * nsize, nsize)
        fractalstep(fcx - 2 * nsize, fcy - 2 * nsize, nsize)
        fractalstep(fcx - 2 * nsize, fcy + 2 * nsize, nsize)
        fractalstep(fcx + 2 * nsize, fcy - 2 * nsize, nsize)


fractalstep(centerx, centery, size)

img.save("fractal.jpg")
img.show()
