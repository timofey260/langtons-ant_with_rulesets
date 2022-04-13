import time
import pygame
from time import sleep
from os import system

print("(arguments can use), [example]")
rule = list(input("rule(l, r, c)[rl]: "))
bs = 5
run = True
color0 = [255, 255, 255]
color1 = [0, 0, 0]
color = [255, 255, 255]
rot = 3
colrules = []
exrules = []  # exit rules
colors = []  # color list
num = 1
for a in rule:
    t = [a, num, color]
    colrules.append(t)
    num += 1
colrules[-1][1] = 0
num = 0

for all in range(0, len(rule)):
    c = 255 - (255 / len(rule)) * all
    color = [c, c, c]
    colors.append(color)
for all in colrules:
    s = [all[0], all[1], colors[num]]
    exrules.append(s)
    num += 1
print(exrules)
del colors, colrules, rule


def mapcreate(map):
    window.fill(color0)
    inx = 0
    iny = 0
    sizey = bs * iny
    sizex = bs * inx
    for list in map:
        for box in list:
            pygame.draw.rect(window, box[-1], (sizex, sizey, bs, bs))
            inx += 1
            sizex = bs * inx
        iny += 1
        sizey = bs * iny
        inx = 0
        sizex = bs * inx


n = 0.1
auto = False
mw = 200
mh = 200


def a():
    global map
    mhl = []
    mwl = []
    for _ in range(mh):
        for _ in range(mw):
            mwl.append(exrules[0])
        mhl.append(mwl)
        mwl = []
    map = mhl


x = round(mw / 2) * bs
y = round(mh / 2) * bs


def step():
    global rot, x, y
    if rot == 4:
        rot = 0
    elif rot == -1:
        rot = 3

    if rot == 0:
        y -= bs
    elif rot == 1:
        x += bs
    elif rot == 2:
        y += bs
    elif rot == 3:
        x -= bs


def next():
    global rot
    nx = int(x / bs)
    ny = int(y / bs)
    if map[ny][nx][0] == "l":
        rot += 1
    elif map[ny][nx][0] == "r":
        rot -= 1
    elif map[ny][nx][0] == "c":
        pass
    map[ny][nx] = exrules[map[ny][nx][1]]
    step()


a()
pygame.init()
window = pygame.display.set_mode([mw * bs, mh * bs])
pygame.display.set_caption('game')
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                next()
            elif event.key == pygame.K_f:
                a()
            elif event.key == pygame.K_BACKSPACE:
                run = False
            elif event.key == pygame.K_t:
                n += 0.1
            elif event.key == pygame.K_g:
                n -= 0.1
            elif event.key == pygame.K_x:
                if auto:
                    auto = False
                else:
                    auto = True
    if auto:
        next()
    mapcreate(map)
    pygame.draw.rect(window, [255, 0, 0], (x, y, bs, bs), 2)
    pygame.display.flip()
    pygame.display.update()
pygame.quit()
