import os


name = ""

death_level = ""
victory_level = ""

def user_name():
    os.system("clear")

    global name

    global death_level
    global victory_level
    
    name = input("What is your name?\n")

    death_level = name + ", YOU LOSE!\nTHE END!"
    victory_level = name + ", YOU WIN!\nTHE END!"

    volor_savanna_original()

def volor_savanna_original():
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

    hunter_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    hunter_list[1] = input("\nYou have chosen to be a hunter!\nDo you want to go hunt or stay put?\n\n1- Hunt; 2- Stay put\nMake Your Choice " + name + ":\n")

    if hunter_list[1] == "1":
        os.system("clear")

        hunter_list[2] = input("\nYou have chosen to go hunt!\nYou have gone hunting.\nYou didn't find any food.\nYou return to your village.\nLuckily, the farmer has enough crops to last your tribe a week.\nDo you want to go hunt right away to make up lost time or do you choose to go eat?\n1- Hunt; 2- Eat\nMake Your Choice " + name + ":\n")

    if hunter_list[1] == "2":
        os.system("clear")
        
        pause = input("\nYou have chosen to stay put.\nUnfortunately, your whole village parishes from hunger.\n" + death_level)

        volor_savanna_original()

    if hunter_list[2] == "1":
        os.system("clear")

        hunter_list[3] = input("\nYou have chosen to go hunt!\nYou go on a successful hunt that should last your tribe a month.\nHowever, you are very tired and because you didn't eat, you have become very sick with malnutrition.\nUnluckily for you, the tribes medicine women is very busy and has a lot of patients to take care of first.\nDo you wish to wait for her or tough it out?\n1- Wait for her; 2- Tough it out\nMake Your Choice " + name + ":\n")

    if hunter_list[2] == "2":
        os.system("clear")

        hunter_list[4] = input("\nYou have chosen to eat.\nYou are fully fueled with energy.\nDo you want to go hunting or play a game with the rest of your tribe?\n1- Hunt; 2- Play a game with the rest of my tribe\nMake Your Choice " + name + ":\n")

    if hunter_list[3] == "1":
        os.system("clear")

        hunter_list[5] = input("\nYou have chosen to wait for her.\nBecause You have chosen to wait for her patiently, she attends to you in a matter of a couple days.\nYou are better in a week.\nSome white men have come to your tribe.\nThey're asking to trade you guns for some of your tribe's animal pelts.\nDo you trade them pelts for guns?\n1- Trade; 2- Not trade\nMake Your Choice " + name + ":\n")

    if hunter_list[3] == "2":
        os.system("clear")

        pause = input("\nYou have chosen to tough it out.\nUnfortunately, because of this, you die from malnutrition.\n" + death_level)

        volor_savanna_original()

    if hunter_list[4] == "1":
        os.system("clear")

        hunter_list[6] = input("\nYou have chosen to hunt.\nYou have found a bunch of zebras to eat.\nSome white men are willing to trade your tribe rifles for some of your zebras.\nRecently, there has been some highly wanted criminals that trade weapons and drugs on the black market.\nThe problem is, you don't know if that's them.\nDo you trade?\nWhat about decline the offer?\nOr do you report them to the authorities?\n1- Trade; 2- Decline the trade; 3- Report them to the authorities\nMake Your Choice " + name + ":\n")

    if hunter_list[4] == "2":
        os.system("clear")

        hunter_list[7] = input("\nYou have chosen to play a game with the rest of your tribe.\nEveryone has a good time and you guys have an awesome feast.\nThere is a hunting challenge that your tribe is having.\nThe challenge is to go hunt The Mighty Lion!\nDo you want to go hunt The Mighty Lion with your tribe to win the challenge?\n1- Yes; 2- No\nMake Your Choice " + name + ":\n")

    if hunter_list[5] == "1":
        os.system("clear")

        hunter_list[8] = input("\nYou have chosen to trade.\nThey trade you guns.\nDo you want to go hunt The Mighty Lion?\n1- Yes; 2- No\nMake Your Choice " + name + ":\n")

    if hunter_list[5] == "2":
        os.system("clear")

        hunter_list[9] = ("\nYou have chosen not to trade.\nBecause of this they want to kill you.\nDo you escape?\n1- Find out!\nMake Your Choice " + name + ":\n")

    if hunter_list[6] == "1":
        os.system("clear")

        pause = input("\nYou have chosen to trade.\nLuckily, these aren't the criminals that are wanted.\nA couple months later the white men settle here.\nPeople keep on flooding into the white men's settlement.\nBecause of this your village becomes rich.\n" + victory_level)

        volor_savanna_original()

    if hunter_list[6] == "2":
        os.system("clear")

        pause = input("\nYou have chosen to decline the trade.\nUnfortunately, these people have smallpox.\nThey transmit it to your tribe.\nBecause you tribe doesn't have any immunity against smallpox your whole tribe dies!\n" + death_level)

        volor_savanna_original()
        
user_name()
