import pygame
from random import randint

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        pygame.draw.ellipse(self.image, color, [0,0,width, height])

        self.rect = self.image.get_rect()

        self.velocity = [randint(4, 8), randint(-8, 8)]
    
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]