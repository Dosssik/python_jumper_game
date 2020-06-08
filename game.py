import pygame
from hero import Hero
from hero import HeroState

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game_finished = False

moving_step = 10

x = 100
y = 100

rect_height = 150
rect_width = 150

isInJump = False
jumpCounter = 10
hero = Hero(rect_height, rect_width)


def do_jump():
    global isInJump, jumpCounter, y
    if jumpCounter >= -10:
        if jumpCounter < 0:
            y += (jumpCounter ** 2) / 3
        else:
            y -= (jumpCounter ** 2) / 3
        jumpCounter -= 1
    else:
        isInJump = False
        jumpCounter = 10


while not game_finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_finished = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > moving_step:
        hero.update(HeroState.left)
        x -= moving_step
    elif keys[pygame.K_RIGHT] and x < screen_width - rect_width - moving_step:
        hero.update(HeroState.right)
        x += moving_step
    elif isInJump:
        hero.update(HeroState.jump)
        do_jump()
    else:
        hero.update(HeroState.idle)
        if keys[pygame.K_DOWN] and y < screen_height - rect_height - moving_step:
            y += moving_step
        elif keys[pygame.K_UP] and y > moving_step:
            y -= moving_step
        elif keys[pygame.K_SPACE]:
            isInJump = True

    screen.fill((192, 192, 255))
    hero.draw(screen, x, y)
    pygame.display.update()
    clock.tick(60)
