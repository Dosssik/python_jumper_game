import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
game_finished = False

speed = 10

x = 100
y = 100

height = 50
width = 50

while not game_finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_finished = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    elif keys[pygame.K_DOWN]:
        y += speed
    elif keys[pygame.K_UP]:
        y -= speed

    screen.fill((192, 192, 255))
    pygame.draw.rect(screen, (100, 100, 100), (x, y, height, width))
    pygame.display.update()
    clock.tick(60)
