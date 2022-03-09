#2D Game
from pygame import mixer

import pygame
import random
import time

mixer.init()
mixer.music.load("Music/Four Brave Champions.mp3")
mixer.music.play()

pygame.init()
screen_size = pygame.display.Info()
my_screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
running = True

lion_image_1 = pygame.image.load("Images/The Mighty Lion 1.png")
lion_image_1 = pygame.transform.scale(lion_image_1,(screen_size.current_h / 10, screen_size.current_h / 10))

lion_image_2 = pygame.image.load("Images/The Mighty Lion 2.png")
lion_image_2 = pygame.transform.scale(lion_image_2,(screen_size.current_h / 10, screen_size.current_h / 10))

lion_image_3 = pygame.image.load("Images/The Mighty Lion 3.png")
lion_image_3 = pygame.transform.scale(lion_image_3,(screen_size.current_h / 10, screen_size.current_h / 10))

lion_image_4 = pygame.image.load("Images/The Mighty Lion 4.png")
lion_image_4 = pygame.transform.scale(lion_image_4,(screen_size.current_h / 10, screen_size.current_h / 10))

player_x = 200
player_y = 200
player_z = 0
player_color = "cyan"
player_health = 3
player_health_total = "player 1: " + str(player_health)
player_health_boolean = False

player_2_x = 500
player_2_y = 200
player_2_z = 0
player_color_2 = "pink"
player_2_health = 3
player_2_health_total = "player 2: " + str(player_health)
player_2_health_boolean = False

ai_1_x = 200
ai_1_y = 200

ai_2_x = 500
ai_2_y = 200

ai_3_x = 200
ai_3_y = 200

ai_4_x = 500
ai_4_y = 200

my_font = pygame.font.SysFont("Timesnewroman", 50)

clock = pygame.time.Clock()

while running:
    rand = random.randint(1,2)
    player_health_font = my_font.render(player_health_total, True, (0,0,0))
    player_2_health_font = my_font.render(player_2_health_total, True, (0,0,0))
    
    tick = clock.tick(60)
    #print(tick)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #keyboard input
    keyboard = pygame.key.get_pressed()

    if keyboard[pygame.K_LEFT] and player_2_x > 0:
        player_2_x -= 12

    if keyboard[pygame.K_a] and player_x > 0:
        player_x -= 12

    if keyboard[pygame.K_RIGHT] and player_2_x < (screen_size.current_w):
        player_2_x += 12

    if keyboard[pygame.K_d] and player_x < (screen_size.current_w):
        player_x += 12

    if keyboard[pygame.K_UP] and player_2_y > 0:
        player_2_y -= 12

    if keyboard[pygame.K_w] and player_y > 0:
        player_y -= 12

    if keyboard[pygame.K_DOWN] and player_2_y < (screen_size.current_h):
        player_2_y += 12

    if keyboard[pygame.K_s] and player_y < (screen_size.current_h):
        player_y += 12

    #quit game
    if keyboard[pygame.K_ESCAPE]:
        running = False

    #reset game
    if keyboard[pygame.K_SPACE]:
        player_x = 200
        player_y = 200

        player_2_x = 500
        player_2_y = 200

        ai_1_x = 200
        ai_1_y = 200

        ai_2_x = 500
        ai_2_y = 200

        ai_3_x = 200
        ai_3_y = 200

        ai_4_x = 500
        ai_4_y = 200

        
        
        player_health = 3
        player_2_health = 3
        player_health_total = "player 1: " + str(player_health)
        player_2_health_total = "player 2: " + str(player_2_health)

    #AI
    player_z = player_x + player_y
    player_2_z = player_2_x + player_2_y

    #AI 1
    if player_z < player_2_z:
        if ai_1_x < player_x:
            ai_1_x += 2

        if ai_1_x > player_x:
            ai_1_x -= 2

        if ai_1_y < player_y:
            ai_1_y += 2

        if ai_1_y > player_y:
            ai_1_y -= 2

    if player_z > player_2_z:
        if ai_1_x < player_2_x:
            ai_1_x += 2

        if ai_1_x > player_2_x:
            ai_1_x -= 2

        if ai_1_y < player_2_y:
            ai_1_y += 2

        if ai_1_y > player_2_y:
            ai_1_y -= 2

    #AI 2
    if player_z > player_2_z:
        if ai_2_x < player_x:
            ai_2_x += 3

        if ai_2_x > player_x:
            ai_2_x -= 3

        if ai_2_y < player_y:
            ai_2_y += 3

        if ai_2_y > player_y:
            ai_2_y -= 3

    if player_z < player_2_z:
        if ai_2_x < player_2_x:
            ai_2_x += 3

        if ai_2_x > player_2_x:
            ai_2_x -= 3

        if ai_2_y < player_2_y:
            ai_2_y += 3

        if ai_2_y > player_2_y:
            ai_2_y -= 3

    #AI 3
    if player_z < player_2_z:
        if ai_3_x < player_x:
            ai_3_x += 4

        if ai_3_x > player_x:
            ai_3_x -= 4

        if ai_3_y < player_y:
            ai_3_y += 4

        if ai_3_y > player_y:
            ai_3_y -= 4

    if player_z > player_2_z:
        if ai_3_x < player_2_x:
            ai_3_x += 4

        if ai_3_x > player_2_x:
            ai_3_x -= 4

        if ai_3_y < player_2_y:
            ai_3_y += 4

        if ai_3_y > player_2_y:
            ai_3_y -= 4

    #AI 4
    if player_z > player_2_z:
        if ai_4_x < player_x:
            ai_4_x += 6

        if ai_4_x > player_x:
            ai_4_x -= 6

        if ai_4_y < player_y:
            ai_4_y += 6

        if ai_4_y > player_y:
            ai_4_y -= 6

    if player_z < player_2_z:
        if ai_4_x < player_2_x:
            ai_4_x += 6

        if ai_4_x > player_2_x:
            ai_4_x -= 6

        if ai_4_y < player_2_y:
            ai_4_y += 6

        if ai_2_y > player_2_y:
            ai_4_y -= 6

    #collision detection
            
    #AI 1
    if ai_1_x == player_x and ai_1_y == player_y:
        player_color = "red"

        if player_health_boolean == True:
            player_health -= 1
            player_health_total = "player 1: " + str(player_health)
            player_health_boolean = False
            
    if ai_1_x == player_2_x and ai_1_y == player_2_y:
        player_color_2 = "red"

        if player_2_health_boolean == True:
            player_2_health -= 1
            player_2_health_total = "player 2: " + str(player_2_health)
            player_2_health_boolean = False
            
    #AI 2
    if ai_2_x == player_x and ai_2_y == player_y:
        player_color = "red"

        if player_health_boolean == True:
            player_health -= 1
            player_health_total = "player 1: " + str(player_health)
            player_health_boolean = False

    if ai_2_x == player_2_x and ai_2_y == player_2_y:
        player_color_2 = "red"

        if player_2_health_boolean == True:
            player_2_health -= 1
            player_2_health_total = "player 2: " + str(player_2_health)
            player_2_health_boolean = False
    #AI 3
    if ai_3_x == player_x and ai_3_y == player_y:
        player_color = "red"

        if player_health_boolean == True:
            player_health -= 1
            player_health_total = "player 1: " + str(player_2_health)
            player_health_boolean = False

    if ai_3_x == player_2_x and ai_3_y == player_2_y:
        player_color_2 = "red"

        if player_2_health_boolean == True:
            player_2_health -= 1
            player_2_health_total = "player 2: " + str(player_2_health)
            player_2_health_boolean = False

    #AI 4
    if ai_4_x == player_x and ai_4_y == player_y:
        player_color = "red"

        if player_health_boolean == True:
            player_health -= 1
            player_health_total = "player 1: " + str(player_2_health)
            player_health_boolean = False

    if ai_4_x == player_2_x and ai_4_y == player_2_y:
        player_color_2 = "red"

        if player_2_health_boolean == True:
            player_2_health -= 1
            player_2_health_total = "player 2: " + str(player_2_health)
            player_2_health_boolean = False

    #alive
    if (ai_1_x != player_x and ai_1_y != player_y) and (ai_2_x != player_x and ai_2_y != player_y) and (ai_3_x != player_x and ai_3_y != player_y) and (ai_4_x != player_x and ai_4_y != player_y):
        player_color = "cyan"
        player_health_boolean = True

    if (ai_1_x != player_2_x and ai_1_y != player_2_y) and (ai_2_x != player_2_x and ai_2_y != player_2_y) and (ai_3_x != player_x and ai_3_y != player_2_y) and (ai_4_x != player_x and ai_4_y != player_2_y):
        player_color_2 = "pink"
        player_2_health_boolean = True
        
    #draw screen
    my_screen.fill((0, 225, 0))

    if player_health > 0:
        pygame.draw.circle(my_screen, (player_color), (player_x, player_y), 100)
        my_screen.blit(player_health_font, (100,(screen_size.current_h) - 200))

    if player_2_health > 0:
        pygame.draw.circle(my_screen, (player_color_2), (player_2_x, player_2_y), 100)
        my_screen.blit(player_2_health_font, (100,(screen_size.current_h) - 100))
    
    my_screen.blit(lion_image_1,(ai_1_x, ai_1_y))
    my_screen.blit(lion_image_2,(ai_2_x, ai_2_y))
    my_screen.blit(lion_image_3,(ai_3_x, ai_3_y))
    my_screen.blit(lion_image_4,(ai_4_x, ai_4_y))
    
    pygame.display.flip()

pygame.quit()
