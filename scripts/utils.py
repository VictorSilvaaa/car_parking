import pygame

def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)
    
def blit_rotate_center(image, top_left, angle):
    #rotaciona a imagem e conserva centralizada na mesma posição de referência
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    return rotated_image, new_rect