import pygame
from hero import Hero
from hero import HeroState
import random
from enemy import Enemy
from enemy import enemy_size

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen_background_image = pygame.image.load("images/game_bg.jpg")

pygame.time.set_timer(pygame.USEREVENT+1, 700)
clock = pygame.time.Clock()
game_finished = False

moving_step = 10

hero_height = 150
hero_width = 150

hero_location_x = screen_width / 2
hero_location_y = screen_height - hero_height

isInJump = False
jumpCounter = 20
hero = Hero(hero_height, hero_width)

enemies = []


def do_jump():
    global isInJump, jumpCounter, hero_location_y
    if jumpCounter >= -20:
        if jumpCounter < 0:
            hero_location_y += (jumpCounter ** 2) / 9
        else:
            hero_location_y -= (jumpCounter ** 2) / 9
        jumpCounter -= 1
    else:
        isInJump = False
        jumpCounter = 20


def draw_window():
    screen.blit(screen_background_image, (0, 0))
    for enemy in enemies:
        if screen_width >= enemy.x >= 0 - enemy_size:
            enemy.draw(screen)
        else:
            enemies.pop(enemies.index(enemy))

    hero.draw(screen, hero_location_x, hero_location_y)
    pygame.display.update()


def createEnemy():
    enemy = Enemy(screen_width, screen_height)
    enemies.append(enemy)


def check_if_hero_is_dead():
    global game_finished
    for enemy in enemies:
        print(hero_location_x)
        print(enemy.rect.centerx)
        print(hero_location_x + hero_width)
        print("")
        x_collision = hero_location_x <= enemy.rect.centerx <= (hero_location_x + hero_width)
        y_collision = hero_location_y + hero_height >= enemy.y
        if x_collision and y_collision:
            game_finished = True


while not game_finished:
    check_if_hero_is_dead()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_finished = True
        elif event.type == pygame.USEREVENT+1 and random.randint(0, 100) > 30:
            createEnemy()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and hero_location_x > moving_step:
        hero.update(HeroState.left)
        hero_location_x -= moving_step
    elif keys[pygame.K_RIGHT] and hero_location_x < screen_width - hero_width - moving_step:
        hero.update(HeroState.right)
        hero_location_x += moving_step

    if isInJump:
        hero.update(HeroState.jump)
        do_jump()
    elif keys[pygame.K_SPACE]:
        isInJump = True
    elif not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]:
        hero.update(HeroState.idle)

    draw_window()
    clock.tick(80)
