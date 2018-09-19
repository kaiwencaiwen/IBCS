from PIL import Image
img = Image.new("RGB", (500, 500), "black")


def set_pixel(img, x, y, r, g, b):
    pixel = img.load()
    pixel[x, y] = (r, g, b)


# horizontal line
for x in range(0, 200):
    set_pixel(img, x, 200, 255, 255, 255)

# vertical line
for y in range(0, 200):
    set_pixel(img, 200, y, 255, 255, 255)

# arbitrary line
end1 = (100, 100)
end2 = (0, 0)


def arbline(end1, end2):
    if end1[0] > end2[0]:
        end2, end1 = end1, end2
    y = end1[1]
    for x in range(end1[0], end2[0]):
        y += (end2[1] - end1[1]) / abs(end2[0] - end1[0])
        set_pixel(img, x, y, 255, 255, 255)


arbline(end1, end2)

# rectangle
topleft = (200, 300)
bottomright = (400, 400)
for x in range(topleft[0], bottomright[0]):
    set_pixel(img, x, topleft[1], 255, 255, 255)

for x in range(topleft[0], bottomright[0]):
    set_pixel(img, x, bottomright[1], 255, 255, 255)

for y in range(topleft[1], bottomright[1]):
    set_pixel(img, topleft[0], y, 255, 255, 255)

for y in range(topleft[1], bottomright[1]):
    set_pixel(img, bottomright[0], y, 255, 255, 255)

# quadrilateral
corner1 = (170, 100)
corner2 = (400, 200)
corner3 = (350, 150)
corner4 = (200, 100)
arbline(corner1, corner2)
arbline(corner2, corner3)
arbline(corner3, corner4)
arbline(corner4, corner1)


# circle
circcenter = (200, 200)
circradius = 50
for x in range(0, 500):
    for y in range(0, 500):
        if (x - circcenter[0])**2 + (y - circcenter[1])**2-circradius**2<0:
            set_pixel(img, x, y, 255, 255, 255)


# rectangle gradient
for x in range(0,200):
    for y in range(400,500):
        set_pixel(img, x, y, x, y-200, x)

# rectangle gradient
for x in range(0,200):
    for y in range(400,500):
        set_pixel(img, x, y, x, y-200, 255-x)

# circle gradient
circcenter = (400, 400)
circradius = 50
for x in range(0, 500):
    for y in range(0, 500):
        dis =(x - circcenter[0])**2 + (y - circcenter[1])**2
        if dis-circradius**2<0:
            set_pixel(img, x, y, int(dis/6), 30+int(dis/8), 255-int(dis/10))
img.save('myimage.jpg')