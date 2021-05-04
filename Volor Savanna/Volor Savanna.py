#Started: 21 April 2021

from tkinter import*

import os
import random
import tkinter

main = tkinter.Tk()

grass_block_entity = []
grass_block_x = []
grass_block_y = []

#player_1_image = r"/home/linux/Downloads/test.png"
player_1_image = "player 1.png"
player_1_image = PhotoImage(file = player_1_image)

#grass_image = r"/home/linux/Downloads/grass.png"
grass_image = "grass.png"
grass_image = PhotoImage(file = grass_image)

seed_logic = random.seed("hello")
seed_logic = random.randint(1,1000)
print(seed_logic)

#x = 850
#y = 600

width = main.winfo_screenwidth() 
height = main.winfo_screenheight()
#print("w=",width,"h=",height)

x = width / 2
y = height / 2

canvas = tkinter.Canvas(main, bg = "green", height = height, width = width)

def grass_logic():
    logic = seed_logic + 400
    grass_block_x.append(logic)
    
    logic = seed_logic + 400
    grass_block_y.append(logic)

    grass_block_entity.append("grass")

    logic = seed_logic + 500
    grass_block_x.append(logic)

    logic = seed_logic + 500
    grass_block_y.append(logic)

    grass_block_entity.append("grass")
    
    logic = seed_logic + 300
    grass_block_x.append(logic)

    logic = seed_logic + 600
    grass_block_y.append(logic)

    grass_block_entity.append("grass")
    
    logic = seed_logic + 600
    grass_block_x.append(logic)

    logic = seed_logic + 300
    grass_block_y.append(logic)

    grass_block_entity.append("grass")
    
    for i in range(0, len(grass_block_entity)):
        #grass_entity = canvas.create_image(grass_block_x[i], grass_block_y[i], image = grass_image)
        grass_block_entity[i] = canvas.create_image(grass_block_x[i], grass_block_y[i], image = grass_image)
        
def down(event): 
    global y
    y += 50
    #canvas.move(player_1, 0, 50)
    print(x,y)

    for i in range (0, len(grass_block_entity)):
        canvas.move(grass_block_entity[i], 0, -50)

def escape(event):
    main.destroy()
    
def left(event):
    global x
    x -= 50
    #canvas.move(player_1, -50, 0)
    print(x,y)

    for i in range (0, len(grass_block_entity)):
        canvas.move(grass_block_entity[i], 50, 0)

def right(event):
    global x
    x+= 50
    #canvas.move(player_1, 50, 0)
    print(x,y)

    for i in range (0, len(grass_block_entity)):
        canvas.move(grass_block_entity[i], -50, 0)
    
def up(event):
    global y
    y -= 50
    #canvas.move(player_1, 0, -50)
    print(x,y)

    for i in range (0, len(grass_block_entity)):
        canvas.move(grass_block_entity[i], 0, 50)

main.bind("<a>", left)
main.bind("<d>", right)
main.bind("<Escape>", escape)
main.bind("<s>", down)
main.bind("<w>", up)

player_1 = canvas.create_image(x, y, image = player_1_image)

grass_logic()

canvas.pack()
main.mainloop()
