import pygame
from hero import Hero
from hero import HeroState
import random
from enemy import Enemy
from enemy import enemy_size
from text import TextObject

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen_background_image = pygame.image.load("images/game_bg.jpg")

pygame.time.set_timer(pygame.USEREVENT + 1, 700)
clock = pygame.time.Clock()
game_finished = False
game_paused = False

moving_step = 10

hero_height = 150
hero_width = 150

hero_location_x = screen_width / 2
hero_location_y = screen_height - hero_height

isInJump = False
jump_counter = 20
hero = Hero(hero_height, hero_width)

enemies = []


def do_jump():
    global isInJump, jump_counter, hero_location_y
    if jump_counter >= -20:
        if jump_counter < 0:
            hero_location_y += (jump_counter ** 2) / 9
        else:
            hero_location_y -= (jump_counter ** 2) / 9
        jump_counter -= 1
    else:
        isInJump = False
        jump_counter = 20


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
    global game_paused
    for enemy in enemies:
        x_collision = hero_location_x <= enemy.rect.centerx <= (hero_location_x + hero_width)
        y_collision = hero_location_y + hero_height >= enemy.y
        if x_collision and y_collision:
            game_paused = True


def main_game_flow():
    global game_finished, isInJump, hero_location_x
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_finished = True
        elif event.type == pygame.USEREVENT + 1 and random.randint(0, 100) > 30:
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


def show_pause_state():
    global game_paused, game_finished, enemies, hero_location_x, hero_location_y, jump_counter
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_finished = True
        elif event.type == pygame.KEYDOWN:
            enemies = []
            pygame.event.clear(pygame.KEYDOWN)
            pygame.event.clear(pygame.K_SPACE)
            hero_location_x = screen_width / 2
            hero_location_y = screen_height - hero_height
            jump_counter = 20
            game_paused = False

    text = TextObject(screen_width / 2, screen_height / 2, lambda: f'GAME OVER! :( Press any key to try again')
    text.draw(screen, True)
    pygame.display.update()


# MAIN LOOP
while not game_finished:
    if game_paused:
        show_pause_state()
    else:
        check_if_hero_is_dead()
        main_game_flow()
    clock.tick(80)
