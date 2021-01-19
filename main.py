import pygame
import random
import time

pygame.init()

run = True
imgrun = True

MAX_HEIGHT = 480
MAX_WIDTH = 320
image_height, image_width = 18, 18

red = pygame.image.load("images//red.png")
orange = pygame.image.load("images//orange.png")
yellow = pygame.image.load("images//yellow.png")
green = pygame.image.load("images//green.png")
blue = pygame.image.load("images//blue.png")
purple = pygame.image.load("images//purple.png")
bgimage = pygame.image.load("images//background.png")

shapeI = [
    [0, 0, 1, 0,
     0, 0, 1, 0,
     0, 0, 1, 0,
     0, 0, 1, 0],
    [0, 0, 0, 0,
     0, 0, 0, 0,
     1, 1, 1, 1,
     0, 0, 0, 0]
]
shapeL = [
    [1, 0, 0, 0,
     1, 0, 0, 0,
     1, 1, 0, 0,
     0, 0, 0, 0],
    [1, 1, 1, 0,
     1, 0, 0, 0,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [1, 1, 0, 0,
     0, 1, 0, 0,
     0, 1, 0, 0,
     0, 0, 0, 0],
    [0, 0, 1, 0,
     1, 1, 1, 0,
     0, 0, 0, 0,
     0, 0, 0, 0]
]
shapeT = [
    [0, 1, 0, 0,
     1, 1, 0, 0,
     0, 1, 0, 0,
     0, 0, 0, 0],
    [0, 1, 0, 0,
     1, 1, 1, 0,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [0, 1, 0, 0,
     0, 1, 1, 0,
     0, 1, 0, 0,
     0, 0, 0, 0],
    [1, 1, 1, 0,
     0, 1, 0, 0,
     0, 0, 0, 0,
     0, 0, 0, 0]
]
shapeO = [
    [1, 1, 0, 0,
     1, 1, 0, 0,
     0, 0, 0, 0,
     0, 0, 0, 0]
]
shapeJ = [
    [0, 1, 0, 0,
     0, 1, 0, 0,
     1, 1, 0, 0,
     0, 0, 0, 0],
    [1, 0, 0, 0,
     1, 1, 1, 0,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [1, 1, 0, 0,
     1, 0, 0, 0,
     1, 0, 0, 0,
     0, 0, 0, 0],
    [1, 1, 1, 0,
     0, 0, 1, 0,
     0, 0, 0, 0,
     0, 0, 0, 0]
]
shapeS = [
    [0, 1, 1, 0,
     1, 1, 0, 0,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [1, 0, 0, 0,
     1, 1, 0, 0,
     0, 1, 0, 0,
     0, 0, 0, 0]
]
shapeZ = [
    [1, 1, 0, 0,
     0, 1, 1, 0,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [0, 1, 0, 0,
     1, 1, 0, 0,
     1, 0, 0, 0,
     0, 0, 0, 0]
]

shape = [shapeZ, shapeO, shapeL, shapeI, shapeS, shapeJ, shapeT]
colors = [red, orange, yellow, green, blue, purple]

def makeShape(screen):
    shapeNum = random.randint(0, len(shape) - 1)
    colorNum = random.randint(0, len(colors) - 1)
    for s in shape[shapeNum]:
        for i in range(4):
            for k in range(4):
                if s[i * 4 + k] == 1:
                    screen.blit(colors[colorNum], (i * image_height, k * image_width))
                else:
                    pass

clock = pygame.time.Clock()

while run:
    clock.tick(30)

    pygame.display.set_caption("tetris!")
    screen = pygame.display.set_mode(((MAX_WIDTH, MAX_HEIGHT)))
    screen.blit(red, (0, 0))
    screen.blit(bgimage, (0, 0))

    if imgrun:
        makeShape(screen)
        imgrun = False

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    pygame.display.update()