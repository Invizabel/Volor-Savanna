#Started: 21 April 2021

from tkinter import*

import math
import os
import random
import tkinter

chunk_x = 0
chunk_y = 0

main = tkinter.Tk()

grass_block_entity = []
grass_block_x = []
grass_block_y = []

player_1_image = "images/player 1.png"
player_1_image = PhotoImage(file = player_1_image)

grass_image = "images/grass.png"
grass_image = PhotoImage(file = grass_image)

width = main.winfo_screenwidth() 
height = main.winfo_screenheight()

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
        
canvas = tkinter.Canvas(main, bg = "green", height = height, width = width)

seed_logic = random.seed("hello")
seed_logic = random.randint(1,1000000000)
print("Seed:", seed_logic)

def grass_logic():
    print("ok")
    logic = (seed_logic % 4096) + 500
    grass_block_x.append(logic)
    
    logic = (seed_logic % 4096) + 400
    grass_block_y.append(logic)

    grass_block_entity.append("grass")

    logic = (seed_logic % 4096) + 700
    grass_block_x.append(logic)

    logic = (seed_logic % 4096) + 400
    grass_block_y.append(logic)

    grass_block_entity.append("grass")

    logic = (seed_logic % 4096) + 900
    grass_block_x.append(logic)

    logic = (seed_logic % 4096) + 400
    grass_block_y.append(logic)

    grass_block_entity.append("grass")
    
    logic = (seed_logic % 4096) + 400
    grass_block_x.append(logic)

    logic = (seed_logic % 4096) + 600
    grass_block_y.append(logic)

    grass_block_entity.append("grass")
    
    logic = (seed_logic % 4096) + 600
    grass_block_x.append(logic)

    logic = (seed_logic % 4096) + 600
    grass_block_y.append(logic)

    grass_block_entity.append("grass")

    logic = (seed_logic % 4096) + 800
    grass_block_x.append(logic)

    logic = (seed_logic % 4096) + 600
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

player_1 = canvas.create_image(player_1_x, player_1_y, image = player_1_image)

grass_logic()

canvas.pack()
main.mainloop()
