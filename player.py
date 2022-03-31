import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        self.pressedDown = False
        self.pressedUp = False

        pygame.draw.rect(self.image, color,  [0,0,width, height])

        self.rect = self.image.get_rect()
    
    def moveDown(self):
        if (self.rect.y > 400):
            self.rect.y = 400
        
        if (self.pressedUp == True):
            self.rect.y = self.rect.y

        else:
            self.rect.move_ip(0, 10)
    
    def moveUp(self):
        if (self.rect.y < 0):
            self.rect.y = 0
        else:
            self.rect.move_ip(0, -10)