import pygame, random
from src.Dependency import *
from src.PowerUp import PowerUp
class Brick:
    def __init__(self, x, y):
        self.tier = 0
        self.color = 1
        self.x = x
        self.y = y
        self.width = 96
        self.height = 48
        self.alive = True
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def Hit(self, powerups):
        gSounds['brick-hit2'].play()

        if self.tier > 0:
            if self.color == 1:
                self.tier -= 1
                self.color = 5
            else:
                self.color -= 1
        else:
            if self.color == 1:
                self.alive = False
            else:
                self.color -= 1

        if not self.alive:
            gSounds['brick-hit1'].play()

            if random.random() < 0.8:
                powerup_type = random.randint(1, len(powerup_image_list))
                powerups.append(PowerUp(self.rect.x, self.rect.y, powerup_type))



    def update(self, dt):
        pass

    def render(self, screen):
        if self.alive:
            screen.blit(brick_image_list[((self.color-1)*4)+self.tier], (self.rect.x, self.rect.y))