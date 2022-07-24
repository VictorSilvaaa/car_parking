import pygame, sys
import math
from time import sleep, process_time, time
from scripts.playerCar import *
from scripts.button import *
from scripts.obstacle import*



car_start = pygame.mixer.Sound('sounds\Car_start.wav')
def level1():
    pygame.init()
    car_start.play(0)
    
    #settings for window
    sizeScreen = widthScreen, heightScreen = 1080,720
    screen = pygame.display.set_mode(sizeScreen)
    pygame.display.set_caption('Parking Car')
    clock = pygame.time.Clock()

    #variables for graphics
    PISTA = scale_image(pygame.image.load("img\pista\pista1.png"), 1)
    PISTA_BORDER = scale_image(pygame.image.load("img\pista\pista_border.png"), 1)
    PISTA_BORDER_MASK = pygame.mask.from_surface(PISTA_BORDER)
    PARKING_POINT = pygame.Rect(838,239,112,54) 

    #obstacles img
    car_black = pygame.image.load('img\sprites\car_black.png')
    car_red = pygame.image.load('img\sprites\car_red.png')
    car_yellow = pygame.image.load('img\sprites\car_yellow.png')
    car_yellow2 = pygame.image.load('img\sprites\car_yellow2.png')
    car_green = pygame.image.load('img\sprites\car_green.png')
    cone_img = pygame.image.load('img\pista\cone.png')
    stone_img = pygame.image.load('img\pista\pedra.png')

    #instace obstacles cars 
    car1 = Obstacle(681.75, 169.59, car_yellow, -90)
    car2 = Obstacle(700.5, 230.5, car_green, -90)
    car3 = Obstacle(703, 294, car_yellow2, -90)
    car4 = Obstacle(701, 362, car_green, -90)
    car5 = Obstacle(870.5, 174.5, car_green, -90)
    car6 = Obstacle(874, 296, car_red, -90)
    car7 = Obstacle(873, 360.5, car_black, -90)
    #sprite group carsObstacles 
    carsObstacles = pygame.sprite.Group()
    carsObstacles.add(car1, car2, car3, car4, car5, car6 , car7)

    #instace obstacles generals
    cone1 = Obstacle(103, 482, cone_img)
    cone2 = Obstacle(58.5, 337, cone_img)
    cone3 = Obstacle(130, 213, cone_img)
    cone4 = Obstacle(485.5, 358.5, cone_img)
    stone1  =  Obstacle(378, 355, stone_img)
    #sprite group obstacles generals
    obstaclesGenerals = pygame.sprite.Group()
    obstaclesGenerals.add(cone1, cone2, cone3, cone4, stone1)
    #sprite group of all obstacles
    obstaclesAll = pygame.sprite.Group()
    obstaclesAll.add(carsObstacles, obstaclesGenerals)


    #pause buttons/img
    pause_img = pygame.image.load('img/pause.png')
    play_img = pygame.image.load('img/play.png')
    break_img = pygame.image.load('img/break.png')
    screen_pause = pygame.image.load('img\screen_pause.png')

    pause_button = Button(963,15, pause_img,1)
    play_button = Button(963,15, play_img,1)
    break_button = Button(1002,15, break_img, 1)

    #victory
    win_img = pygame.image.load('img\screen_win.png')
    continue_img = pygame.image.load('img\continue.png')
    menu_img =  pygame.image.load('img\menu.png')
    continue_button = Button(321, 588, continue_img,1)
    menu_button = Button(549, 588, menu_img,1)

    #text
    font = pygame.font.SysFont('arial',40, True,True)
    
       

    #player car instance
    carro = PlayerCar(3,3,(73, 635),0)

    result = False
    state = 'run'
    run = True
    time = 0
    while run:
        clock.tick(60)
        if state == 'run':
            screen.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if pygame.mouse.get_pressed()[0]:
                    if pause_button.clicked():
                        state= 'pause'
                    if break_button.clicked():
                        run = False

            if pygame.sprite.spritecollide(carro, obstaclesAll, False, pygame.sprite.collide_mask) or \
               PISTA_BORDER_MASK.overlap(carro.mask, (carro.rect.x, carro.rect.y)):
                carro.resetCar()
            
            if PARKING_POINT.contains(carro.rect):
                result = True
                state = 'victory'
        
            carro.controllerDirection()
            screen.blit(PISTA, (0,0))
            carro.draw(screen)
            obstaclesAll.draw(screen)
            pause_button.draw(screen)
            break_button.draw(screen)

            #time controller
            time += clock.get_time()
            time_formated = font.render(f'{60-(time//1000)}', True, (255,0,0))
            screen.blit(time_formated, (0,0))
            if time//1000 >= 60:
                carro.resetCar()
                time =0
        elif state == 'pause':
            screen.blit(screen_pause, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if pygame.mouse.get_pressed()[0]:
                    if play_button.clicked():
                        state= 'run'
                    if break_button.clicked():
                        run = False
            play_button.draw(screen)
            break_button.draw(screen)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if pygame.mouse.get_pressed()[0]:
                    if menu_button.clicked():
                        run = False
            screen.blit(win_img,(0,0))
            continue_button.draw(screen)
            menu_button.draw(screen)
        
        pygame.display.update()
    return result

if __name__ == "__main__":
  level1()
