#Started: 21 April 2021

from tkinter import*
from tkinter.ttk import*

import math
import os
import pygame
import random
import tkinter
import time

chunk_x = 0
chunk_y = 0

main = Tk()
label = Label(main)

width = main.winfo_screenwidth() 
height = main.winfo_screenheight()
canvas = tkinter.Canvas(main, bg = "green", height = height, width = width)

grass_block_entity = []
grass_block_x = []
grass_block_y = []

index = 0

player_1_image = PhotoImage(file = "images/standing.png")
image_1 = PhotoImage(file = "images/L1.png")
image_2 = PhotoImage(file = "images/R1.png")

player_1_button = Button(main)
player_1_button.grid(row = 1)

grass_image = "images/grass.png"
grass_image = PhotoImage(file = grass_image)

player_1_x = width / 2
player_1_y = height / 2

def down(event):
    global player_1_y

    chunk_y = player_1_y / height
    chunk = math.ceil(chunk_y)
    print("Chunk y:", + chunk)
    
    player_1_y += 50
    
    print(player_1_x, player_1_y)

    for i in range (0, len(grass_block_entity)):
        canvas.move(grass_block_entity[i], 0, -50)

def escape(event):
    main.destroy()
    
def left(event):
    global image_1
    global image_2
    player_1_button.config(image = image_1)
    player_1_button.update()
    
    time.sleep(1)
    player_1_button.config(image = image_2)
    player_1_button.update()
    
    global player_1_x

    chunk_x = player_1_x / width
    chunk = math.ceil(chunk_x)
    print("Chunk x:", + chunk)
    
    player_1_x -= 50
    
    print(player_1_x, player_1_y)

    for i in range (0, len(grass_block_entity)):
        canvas.move(grass_block_entity[i], 50, 0)

def right(event):
    global player_1_x

    chunk_x = player_1_x / width
    chunk = math.ceil(chunk_x)
    print("Chunk x:", + chunk)
    
    player_1_x += 50

    print(player_1_x, player_1_y)

    for i in range (0, len(grass_block_entity)):
        canvas.move(grass_block_entity[i], -50, 0)
    
def up(event):
    global player_1_y

    chunk_y = player_1_y / height
    chunk = math.ceil(chunk_y)
    print("Chunk y:", + chunk)
    
    player_1_y -= 50

    print(player_1_x, player_1_y)

    for i in range (0, len(grass_block_entity)):
        canvas.move(grass_block_entity[i], 0, 50)
        
seed_logic = random.seed("hello!")
seed_logic = random.randint(1,1000)
print("Seed:", seed_logic)

def grass_logic():
    print("ok")

    for i in range(1,10):
        print("i:", i)
        logic = i * ((seed_logic % 4096) + 500)
        grass_block_x.append(logic)
        
        logic = i * ((seed_logic % 4096) + 400)
        grass_block_y.append(logic)

        grass_block_entity.append("grass")

        logic = i * ((seed_logic % 4096) + 700)
        grass_block_x.append(logic)

        logic = i * ((seed_logic % 4096) + 400)
        grass_block_y.append(logic)

        grass_block_entity.append("grass")

        logic = i * ((seed_logic % 4096) + 900)
        grass_block_x.append(logic)

        logic = i * ((seed_logic % 4096) + 400)
        grass_block_y.append(logic)

        grass_block_entity.append("grass")
        
        logic = i * ((seed_logic % 4096) + 400)
        grass_block_x.append(logic)

        logic = i * ((seed_logic % 4096) + 600)
        grass_block_y.append(logic)

        grass_block_entity.append("grass")
        
        logic = i * ((seed_logic % 4096) + 600)
        grass_block_x.append(logic)

        logic = i * ((seed_logic % 4096) + 600)
        grass_block_y.append(logic)

        grass_block_entity.append("grass")

        logic = i * ((seed_logic % 4096) + 800)
        grass_block_x.append(logic)

        logic = i * ((seed_logic % 4096) + 600)
        grass_block_y.append(logic)

        grass_block_entity.append("grass")
    
    for i in range(0, len(grass_block_entity)):
        grass_block_entity[i] = canvas.create_image(grass_block_x[i], grass_block_y[i], image = grass_image)

    print("logic:", logic)
        
main.bind("<a>", left)
main.bind("<d>", right)
main.bind("<Escape>", escape)
main.bind("<s>", down)
main.bind("<w>", up)

grass_logic()

canvas.grid()

main.mainloop()
