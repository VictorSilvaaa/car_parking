import pygame

#button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        #draw button on screen
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            pygame.draw.rect(screen, (0,200,0), (self.rect.x-2,self.rect.y-4,self.rect.width+4,self.rect.height), 2)
        screen.blit(self.image, (self.rect.x, self.rect.y))
		
    def clicked(self):
        flag = False
        pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            flag = True
        return flag
			
				
			
			
