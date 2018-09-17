from PIL import Image
import random
img = Image.new("RGB", (1000, 1000), "black")
pixel = img.load()

# for n in range(0, 1000):
#     for j in range(0, 1000):
#         # a = random.randint(125, 255)
#         # b = random.randint(0, 125)
#         # c = random.randint(0, 125)
#         pixel[n, j] = (int(n/4), int(j/4), 255)
# red, green, blue = pixel[250, 250]


def discalc(x, y):
    return int((((500 - x)**2) + ((500 - y)**2))**0.5)


pixel[500, 500] = (0, 255, 0)
for point in range(0, 200000):
    for dir in range(4):
        startval = random.randint(1, 998)
        if dir == 0:
            for n in range(1, 1000):
                if pixel[startval, n][1] + pixel[startval + 1, n][1] + pixel[startval - 1, n][1] != 0:
                    pixel[startval, n - 1] = (0, 355 - discalc(startval, n - 1), 0)
                    break
        elif dir == 1:
            for n in range(1, 1000):
                if pixel[n, startval][1] + pixel[n, startval + 1][1] + pixel[n, startval - 1][1] != 0:
                    pixel[n - 1, startval] = (0, 355 - discalc(n - 1, startval), 0)
                    break
        elif dir == 2:
            for n in range(1, 999):
                if pixel[startval, 999 - n][1] + pixel[startval + 1, 999 - n][1] + pixel[startval - 1, 999 - n][1] != 0:
                    pixel[startval, 1000 - n] = (0, 355 - discalc(startval, 1000 - n), 0)
                    break
        else:
            for n in range(1, 999):
                if pixel[999 - n, startval][1] + pixel[999 - n, startval + 1][1] + pixel[999 - n, startval - 1][1] != 0:
                    pixel[1000 - n, startval] = (0, 355 - discalc(1000 - n, startval), 0)
                    break
img.save("green.jpg")
img.show()
