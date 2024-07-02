import pygame
import time
import sys
from pygame.locals import *

pygame.init()

screen_width = 480
screen_height = 600

gutter = 20

scoore_height = 90
mole_width = (screen_width-gutter*4)/3
mole_height = (screen_height-scoore_height-gutter*3)/3


class Mole():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(surface, color, pygame.Rect(
            self.x, self.y, mole_width, mole_height))


moles = [
    Mole(gutter, scoore_height),
    Mole(mole_width + gutter*2, scoore_height),
    Mole(mole_width*2 + gutter*3, scoore_height),

    Mole(gutter, scoore_height + mole_height + gutter),
    Mole(mole_width + gutter*2, scoore_height + mole_height + gutter),
    Mole(mole_width * 2 + gutter*3, scoore_height + mole_height + gutter),

    Mole(gutter, scoore_height + mole_height * 2 + gutter * 2),
    Mole(mole_width + gutter*2, scoore_height + mole_height * 2 + gutter * 2),
    Mole(mole_width * 2 + gutter*3, scoore_height + mole_height * 2 + gutter * 2),
]


def draw_moles():
    for mole in moles:
        mole.draw()


surface = pygame.display.set_mode((screen_width, screen_height))

color = (200, 0, 0)

# rec1 = pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))


def game():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == MOUSEBUTTONDOWN:
                print(event)
                (x, y) = pygame.mouse.get_pos()
                print(x, y)

        draw_moles()

        pygame.display.flip()


game()
