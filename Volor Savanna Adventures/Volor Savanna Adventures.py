#2D Game
from pygame import mixer

import math
import pygame
import random
import sys

mixer.init()
mixer.music.load("Music/Four Brave Champions.mp3")
mixer.music.play(-1)

#draw screen
pygame.init()
screen_size = pygame.display.Info()
my_screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
my_screen.fill("yellow")

#global variables
tree_x = []
tree_y = []

def generate_terrain():
    #seed number is for development only
    #trees
    original_seed = 11182001
    seed_x = random.seed(original_seed)
    seed_x = random.random()
    seed_x = seed_x * 10
    seed_x = math.ceil(seed_x)
    mod_seed = "123"[::-1]
    mod_seed = int(mod_seed)
    seed_y = random.seed(mod_seed)
    seed_y = random.random()
    seed_y = seed_y * 10
    seed_y = math.ceil(seed_y)
    
    for i in range(0,math.ceil(screen_size.current_h / 5),50):
        tree_x.append(i * seed_x)
        tree_y.append(i * seed_y)
    
def one_player():
    generate_terrain()
    
    #inventory
    break_entity = False
    entity_list = []
    inventory = ["","","",""]
    inventory_1 = True
    inventory_2 = False
    inventory_3 = False
    inventory_4 = False
    place_entity = False

    #entity list
    log_total = [0,0,0,0]
    log_list_x = []
    log_list_y = []

    #misc
    load_game = False
    running = True

    #load images
    lion_image_1 = pygame.image.load("Images/The Mighty Lion 1.png")
    lion_image_1 = pygame.transform.scale(lion_image_1,(100, 100))
    tree_image = pygame.image.load("Images/tree.png")
    tree_image = pygame.transform.scale(tree_image,(100, 100))

    #player stats
    player_x = screen_size.current_w / 2
    player_y = screen_size.current_h / 2
    player_z = 0
    player_color = "cyan"
    player_health = 20
    player_health_total = "player 1: " + str(player_health)
    player_health_boolean = False

    my_font = pygame.font.SysFont("Timesnewroman", 50)

    clock = pygame.time.Clock()

    #temp
    inventory[0] = "log"
    inventory[1] = "log"
    inventory[2] = "log"
    inventory[3] = "log"

    while running:
        my_screen.fill("yellow")
        
        #render health
        player_health_font = my_font.render(player_health_total, True, (0,0,0))

        tick = clock.tick(1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #keyboard input
        keyboard = pygame.key.get_pressed()

        if keyboard[pygame.K_LEFT] and player_x > 0:
            player_x -= 10

        if keyboard[pygame.K_a] and player_x > 0:
            player_x -= 10

        if keyboard[pygame.K_RIGHT] and player_x < (screen_size.current_w):
            player_x += 10

        if keyboard[pygame.K_d] and player_x < (screen_size.current_w):
            player_x += 10

        if keyboard[pygame.K_UP] and player_y > 0:
            player_y -= 10

        if keyboard[pygame.K_w] and player_y > 0:
            player_y -= 10

        if keyboard[pygame.K_DOWN] and player_y < (screen_size.current_h - 400):
            player_y += 10

        if keyboard[pygame.K_s] and player_y < (screen_size.current_h - 400):
            player_y += 10

        if keyboard[pygame.K_1]:
            inventory_1 = True
            inventory_2 = False
            inventory_3 = False
            inventory_4 = False

        if keyboard[pygame.K_2]:
            inventory_1 = False
            inventory_2 = True
            inventory_3 = False
            inventory_4 = False

        if keyboard[pygame.K_3]:
            inventory_1 = False
            inventory_2 = False
            inventory_3 = True
            inventory_4 = False

        if keyboard[pygame.K_4]:
            inventory_1 = False
            inventory_2 = False
            inventory_3 = False
            inventory_4 = True

        if keyboard[pygame.K_TAB] and player_y < (screen_size.current_h):
            load_game = True

        if keyboard[pygame.K_q]:
            place_entity = True

        if keyboard[pygame.K_e]:
            break_entity = True

        #quit game
        if keyboard[pygame.K_ESCAPE]:
            running = False

        #title screen
        if keyboard[pygame.K_t]:
            title_screen()

        #reset game
        if keyboard[pygame.K_SPACE]:
            player_x = screen_size.current_w / 2
            player_y = screen_size.current_h / 2
            player_health = 20
            player_health_total = "player 1: " + str(player_health)

        #alive
        player_color = "cyan"
        player_health_boolean = True

        #hotbar

        #slot 1
        if inventory_1 == True:
            pygame.draw.rect(my_screen, "white", pygame.Rect(screen_size.current_w * (4/16), screen_size.current_h - 200, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "dark gray", pygame.Rect(screen_size.current_w * (6/16), screen_size.current_h - 200, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "light gray", pygame.Rect(screen_size.current_w * (8/16), screen_size.current_h - 200, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "dark gray", pygame.Rect(screen_size.current_w * (10/16), screen_size.current_h - 200, screen_size.current_w / 8, screen_size.current_h - 100))

        #slot 2
        if inventory_2 == True:
            pygame.draw.rect(my_screen, "light gray", pygame.Rect(screen_size.current_w * (4/16), screen_size.current_h - 200, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "white", pygame.Rect(screen_size.current_w * (6/16), screen_size.current_h - 200, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "light gray", pygame.Rect(screen_size.current_w * (8/16), screen_size.current_h - 200, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "dark gray", pygame.Rect(screen_size.current_w * (10/16), screen_size.current_h - 200, screen_size.current_w / 8, screen_size.current_h - 100))

        if inventory_3 == True:
            pygame.draw.rect(my_screen, "light gray", pygame.Rect(screen_size.current_w * (4/16), screen_size.current_h - 200, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "dark gray", pygame.Rect(screen_size.current_w * (6/16), screen_size.current_h - 200, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "white", pygame.Rect(screen_size.current_w * (8/16), screen_size.current_h - 200, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "dark gray", pygame.Rect(screen_size.current_w * (10/16), screen_size.current_h - 200, screen_size.current_w / 8, screen_size.current_h - 100))

        if inventory_4 == True:
            pygame.draw.rect(my_screen, "light gray", pygame.Rect(screen_size.current_w * (4/16), screen_size.current_h - 200, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "dark gray", pygame.Rect(screen_size.current_w * (6/16), screen_size.current_h - 200, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "light gray", pygame.Rect(screen_size.current_w * (8/16), screen_size.current_h - 200, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "white", pygame.Rect(screen_size.current_w * (10/16), screen_size.current_h - 200, screen_size.current_w / 8, screen_size.current_h - 100))

        #render player
        if player_health > 0:
            my_screen.blit(lion_image_1,(player_x, player_y))
            my_screen.blit(player_health_font, (100,(screen_size.current_h) - 100))
            
        #place entity
        if place_entity == True:
            place_entity = False
            exists = False

            if inventory_1 == True:
                if inventory[0] == "log" and int(log_total[0]) > 0:
                    for i in log_list_x:
                        if i == (int(math.ceil(player_x / 100.0)) * 100):
                            for i in log_list_y:
                                if i == (int(math.ceil(player_y / 100.0)) * 100):
                                    exists = True
                                    break
                        
                    if exists == False:
                        log_list_x.append(int(math.ceil(player_x / 100.0)) * 100)
                        log_list_y.append(int(math.ceil(player_y / 100.0)) * 100)
                        log_total[0] = int(log_total[0]) - 1
                    
            if inventory_2 == True:
                if inventory[1] == "log" and int(log_total[1]) > 0:
                    for i in log_list_x:
                        if i == (int(math.ceil(player_x / 100.0)) * 100):
                            for i in log_list_y:
                                if i == (int(math.ceil(player_y / 100.0)) * 100):
                                    exists = True
                                    break
                        
                    if exists == False:
                        log_list_x.append(int(math.ceil(player_x / 100.0)) * 100)
                        log_list_y.append(int(math.ceil(player_y / 100.0)) * 100)
                        log_total[1] = int(log_total[1]) - 1

            if inventory_3 == True:
                if inventory[2] == "log" and int(log_total[2]) > 0:
                    for i in log_list_x:
                        if i == (int(math.ceil(player_x / 100.0)) * 100):
                            for i in log_list_y:
                                if i == (int(math.ceil(player_y / 100.0)) * 100):
                                    exists = True
                                    break
                        
                    if exists == False:
                        log_list_x.append(int(math.ceil(player_x / 100.0)) * 100)
                        log_list_y.append(int(math.ceil(player_y / 100.0)) * 100)
                        log_total[2] = int(log_total[2]) - 1

            if inventory_4 == True:
                if inventory[3] == "log" and int(log_total[3]) > 0:
                    for i in log_list_x:
                        if i == (int(math.ceil(player_x / 100.0)) * 100):
                            for i in log_list_y:
                                if i == (int(math.ceil(player_y / 100.0)) * 100):
                                    exists = True
                                    break
                        
                    if exists == False:
                        log_list_x.append(int(math.ceil(player_x / 100.0)) * 100)
                        log_list_y.append(int(math.ceil(player_y / 100.0)) * 100)
                        log_total[3] = int(log_total[3]) - 1
                
        #break entity
        if break_entity == True:
            break_entity = False

            #log
            for i in range(len(log_list_x)):
                if i < len(log_list_x):
                    if player_x <= log_list_x[i] + 50 and player_x >= log_list_x[i] - 50:
                        if player_y <= log_list_y[i] + 50 and player_y >= log_list_y[i] - 50:
                            log_list_x.pop(i)
                            log_list_y.pop(i)

                            if inventory_1 == True:
                                log_total[0] = int(log_total[0]) + 1
                                
                            if inventory_2 == True:
                                log_total[1] = int(log_total[1]) + 1

                            if inventory_3 == True:
                                log_total[2] = int(log_total[2]) + 1

                            if inventory_4 == True:
                                log_total[3] = int(log_total[3]) + 1

            #terrain
            for i in range(len(tree_x)):
                if i < len(tree_x):
                    if player_x <= tree_x[i] + 50 and player_x >= tree_x[i] - 50:
                        if player_y <= tree_y[i] + 50 and player_y >= tree_y[i] - 50:
                            tree_x.pop(i)
                            tree_y.pop(i)

                            if inventory_1 == True:
                                log_total[0] = int(log_total[0]) + 1
                                
                            if inventory_2 == True:
                                log_total[1] = int(log_total[0]) + 1

                            if inventory_3 == True:
                                log_total[2] = int(log_total[0]) + 1

                            if inventory_4 == True:
                                log_total[3] = int(log_total[0]) + 1
                            
        #render entities
        if load_game == False:
            for i in range(len(log_list_x)):
                if i < len(log_list_x):
                    my_screen.blit(tree_image,(log_list_x[i], log_list_y[i]))

        #render terrain
        if load_game == False:
            for i in range(len(tree_x)):
                my_screen.blit(tree_image,(tree_x[i], tree_y[i]))

        if load_game == True:
            load_game = False

        pygame.display.flip()

    pygame.quit()

def title_screen():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #keyboard input
        keyboard = pygame.key.get_pressed()

        if keyboard[pygame.K_1]:
            one_player()

        if keyboard[pygame.K_2]:
            two_player()

        if keyboard[pygame.K_3]:
            multiplayer()

        #quit game
        if keyboard[pygame.K_ESCAPE]:
            running = False

        #draw fonts
        title_font = pygame.font.SysFont("Timesnewroman", 100)
        sub_font = pygame.font.SysFont("Timesnewroman", 50)

        title = title_font.render("Welcome to Volor Savanna!",True, ("black"))
        one = sub_font.render("1 = start",True, (0,0,0))
        reset = sub_font.render("space bar = reset game (dev build)",True, (0,0,0))
        escape = sub_font.render("escape = quit",True, (0,0,0))
        my_help = sub_font.render("t = title screen",True, (0,0,0))
        load = sub_font.render("tab = save game",True,(0,0,0))
        break_block = sub_font.render("e = break block",True,(0,0,0))
        place_block = sub_font.render("q = place block",True,(0,0,0))
        hotbar = sub_font.render("1-4 = hotbar",True,(0,0,0))

        my_screen.blit(title, (100,50))
        my_screen.blit(one, (100, 200))
        my_screen.blit(reset, (100, 250))
        my_screen.blit(escape, (100, 300))
        my_screen.blit(my_help, (100, 350))
        my_screen.blit(load, (100, 400))
        my_screen.blit(break_block, (100, 450))
        my_screen.blit(place_block, (100, 500))
        my_screen.blit(hotbar, (100, 550))

        pygame.display.flip()

    pygame.quit()

title_screen()
