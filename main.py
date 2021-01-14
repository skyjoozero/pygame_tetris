import pygame

pygame.init()

size = [300, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris!")

clock = pygame.time.Clock()

run = True

spriteImg = pygame.image.load("images//tiles.png")

blue = pygame.image.load(spriteImg, )

while run:
    clock.tick(10)

    screen.blit(spriteImg, (0, 0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    pygame.display.update
    
