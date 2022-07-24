from scripts.utils import*
import pygame 

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x,y,image,angle=0):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = blit_rotate_center(image, (x,y), angle)
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y
        self.life = 3
        
        