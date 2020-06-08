from enum import Enum
import pygame as pg


class HeroState(Enum):
    idle = 0
    left = 1
    right = 2
    jump = 3


class Hero:
    def __init__(self, height, width):
        self.state = HeroState.idle
        self.right_image_array = [
            pg.transform.scale(pg.image.load('images/Run (1).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Run (2).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Run (3).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Run (4).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Run (5).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Run (6).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Run (7).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Run (8).png'), (height, width))
        ]
        self.left_image_array = [
            pg.transform.flip(pg.transform.scale(pg.image.load('images/Run (1).png'), (height, width)), True, False),
            pg.transform.flip(pg.transform.scale(pg.image.load('images/Run (2).png'), (height, width)), True, False),
            pg.transform.flip(pg.transform.scale(pg.image.load('images/Run (3).png'), (height, width)), True, False),
            pg.transform.flip(pg.transform.scale(pg.image.load('images/Run (4).png'), (height, width)), True, False),
            pg.transform.flip(pg.transform.scale(pg.image.load('images/Run (5).png'), (height, width)), True, False),
            pg.transform.flip(pg.transform.scale(pg.image.load('images/Run (6).png'), (height, width)), True, False),
            pg.transform.flip(pg.transform.scale(pg.image.load('images/Run (7).png'), (height, width)), True, False),
            pg.transform.flip(pg.transform.scale(pg.image.load('images/Run (8).png'), (height, width)), True, False)
        ]
        self.idle_image_array = [
            pg.transform.scale(pg.image.load('images/Idle (1).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Idle (2).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Idle (3).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Idle (4).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Idle (5).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Idle (6).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Idle (7).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Idle (8).png'), (height, width))
        ]
        self.jump_image_array = [
            pg.transform.scale(pg.image.load('images/Slide (1).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Slide (2).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Slide (3).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Slide (4).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Slide (5).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Slide (6).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Slide (7).png'), (height, width)),
            pg.transform.scale(pg.image.load('images/Slide (8).png'), (height, width))
        ]
        self.animation_index = 0

    def update(self, state):
        self.state = state
        if self.animation_index + 1 > 49:
            self.animation_index = 0
        else:
            self.animation_index += 1

    def draw(self, window, x, y):
        index_ = self.animation_index // 7
        if self.state == HeroState.right:
            window.blit(self.right_image_array[index_], (x, y))
        elif self.state == HeroState.left:
            window.blit(self.left_image_array[index_], (x, y))
        elif self.state == HeroState.idle:
            window.blit(self.idle_image_array[index_], (x, y))
        elif self.state == HeroState.jump:
            window.blit(self.jump_image_array[index_], (x, y))

