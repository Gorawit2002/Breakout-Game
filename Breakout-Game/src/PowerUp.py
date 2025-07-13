import pygame
from src.constants import *
from src.Dependency import *
from src.resources import powerup_image_list

class PowerUp:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.type = type
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.dy = 150
        self.alive = True
        self.image = powerup_image_list[self.type - 1]

    def update(self, dt):
        self.rect.y += self.dy * dt
        if self.rect.y > HEIGHT:
            self.alive = False

    def render(self, screen):
        if self.alive:
            screen.blit(self.image, (self.rect.x, self.rect.y))