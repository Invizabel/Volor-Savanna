import os


name = ""

def volor_savanna_original():
    os.system("clear")

    global name
    name = input("What is your name?\n")

    os.system("clear")
    character = input("\nWelcome to Volor Savanna!\nYou are a member of an African Tribe!\nWho do you want to be?\n\n1- Hunter\n2- Warrior\n3- Crafter\n4- Farmer\n5- Medicine Person\n")

    if character == "1":
        hunter()

    if character == "2":
        warrior()

    if character == "3":
        crafter()

    if character == "4":
        farmer()

    if character == "5":
        medicine_person()

def hunter():
    os.system("clear")

    hunter_list = ["0", "1", "2", "3", "4", "5"]

    hunter_list[1] = input("\nYou have chosen to be a hunter!\nDo you want to go hunt or stay put?\n\n1- Hunt; 2- Stay put\nMake Your Choice " + name + ":\n")
    
volor_savanna_original()
