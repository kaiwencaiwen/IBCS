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

pixel[500, 500] = (255, 255, 255)
for point in range(0, 50000):
    for dir in range(4):
        startval = random.randint(1, 998)
        if dir == 0:
            for n in range(0, 1000):
                if pixel[startval, n] != (0, 0, 0) or pixel[startval + 1, n] != (0, 0, 0) or pixel[startval - 1, n] != (0, 0, 0):
                    red, green, blue = pixel[startval, n]
                    pixel[startval, n -
                          1] = (abs(255-500+startval),abs(255-500+n),abs(255-500+startval+n))
                    break
        if dir == 1:
            for n in range(0, 1000):
                if pixel[n, startval] != (0, 0, 0) or pixel[n, startval + 1] != (0, 0, 0) or pixel[n, startval - 1] != (0, 0, 0):
                    red, green, blue = pixel[startval, n]
                    pixel[n - 1,
                          startval] = (abs(255-500+startval),abs(255-500+n),abs(255-500+startval+n))
                    break
        if dir == 2:
            for n in range(0, 1000):
                if pixel[startval, 999 - n] != (0, 0, 0) or pixel[startval + 1, 999 - n] != (0, 0, 0) or pixel[startval - 1, 999 - n] != (0, 0, 0):
                    red, green, blue = pixel[startval, n]
                    pixel[startval, 1000 -
                          n] = (abs(255-500+startval),abs(255-500+n),abs(255-500+startval+n))
                    break
        if dir == 3:
            for n in range(0, 1000):
                if pixel[999 - n, startval] != (0, 0, 0) or pixel[999 - n, startval + 1] != (0, 0, 0) or pixel[999 - n, startval - 1] != (0, 0, 0):
                    red, green, blue = pixel[startval, n]
                    pixel[1000 - n,
                          startval] = (abs(255-500+startval),abs(255-500+n),abs(255-500+startval+n))
                    break
img.save("green.jpg")
img.show()