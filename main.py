import pygame, sys
from scripts.button import *
from scripts.game import *
pygame.init()

screenSize = screenWidth , screeHeight = (1080, 720)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Main Menu")
time = pygame.time.Clock()

#img buttons
start_img = pygame.image.load('img\start.png')
levels_img = pygame.image.load('img\levels.png')
quit_img = pygame.image.load('img\quit.png')
logo_img = pygame.image.load('img\logo.png')
l1_img = pygame.image.load('img/1.png')
l2_img = pygame.image.load('img/2.png')
l3_img = pygame.image.load('img/3.png')
back_img = pygame.image.load('img/back.png')

#instance buttons
start_button = Button(438,237, start_img,1)
levels_button = Button(438,307, levels_img ,1)
quit_button = Button(438,377, quit_img ,1)
back_button = Button(438,588, back_img ,1)
l1_button = Button(102,95,l1_img,1)
l2_button = Button(202,95,l2_img,1)
l3_button = Button(302,95,l3_img,1)

#background music menu
pygame.mixer.music.set_volume(1)
soundMenuBackground = pygame.mixer.music.load('sounds\\fundomenuu.wav')
pygame.mixer.music.play(-1)

state = 'menu'
level = 1
run = True
while run:
    time.tick(30)
    screen.fill((52,78,91))
    if state == 'menu':
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed()[0]:
                if start_button.clicked():
                    pygame.mixer.music.stop()
                    game(level)
                elif levels_button.clicked():
                    state = 'levels'
                elif quit_button.clicked():
                    run = False
        screen.blit(logo_img, (243,96))
        start_button.draw(screen)
        levels_button.draw(screen)
        quit_button.draw(screen)
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed()[0]:
                if l1_button.clicked():
                    pygame.mixer.music.stop()
                    result = game(1)
                    if result:
                        level = 2
                    state = 'menu'
                elif l2_button.clicked() and level>=1:
                    pygame.mixer.music.stop()
                    result = game(2)
                elif l3_button.clicked():
                    print('level3')
                elif back_button.clicked():
                    state = 'menu'
        back_button.draw(screen)
        l1_button.draw(screen)
        l2_button.draw(screen)
        l3_button.draw(screen)
    
    
    pygame.display.update()