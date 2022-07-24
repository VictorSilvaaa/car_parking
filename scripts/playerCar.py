import pygame
from scripts.utils import *
import math
from time import sleep

RED_CAR = scale_image(pygame.image.load("img\sprites\carTeste2.png"), 1)

pygame.mixer.init()
car_sounds = pygame.mixer.Channel(1)
car_acelaration = pygame.mixer.Sound("sounds\Acelaration.wav")
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self, max_vel, rotation_vel, initPosition, angle):
        pygame.sprite.Sprite.__init__(self)
        self.img = RED_CAR
        self.mask = pygame.mask.from_surface(self.img)
        self.rect = self.img.get_rect()
        self.max_vel = max_vel
        self.moved = False
        self.acceleration = 0.1
        self.rotation_vel = rotation_vel
        self.rotated_image = self.img
        self.direction = ''
        self.vel = 0
        self.angle = angle
        self.initPosition = initPosition
        self.x, self.y = initPosition
        
    def rotate(self, left=False, right=False):
        if self.vel >0:
            if left:
                self.angle += self.rotation_vel
            else:
                self.angle -= self.rotation_vel
        elif self.vel<0:
            if left:
                self.angle -= self.rotation_vel
            else:
                self.angle += self.rotation_vel

    def move_to(self,direction):
        if direction == 'front':
            self.vel = min(self.vel + self.acceleration, self.max_vel)
        else:
            self.vel = max(self.vel - self.acceleration, -self.max_vel)
        self.newPosition()
    
    def controllerDirection(self):
        keys = pygame.key.get_pressed()
        self.moved = False
        if keys[pygame.K_a]:
            self.rotate(left=True)
        if keys[pygame.K_d]:
            self.rotate(right=True)
        if keys[pygame.K_w]:
            self.moved = True
            self.move_to('front')
        if keys[pygame.K_s]:
            self.moved = True
            self.move_to('back')
        if not self.moved:
            self.reduce_speed() 
            car_sounds.fadeout(100)
        
        if self.moved:
            if not car_sounds.get_busy():
                car_sounds.play(car_acelaration)
 
    def newPosition(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        if self.vel >= 0:
            self.vel = max(self.vel - self.acceleration*1.25, 0)
        else:
            self.vel = min(self.vel + self.acceleration*1.25, 0)
        self.newPosition()
    
    def draw(self, screen):
        self.rotated_image, self.rect = blit_rotate_center(self.img, (self.x, self.y), self.angle) 
        self.mask = pygame.mask.from_surface(self.rotated_image)
        screen.blit(self.rotated_image, self.rect.topleft)
    
    def resetCar(self):
        self.vel = 0
        self.angle = 0
        self.x, self.y = self.initPosition
    

