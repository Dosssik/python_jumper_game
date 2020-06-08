import pygame as pg
from enum import Enum
import random


class MovingDirection(Enum):
    right = 0
    left = 1


enemy_size = 100

left_to_right_sprites = [
    pg.transform.scale(pg.image.load('images/enemy/Hurt (1).png'), (enemy_size, enemy_size)),
    pg.transform.scale(pg.image.load('images/enemy/Hurt (2).png'), (enemy_size, enemy_size)),
    pg.transform.scale(pg.image.load('images/enemy/Hurt (3).png'), (enemy_size, enemy_size)),
    pg.transform.scale(pg.image.load('images/enemy/Hurt (4).png'), (enemy_size, enemy_size)),
    pg.transform.scale(pg.image.load('images/enemy/Hurt (5).png'), (enemy_size, enemy_size)),
    pg.transform.scale(pg.image.load('images/enemy/Hurt (6).png'), (enemy_size, enemy_size)),
    pg.transform.scale(pg.image.load('images/enemy/Hurt (7).png'), (enemy_size, enemy_size))
]
right_to_left_sprites = [
    pg.transform.flip(pg.transform.scale(pg.image.load('images/enemy/Hurt (1).png'), (enemy_size, enemy_size)), True, False),
    pg.transform.flip(pg.transform.scale(pg.image.load('images/enemy/Hurt (2).png'), (enemy_size, enemy_size)), True, False),
    pg.transform.flip(pg.transform.scale(pg.image.load('images/enemy/Hurt (3).png'), (enemy_size, enemy_size)), True, False),
    pg.transform.flip(pg.transform.scale(pg.image.load('images/enemy/Hurt (4).png'), (enemy_size, enemy_size)), True, False),
    pg.transform.flip(pg.transform.scale(pg.image.load('images/enemy/Hurt (5).png'), (enemy_size, enemy_size)), True, False),
    pg.transform.flip(pg.transform.scale(pg.image.load('images/enemy/Hurt (6).png'), (enemy_size, enemy_size)), True, False),
    pg.transform.flip(pg.transform.scale(pg.image.load('images/enemy/Hurt (7).png'), (enemy_size, enemy_size)), True, False)
]


class Enemy:
    def __init__(self, screen_width, screen_height):
        if random.randint(0, 1) == 0:
            self.direction = MovingDirection.left
            self.x = screen_width
            self.sprites = right_to_left_sprites
        else:
            self.direction = MovingDirection.right
            self.x = 0
            self.sprites = left_to_right_sprites
        self.velocity = random.randint(2, 5)
        self.y = screen_height - enemy_size
        self.animation_index = 0
        self.rect = pg.transform.scale(pg.image.load('images/enemy/Hurt (1).png'), (enemy_size, enemy_size)).get_rect(x=self.x, y=self.y)

    def draw(self, window):
        if self.animation_index + 1 > 36:
            self.animation_index = 0
        else:
            self.animation_index += 1
        index_ = self.animation_index // 6

        if self.direction == MovingDirection.left:
            self.x -= self.velocity
        else:
            self.x += self.velocity

        if self.direction == MovingDirection.left:
            self.x -= self.velocity
        else:
            self.x += self.velocity
        image = self.sprites[index_]
        self.rect = image.get_rect(x=self.x, y=self.y)
        window.blit(image, (self.x, self.y))
