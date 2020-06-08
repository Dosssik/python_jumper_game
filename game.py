import pygame

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game_finished = False

moving_step = 10

x = 100
y = 100

rect_height = 50
rect_width = 50

isInJump = False
jumpCounter = 10

while not game_finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_finished = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > moving_step:
        x -= moving_step
    elif keys[pygame.K_RIGHT] and x < screen_width - rect_width - moving_step:
        x += moving_step
    elif isInJump:
        if jumpCounter >= -10:
            if jumpCounter < 0:
                y += (jumpCounter ** 2) / 3
            else:
                y -= (jumpCounter ** 2) / 3
            jumpCounter -= 1
        else:
            isInJump = False
            jumpCounter = 10
    else:
        if keys[pygame.K_DOWN] and y < screen_height - rect_height - moving_step:
            y += moving_step
        elif keys[pygame.K_UP] and y > moving_step:
            y -= moving_step
        elif keys[pygame.K_SPACE]:
            isInJump = True

    screen.fill((192, 192, 255))
    rect_background = (100, 100, 100)
    pygame.draw.rect(screen, rect_background, (x, y, rect_height, rect_width))
    pygame.display.update()
    clock.tick(60)
