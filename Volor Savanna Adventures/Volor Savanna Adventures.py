#2D Game
from pygame import *

import math
import numpy as np
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
tree_x = np.array([])
tree_y = np.array([])

def generate_terrain():
    #global
    global tree_x
    global tree_y
    
    #seed number is for development only
    #trees
    original_seed = "1234"
    seed_x = random.seed(original_seed)
    seed_x = random.random()
    seed_x = seed_x * 10
    seed_x = math.ceil(seed_x)
    mod_seed = original_seed[::-1]
    mod_seed = int(mod_seed)
    seed_y = random.seed(mod_seed)
    seed_y = random.random()
    seed_y = seed_y * 10
    seed_y = math.ceil(seed_y)
    
    for i in range(0,math.ceil(screen_size.current_h / 5),50):
        tree_x = np.append(tree_x, i * seed_x)
        tree_y = np.append(tree_y, i * seed_y)
    
def one_player():
    generate_terrain()

    #entity list
    log_list_x = np.array([])
    log_list_y = np.array([])
    log_total = [0,0,0,0]

    plank_list_x = np.array([])
    plank_list_y = np.array([])
    plank_total = [0,0,0,0]

    sapling_list_x = np.array([])
    sapling_list_y = np.array([])
    sapling_total = [0,0,0,0]

    #fonts
    item_total_font = pygame.font.SysFont("Timesnewroman", 50)
    my_font = pygame.font.SysFont("Timesnewroman", 50)
    fps = pygame.font.SysFont("Timesnewroman", 100)

    #global
    global tree_x
    global tree_y

    #inventory
    break_entity = False
    entity_list = []
    inventory = ["","","",""]
    inventory_1 = True
    inventory_2 = False
    inventory_3 = False
    inventory_4 = False
    place_entity = False

    #load image entities
    axolotl_image = pygame.image.load("Images/axolotl.png")
    axolotl_image = pygame.transform.scale(axolotl_image,(100, 100))

    lion_image_1 = pygame.image.load("Images/The Mighty Lion 1.png")
    lion_image_1 = pygame.transform.scale(lion_image_1,(100, 100))

    log_image = pygame.image.load("Images/log.png")
    log_image = pygame.transform.scale(log_image,(100, 100))

    plank_image = pygame.image.load("Images/plank.png")
    plank_image = pygame.transform.scale(plank_image,(100, 100))

    sapling_image = pygame.image.load("Images/sapling.png")
    sapling_image = pygame.transform.scale(sapling_image,(100, 100))

    tree_image = pygame.image.load("Images/tree.png")
    tree_image = pygame.transform.scale(tree_image,(100, 100))

    #load image inventory
    log_image_inventory = pygame.image.load("Images/log.png")
    log_image_inventory = pygame.transform.scale(log_image_inventory,(50, 50))

    plank_image_inventory = pygame.image.load("Images/plank.png")
    plank_image_inventory = pygame.transform.scale(plank_image_inventory,(50, 50))

    sapling_image_inventory = pygame.image.load("Images/sapling.png")
    sapling_image_inventory = pygame.transform.scale(sapling_image_inventory,(50, 50))

    #misc
    cancel_action = False
    cancel_action_boi = False
    cancel_action_down = False
    cancel_action_up = False
    clock = pygame.time.Clock()
    crafting = False
    crafting_confirm = False
    load_game = False
    running = True

    #pet
    pet_x = 0
    pet_y = 0

    #player stats
    player_x = screen_size.current_w / 2
    player_y = screen_size.current_h / 2
    player_health = 20
    player_health_total = "health: " + str(player_health)
    player_health_boolean = False

    #terrain lists
    sapling_x = []
    sapling_y = []

    while running:
        my_screen.fill("yellow")
        
        #render health
        player_health_font = my_font.render(player_health_total, True, (0,0,0))

        tick = clock.tick(1000000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                cancel_action_down = True
                cancel_action_up = False

            if event.type == pygame.KEYUP:
                cancel_action_down = False
                cancel_action_up = True

        #keyboard input
        keyboard = pygame.key.get_pressed()

        left_mouse = pygame.mouse.get_pressed()[0]
        right_mouse = pygame.mouse.get_pressed()[2]

        if keyboard[pygame.K_LEFT] and player_x > 0:
            player_x -= 10

        if keyboard[pygame.K_a] and player_x > 0:
            player_x -= 10

        if keyboard[pygame.K_RIGHT] and player_x < (screen_size.current_w) - 100:
            player_x += 10

        if keyboard[pygame.K_d] and player_x < (screen_size.current_w) - 100:
            player_x += 10

        if keyboard[pygame.K_UP] and player_y > 0:
            player_y -= 10

        if keyboard[pygame.K_w] and player_y > 0:
            player_y -= 10

        if keyboard[pygame.K_DOWN] and player_y < (screen_size.current_h - 600):
            player_y += 10

        if keyboard[pygame.K_s] and player_y < (screen_size.current_h - 600):
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

        #craft
        if keyboard[pygame.K_c] and cancel_action_down == True:
            crafting = True

        #load game
        if keyboard[pygame.K_TAB] and player_y < (screen_size.current_h):
            load_game = True

        #right mouse
        if right_mouse:
            place_entity = True

        #only 1 craftable item
        if pygame.mouse.get_pos()[1] >= screen_size.current_h - 200 and pygame.mouse.get_pos()[1] <= screen_size.current_h - 100 and pygame.mouse.get_pos()[0] > (screen_size.current_w * (4/16)) and pygame.mouse.get_pos()[0] < screen_size.current_w * (6/16) and left_mouse:
                crafting_confirm = True

        else:
            crafting_confirm = False

        #left mouse
        if left_mouse:
            if pygame.mouse.get_pos()[1] < screen_size.current_h - 200:
                break_entity = True
                cancel_action = False
                crafting = False
                crafting_confirm = False
                
            if pygame.mouse.get_pos()[1] >= screen_size.current_h - 200:
                #inventory 1
                if pygame.mouse.get_pos()[0] > (screen_size.current_w * (4/16)) and pygame.mouse.get_pos()[0] < screen_size.current_w * (6/16):
                    inventory_1 = True
                    inventory_2 = False
                    inventory_3 = False
                    inventory_4 = False

                #inventory 2
                if pygame.mouse.get_pos()[0] > (screen_size.current_w * (6/16)) and pygame.mouse.get_pos()[0] < screen_size.current_w * (8/16):
                    inventory_1 = False
                    inventory_2 = True
                    inventory_3 = False
                    inventory_4 = False

                #inventory 3
                if pygame.mouse.get_pos()[0] > (screen_size.current_w * (8/16)) and pygame.mouse.get_pos()[0] < screen_size.current_w * (10/16):
                    inventory_1 = False
                    inventory_2 = False
                    inventory_3 = True
                    inventory_4 = False

                #inventory 4
                if pygame.mouse.get_pos()[0] > (screen_size.current_w * (10/16)) and pygame.mouse.get_pos()[0] < screen_size.current_w * (12/16):
                    inventory_1 = False
                    inventory_2 = False
                    inventory_3 = False
                    inventory_4 = True

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
        player_health_boolean = True

        #pet ai
        if player_x < pet_x:
            pet_x -= 1

        if player_x > pet_x:
            pet_x += 1

        if player_y < pet_y:
            pet_y -= 1

        if player_y > pet_y:
            pet_y += 1

        #hotbar
        
        #slot 1
        if inventory_1 == True:
            pygame.draw.rect(my_screen, "white", pygame.Rect(screen_size.current_w * (4/16), screen_size.current_h - 100, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "dark gray", pygame.Rect(screen_size.current_w * (6/16), screen_size.current_h - 100, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "light gray", pygame.Rect(screen_size.current_w * (8/16), screen_size.current_h - 100, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "dark gray", pygame.Rect(screen_size.current_w * (10/16), screen_size.current_h - 100, screen_size.current_w / 8, screen_size.current_h - 100))

        #slot 2
        if inventory_2 == True:
            pygame.draw.rect(my_screen, "light gray", pygame.Rect(screen_size.current_w * (4/16), screen_size.current_h - 100, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "white", pygame.Rect(screen_size.current_w * (6/16), screen_size.current_h - 100, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "light gray", pygame.Rect(screen_size.current_w * (8/16), screen_size.current_h - 100, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "dark gray", pygame.Rect(screen_size.current_w * (10/16), screen_size.current_h - 100, screen_size.current_w / 8, screen_size.current_h - 100))

        if inventory_3 == True:
            pygame.draw.rect(my_screen, "light gray", pygame.Rect(screen_size.current_w * (4/16), screen_size.current_h - 100, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "dark gray", pygame.Rect(screen_size.current_w * (6/16), screen_size.current_h - 100, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "white", pygame.Rect(screen_size.current_w * (8/16), screen_size.current_h - 100, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "dark gray", pygame.Rect(screen_size.current_w * (10/16), screen_size.current_h - 100, screen_size.current_w / 8, screen_size.current_h - 100))

        if inventory_4 == True:
            pygame.draw.rect(my_screen, "light gray", pygame.Rect(screen_size.current_w * (4/16), screen_size.current_h - 100, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "dark gray", pygame.Rect(screen_size.current_w * (6/16), screen_size.current_h - 100, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "light gray", pygame.Rect(screen_size.current_w * (8/16), screen_size.current_h - 100, screen_size.current_w / 8, screen_size.current_h - 100))
            pygame.draw.rect(my_screen, "white", pygame.Rect(screen_size.current_w * (10/16), screen_size.current_h - 100, screen_size.current_w / 8, screen_size.current_h - 100))

        #crafting
        if crafting == True:
            plank_boi = False
            total_log_boi = 0

            if crafting_confirm == False:
                #craft planks
                for i in range(len(inventory)):
                    if i < len(inventory):
                        if inventory[i] == "log":
                            plank_boi = True
                            total_log_boi = log_total[i]

            if plank_boi == True and cancel_action == False:
                #planks only
                pygame.draw.rect(my_screen, "red", pygame.Rect(screen_size.current_w * (4/16), screen_size.current_h - 200, screen_size.current_w / 8, 100))
                my_screen.blit(plank_image_inventory,(screen_size.current_w * (4/16) + 100, screen_size.current_h - 175))
                plank_font = item_total_font.render(str(total_log_boi * 4),True, ("black"))
                my_screen.blit(plank_font, (screen_size.current_w * (4/16) + 200, screen_size.current_h - 175))
                
            if crafting_confirm == True and cancel_action == False:
                crafting = False
                crafting_confirm = False
                plank_boi = False
                #planks
                for i in range(len(inventory)):
                    if inventory[i] == "log":
                        for ii in range(len(inventory)):
                            if inventory[ii] == "plank":
                                #inventory[ii] = "plank"
                                plank_total[ii] += log_total[i] * 4
                                log_total[i] = 0
                                break

                            else:
                                inventory[i] = "plank"
                                plank_total[i] = log_total[i] * 4
                                log_total[i] = 0
                                break

            if cancel_action == True:
                cancel_action = False
                crafting = False
                crafting_confirm = False
                            
        #render player
        if player_health > 0:
            my_screen.blit(lion_image_1,(player_x, player_y))
            my_screen.blit(player_health_font, (100,(screen_size.current_h) - 100))
            
        #place entity
        if place_entity == True:
            place_entity = False
            exists = False

            #inventory 1
            if inventory_1 == True:
                #print(int(math.ceil(player_x / 100.0)) * 100)
                #log
                if inventory[0] == "log" and int(log_total[0]) > 0:
                    for i in range(len(log_list_x)):
                        if log_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                            if log_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                exists = True
                                break

                    if exists == False:
                        for i in range(len(sapling_list_x)):
                            if sapling_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                                if sapling_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                    exists = True
                                    break
                        
                    if exists == False:
                        log_list_x = np.append(log_list_x, int(math.ceil(player_x / 100.0)) * 100)
                        log_list_y = np.append(log_list_y, int(math.ceil(player_y / 100.0)) * 100)
                        log_total[0] = log_total[0] - 1

                #plank
                if inventory[0] == "plank" and int(plank_total[0]) > 0:
                    for i in range(len(plank_list_x)):
                        if plank_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                            if plank_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                exists = True
                                break

                    if exists == False:
                        for i in range(len(plank_list_x)):
                            if plank_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                                if plank_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                    exists = True
                                    break
                        
                    if exists == False:
                        plank_list_x = np.append(plank_list_x, int(math.ceil(player_x / 100.0)) * 100)
                        plank_list_y = np.append(plank_list_y, int(math.ceil(player_y / 100.0)) * 100)
                        plank_total[0] = plank_total[0] - 1

                #sapling
                if inventory[0] == "sapling" and int(sapling_total[0]) > 0:
                    for i in range(len(log_list_x)):
                        if log_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                            if log_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                exists = True
                                break

                    if exists == False:
                        for i in range(len(sapling_list_x)):
                            if sapling_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                                if sapling_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                    exists = True
                                    break
                                
                    if exists == False:
                        sapling_list_x = np.append(sapling_list_x, int(math.ceil(player_x / 100.0)) * 100)
                        sapling_list_y = np.append(sapling_list_y, int(math.ceil(player_y / 100.0)) * 100)
                        sapling_total[0] = sapling_total[0] - 1

            #inventory 2
            if inventory_2 == True:
                #log
                if inventory[1] == "log" and int(log_total[1]) > 0:
                    for i in range(len(log_list_x)):
                        if log_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                            if log_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                exists = True
                                break

                    if exists == False:
                        for i in range(len(sapling_list_x)):
                            if sapling_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                                if sapling_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                    exists = True
                                    break
                        
                    if exists == False:
                        log_list_x = np.append(log_list_x, int(math.ceil(player_x / 100.0)) * 100)
                        log_list_y = np.append(log_list_y, int(math.ceil(player_y / 100.0)) * 100)
                        log_total[1] = log_total[1] - 1

                #plank
                if inventory[1] == "plank" and int(plank_total[1]) > 0:
                    for i in range(len(plank_list_x)):
                        if plank_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                            if plank_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                exists = True
                                break

                    if exists == False:
                        for i in range(len(plank_list_x)):
                            if plank_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                                if plank_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                    exists = True
                                    break
                        
                    if exists == False:
                        plank_list_x = np.append(plank_list_x, int(math.ceil(player_x / 100.0)) * 100)
                        plank_list_y = np.append(plank_list_y, int(math.ceil(player_y / 100.0)) * 100)
                        plank_total[1] = plank_total[1] - 1

                #saplings
                if inventory[1] == "sapling" and int(sapling_total[1]) > 0:
                    for i in range(len(log_list_x)):
                        if log_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                            if log_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                exists = True
                                break

                    if exists == False:
                        for i in range(len(sapling_list_x)):
                            if sapling_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                                if sapling_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                    exists = True
                                    break
                        
                    if exists == False:
                        sapling_list_x = np.append(sapling_list_x, int(math.ceil(player_x / 100.0)) * 100)
                        sapling_list_y = np.append(sapling_list_y, int(math.ceil(player_y / 100.0)) * 100)
                        sapling_total[1] = sapling_total[1] - 1

            #inventory 3
            if inventory_3 == True:
                #log
                if inventory[2] == "log" and int(log_total[2]) > 0:
                    for i in range(len(log_list_x)):
                        if log_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                            if log_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                exists = True
                                break

                    if exists == False:
                        for i in range(len(sapling_list_x)):
                            if sapling_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                                if sapling_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                    exists = True
                                    break
                        
                    if exists == False:
                        log_list_x = np.append(log_list_x, int(math.ceil(player_x / 100.0)) * 100)
                        log_list_y = np.append(log_list_y, int(math.ceil(player_y / 100.0)) * 100)
                        log_total[2] = log_total[2] - 1

                #plank
                if inventory[2] == "plank" and int(plank_total[2]) > 0:
                    for i in range(len(plank_list_x)):
                        if plank_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                            if plank_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                exists = True
                                break

                    if exists == False:
                        for i in range(len(plank_list_x)):
                            if plank_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                                if plank_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                    exists = True
                                    break
                        
                    if exists == False:
                        plank_list_x = np.append(plank_list_x, int(math.ceil(player_x / 100.0)) * 100)
                        plank_list_y = np.append(plank_list_y, int(math.ceil(player_y / 100.0)) * 100)
                        plank_total[2] = plank_total[2] - 1

                #saplings
                if inventory[2] == "sapling" and int(sapling_total[2]) > 0:
                    for i in range(len(log_list_x)):
                        if log_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                            if log_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                exists = True
                                break

                    if exists == False:
                        for i in range(len(sapling_list_x)):
                            if sapling_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                                if sapling_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                    exists = True
                                    break
                        
                    if exists == False:
                        sapling_list_x = np.append(sapling_list_x, int(math.ceil(player_x / 100.0)) * 100)
                        sapling_list_y = np.append(sapling_list_y, int(math.ceil(player_y / 100.0)) * 100)
                        sapling_total[2] = sapling_total[2] - 1

            #inventory 4
            if inventory_4 == True:
                #log
                if inventory[3] == "log" and int(log_total[3]) > 0:
                    for i in range(len(log_list_x)):
                        if log_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                            if log_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                exists = True
                                break

                    if exists == False:
                        for i in range(len(sapling_list_x)):
                            if sapling_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                                if sapling_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                    exists = True
                                    break
                        
                    if exists == False:
                        log_list_x = np.append(log_list_x, int(math.ceil(player_x / 100.0)) * 100)
                        log_list_y = np.append(log_list_y, int(math.ceil(player_y / 100.0)) * 100)
                        log_total[3] = log_total[3] - 1

                #plank
                if inventory[3] == "plank" and int(plank_total[3]) > 0:
                    for i in range(len(plank_list_x)):
                        if plank_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                            if plank_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                exists = True
                                break

                    if exists == False:
                        for i in range(len(plank_list_x)):
                            if plank_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                                if plank_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                    exists = True
                                    break
                        
                    if exists == False:
                        plank_list_x = np.append(plank_list_x, int(math.ceil(player_x / 100.0)) * 100)
                        plank_list_y = np.append(plank_list_y, int(math.ceil(player_y / 100.0)) * 100)
                        plank_total[3] = plank_total[3] - 1

                #saplings
                if inventory[3] == "sapling" and int(sapling_total[3]) > 0:
                    for i in range(len(log_list_x)):
                        if log_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                            if log_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                exists = True
                                break

                    if exists == False:
                        for i in range(len(sapling_list_x)):
                            if sapling_list_x[i] == (int(math.ceil(player_x / 100.0)) * 100):
                                if sapling_list_y[i] == (int(math.ceil(player_y / 100.0)) * 100):
                                    exists = True
                                    break
                        
                    if exists == False:
                        sapling_list_x = np.append(sapling_list_x, int(math.ceil(player_x / 100.0)) * 100)
                        sapling_list_y = np.append(sapling_list_y, int(math.ceil(player_y / 100.0)) * 100)
                        sapling_total[3] = sapling_total[3] - 1
                
        #break entity
        if break_entity == True:
            break_entity = False

            #entities
            #log
            for i in range(len(log_list_x)):
                if i < len(log_list_x):
                    if player_x <= log_list_x[i] + 75 and player_x >= log_list_x[i] - 75:
                        if player_y <= log_list_y[i] + 75 and player_y >= log_list_y[i] - 75:
                            log_list_x = np.delete(log_list_x, i)
                            log_list_y = np.delete(log_list_y, i)
                            counter = 0

                            for i in inventory:
                                if i == "" or i == "log":
                                    inventory[counter] = "log"
                                    log_total[counter] = log_total[counter] + 1
                                    break
                                
                                counter += 1

            #plank
            for i in range(len(plank_list_x)):
                if i < len(plank_list_x):
                    if player_x <= plank_list_x[i] + 75 and player_x >= plank_list_x[i] - 75:
                        if player_y <= plank_list_y[i] + 75 and player_y >= plank_list_y[i] - 75:
                            plank_list_x = np.delete(plank_list_x, i)
                            plank_list_y = np.delete(plank_list_y, i)
                            counter = 0

                            for i in inventory:    
                                if i == "" or i == "plank":
                                    inventory[counter] = "plank"
                                    plank_total[counter] = plank_total[counter] + 1
                                    break
                                
                                counter += 1

            #sapling
            for i in range(len(sapling_list_x)):
                if i < len(sapling_list_x):
                    if player_x <= sapling_list_x[i] + 75 and player_x >= sapling_list_x[i] - 75:
                        if player_y <= sapling_list_y[i] + 75 and player_y >= sapling_list_y[i] - 75:
                            sapling_list_x = np.delete(sapling_list_x, i)
                            sapling_list_y = np.delete(sapling_list_y, i)
                            counter = 0

                            for i in inventory:    
                                if i == "" or i == "sapling":
                                    inventory[counter] = "sapling"
                                    sapling_total[counter] = sapling_total[counter] + 1
                                    break
                                
                                counter += 1

            #terrain
            #trees
            for i in range(len(tree_x)):
                if i < len(tree_x):
                    if player_x <= tree_x[i] + 75 and player_x >= tree_x[i] - 75:
                        if player_y <= tree_y[i] + 75 and player_y >= tree_y[i] - 75:
                            tree_x = np.delete(tree_x, i)
                            tree_y = np.delete(tree_y, i)
                            counter = 0
                            
                            for i in inventory:
                                rand = random.randint(4,6)

                                if i == "" or i == "log":
                                    inventory[counter] = "log"
                                    log_total[counter] = log_total[counter] + rand
                                    break

                                counter += 1

                            counter = 0

                            for i in inventory:
                                rand = random.randint(1,3)

                                if i == "" or i == "sapling":
                                    inventory[counter] = "sapling"
                                    sapling_total[counter] = sapling_total[counter] + rand
                                    break

                                counter += 1
                            
        #render entities in inventory
        if load_game == False:
            #pet
            my_screen.blit(axolotl_image,(pet_x, pet_y))
            
            #log
            if log_total[0] > 0:
                my_screen.blit(log_image_inventory,(screen_size.current_w * (4/16) + 100, screen_size.current_h - 75))
                item_font_1 = item_total_font.render(str(log_total[0]),True, ("black"))
                my_screen.blit(item_font_1, (screen_size.current_w * (4/16) + 200, screen_size.current_h - 100))

            if log_total[1] > 0:
                my_screen.blit(log_image_inventory,(screen_size.current_w * (6/16) + 100, screen_size.current_h - 75))
                item_font_2 = item_total_font.render(str(log_total[1]),True, ("black"))
                my_screen.blit(item_font_2, (screen_size.current_w * (6/16) + 200, screen_size.current_h - 100))

            if log_total[2] > 0:
                my_screen.blit(log_image_inventory,(screen_size.current_w * (8/16) + 100, screen_size.current_h - 75))
                item_font_3 = item_total_font.render(str(log_total[2]),True, ("black"))
                my_screen.blit(item_font_3, (screen_size.current_w * (8/16) + 200, screen_size.current_h - 100))

            if log_total[3] > 0:
                my_screen.blit(log_image_inventory,(screen_size.current_w * (10/16) + 100, screen_size.current_h - 75))
                item_font_4 = item_total_font.render(str(log_total[3]),True, ("black"))
                my_screen.blit(item_font_4, (screen_size.current_w * (10/16) + 200, screen_size.current_h - 100))

            #plank
            if plank_total[0] > 0:
                my_screen.blit(plank_image_inventory,(screen_size.current_w * (4/16) + 100, screen_size.current_h - 75))
                item_font_1 = item_total_font.render(str(plank_total[0]),True, ("black"))
                my_screen.blit(item_font_1, (screen_size.current_w * (4/16) + 200, screen_size.current_h - 100))

            if plank_total[1] > 0:
                my_screen.blit(plank_image_inventory,(screen_size.current_w * (6/16) + 100, screen_size.current_h - 75))
                item_font_2 = item_total_font.render(str(plank_total[1]),True, ("black"))
                my_screen.blit(item_font_2, (screen_size.current_w * (6/16) + 200, screen_size.current_h - 100))

            if plank_total[2] > 0:
                my_screen.blit(plank_image_inventory,(screen_size.current_w * (8/16) + 100, screen_size.current_h - 75))
                item_font_3 = item_total_font.render(str(plank_total[2]),True, ("black"))
                my_screen.blit(item_font_3, (screen_size.current_w * (8/16) + 200, screen_size.current_h - 100))

            if plank_total[3] > 0:
                my_screen.blit(plank_image_inventory,(screen_size.current_w * (10/16) + 100, screen_size.current_h - 75))
                item_font_4 = item_total_font.render(str(plank_total[3]),True, ("black"))
                my_screen.blit(item_font_4, (screen_size.current_w * (10/16) + 200, screen_size.current_h - 100))

            #sapling
            if sapling_total[0] > 0:
                my_screen.blit(sapling_image_inventory,(screen_size.current_w * (4/16) + 100, screen_size.current_h - 75))
                item_font_1 = item_total_font.render(str(sapling_total[0]),True, ("black"))
                my_screen.blit(item_font_1, (screen_size.current_w * (4/16) + 200, screen_size.current_h - 100))

            if sapling_total[1] > 0:
                my_screen.blit(sapling_image_inventory,(screen_size.current_w * (6/16) + 100, screen_size.current_h - 75))
                item_font_2 = item_total_font.render(str(sapling_total[1]),True, ("black"))
                my_screen.blit(item_font_2, (screen_size.current_w * (6/16) + 200, screen_size.current_h - 100))

            if sapling_total[2] > 0:
                my_screen.blit(sapling_image_inventory,(screen_size.current_w * (8/16) + 100, screen_size.current_h - 75))
                item_font_3 = item_total_font.render(str(sapling_total[2]),True, ("black"))
                my_screen.blit(item_font_3, (screen_size.current_w * (8/16) + 200, screen_size.current_h - 100))

            if sapling_total[3] > 0:
                my_screen.blit(sapling_image_inventory,(screen_size.current_w * (10/16) + 100, screen_size.current_h - 75))
                item_font_4 = item_total_font.render(str(sapling_total[3]),True, ("black"))
                my_screen.blit(item_font_4, (screen_size.current_w * (10/16) + 200, screen_size.current_h - 100))

            #growth
            random_sapling_growth = random.randint(0,len(sapling_list_x))
            random_time = random.randint(1,10000)

            if random_time == 1 and len(sapling_list_x) > 0:
                if random_sapling_growth < len(sapling_list_x):
                    tree_x = np.append(tree_x, sapling_list_x[random_sapling_growth])
                    tree_y = np.append(tree_y, sapling_list_y[random_sapling_growth])
                    sapling_list_x = np.delete(sapling_list_x, random_sapling_growth)
                    sapling_list_y = np.delete(sapling_list_y, random_sapling_growth)

            #render log
            for i in range(len(log_list_x)):
                if i < len(log_list_x):
                    my_screen.blit(log_image,(log_list_x[i], log_list_y[i]))

            #render plank
            for i in range(len(plank_list_x)):
                if i < len(plank_list_x):
                    my_screen.blit(plank_image,(plank_list_x[i], plank_list_y[i]))

            #render sapling
            for i in range(len(sapling_list_x)):
                if i < len(sapling_list_x):
                    my_screen.blit(sapling_image,(sapling_list_x[i], sapling_list_y[i]))

            #render tree
            for i in range(len(tree_x)):
                if i < len(tree_x):
                    my_screen.blit(tree_image,(tree_x[i], tree_y[i]))

        if load_game == True:
            load_game = False

        #display fps
        fps = item_total_font.render("fps: " + str(int(math.floor(clock.get_fps()))),True, ("black"))
        my_screen.blit(fps, (100,(screen_size.current_h) - 200))

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
        break_block = sub_font.render("left click = break block",True,(0,0,0))
        place_block = sub_font.render("right click = place block",True,(0,0,0))
        hotbar = sub_font.render("1-4 = hotbar",True,(0,0,0))
        crafting = sub_font.render("c = crafting",True,(0,0,0))

        my_screen.blit(title, (100,50))
        my_screen.blit(one, (100, 200))
        my_screen.blit(reset, (100, 250))
        my_screen.blit(escape, (100, 300))
        my_screen.blit(my_help, (100, 350))
        my_screen.blit(load, (100, 400))
        my_screen.blit(break_block, (100, 450))
        my_screen.blit(place_block, (100, 500))
        my_screen.blit(hotbar, (100, 550))
        my_screen.blit(crafting, (100, 600))

        pygame.display.flip()

    pygame.quit()

title_screen()
