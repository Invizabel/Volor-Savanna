import os
import random

#the players name
name = ""

#variables for level finish
death_level = ""
victory_level = ""

#random number generator
rand = random.randint(1,2)

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

    character = input("Welcome to Volor Savanna!\nYou are a member of an African Tribe!\nWho do you want to be?\n\n1- Hunter\n2- Warrior\n3- Crafter\n4- Farmer\n5- Medicine Person\n")

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
    global rand
    rand = random.randint(1,2)
    
    os.system("clear")

    #keeps track of the players progress through the level. Used to prevent cheating.
    hunter_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    hunter_list[1] = input("You have chosen to be a hunter!\nDo you want to go hunt or stay put?\n\n1- Hunt; 2- Stay put\nMake your choice " + name + ":\n")

    if hunter_list[1] == "1":
        os.system("clear")

        hunter_list[2] = input("You have chosen to go hunt!\nYou have gone hunting.\nYou didn't find any food.\nYou return to your village.\nLuckily, the farmer has enough crops to last your tribe a week.\nDo you want to go hunt right away to make up lost time or do you choose to go eat?\n\n1- Hunt; 2- Eat\nMake your choice " + name + ":\n")

    if hunter_list[1] == "2":
        os.system("clear")
        
        pause = input("You have chosen to stay put.\nUnfortunately, your whole village parishes from hunger.\n" + death_level)

        volor_savanna_original()

    if hunter_list[2] == "1":
        os.system("clear")

        hunter_list[3] = input("You have chosen to go hunt!\nYou go on a successful hunt that should last your tribe a month.\nHowever, you are very tired and because you didn't eat, you have become very sick with malnutrition.\nUnluckily for you, the tribes medicine women is very busy and has a lot of patients to take care of first.\nDo you wish to wait for her or tough it out?\n\n1- Wait for her; 2- Tough it out\nMake your choice " + name + ":\n")

    if hunter_list[2] == "2":
        os.system("clear")

        hunter_list[4] = input("You have chosen to eat.\nYou are fully fueled with energy.\nDo you want to go hunting or play a game with the rest of your tribe?\n\n1- Hunt; 2- Play a game with the rest of my tribe\nMake your choice " + name + ":\n")

    if hunter_list[3] == "1":
        os.system("clear")

        hunter_list[5] = input("You have chosen to wait for her.\nBecause You have chosen to wait for her patiently, she attends to you in a matter of a couple days.\nYou are better in a week.\nSome white men have come to your tribe.\nThey're asking to trade you guns for some of your tribe's animal pelts.\nDo you trade them pelts for guns?\n\n1- Trade; 2- Not trade\nMake your choice " + name + ":\n")

    if hunter_list[3] == "2":
        os.system("clear")

        pause = input("You have chosen to tough it out.\nUnfortunately, because of this, you die from malnutrition.\n" + death_level)

        volor_savanna_original()

    if hunter_list[4] == "1":
        os.system("clear")

        hunter_list[6] = input("You have chosen to hunt.\nYou have found a bunch of zebras to eat.\nSome white men are willing to trade your tribe rifles for some of your zebras.\nRecently, there has been some highly wanted criminals that trade weapons and drugs on the black market.\nThe problem is, you don't know if that's them.\nDo you trade?\nWhat about decline the offer?\nOr do you report them to the authorities?\n\n1- Trade; 2- Decline the trade; 3- Report them to the authorities\nMake your choice " + name + ":\n")

    if hunter_list[4] == "2":
        os.system("clear")

        hunter_list[7] = input("You have chosen to play a game with the rest of your tribe.\nEveryone has a good time and you guys have an awesome feast.\nThere is a hunting challenge that your tribe is having.\nThe challenge is to go hunt The Mighty Lion!\nDo you want to go hunt The Mighty Lion with your tribe to win the challenge?\n\n1- Yes; 2- No\nMake your choice " + name + ":\n")

    if hunter_list[5] == "1":
        os.system("clear")

        hunter_list[8] = input("You have chosen to trade.\nThey trade you guns.\nDo you want to go hunt The Mighty Lion?\n\n1- Yes; 2- No\nMake your choice " + name + ":\n")

    if hunter_list[5] == "2":
        os.system("clear")

        hunter_list[9] = input("You have chosen not to trade.\nBecause of this they want to kill you.\nDo you escape?\n\n1- Find out!\nMake your choice " + name + ":\n")

    if hunter_list[6] == "1":
        os.system("clear")

        pause = input("You have chosen to trade.\nLuckily, these aren't the criminals that are wanted.\nA couple months later the white men settle here.\nPeople keep on flooding into the white men's settlement.\nBecause of this your village becomes rich.\n" + victory_level)

        volor_savanna_original()

    if hunter_list[6] == "2":
        os.system("clear")

        pause = input("You have chosen to decline the trade.\nUnfortunately, these people have smallpox.\nThey transmit it to your tribe.\nBecause you tribe doesn't have any immunity against smallpox your whole tribe dies!\n" + death_level)

        volor_savanna_original()

    if hunter_list[6] == "3":
        os.system("clear")

        hunter_list[10] = input("You have chosen to report them to the authorities.\nThese guys turn out to be the wanted criminals after all.\nYour tribe gains importance in the African community because you turned these criminals into the authorities.\nDo you want to go hunt The Mighty Lion?\n\n19- Yes; 20- No\nMake your choice " + name + ":\n")

    if hunter_list[7] == "1":
        the_mighty_lion()

    if hunter_list[7] == "2":
        os.system("clear")

        pause = input("You have chosen not to hunt The Mighty Lion.\nUnfortunately, you die from malaria.\n" + death_level)

        volor_savanna_original()

    if hunter_list[8] == "1":
        the_mighty_lion()

    if hunter_list[8] == "2":
        os.system("clear")

        pause = input("You have chosen not to hunt The Mighty Lion.\nUnfortunately, a random lightning bolt from out of nowhere, probably from Zeus, kills you.\n" + death_level)

        volor_savanna_original()
        
    if hunter_list[9] == "1" and rand == 1:
        os.system("clear")

        pause = input("Unfortunately, you don't escape.\nThey kill you on the spot with a feather.\n" + death_level)

        volor_savanna_original()

    if hunter_list[9] == "1" and rand == 2:
        os.system("clear")

        pause = input("You manage to escape.\nYou live a long and prosperous life!\n" + victory_level)

        volor_savanna_original()

    if hunter_list[10] == "1":
        volor_savanna_original()

    if hunter_list[10] == "2":
        os.system("clear")

        pause = input("You have chosen not to hunt The Mighty Lion.\nUnfortunately, a Chandra Planeswalker burns you to death!\n" + death_level)

        volor_savanna_original()
        
def the_mighty_lion():
    global rand
    rand = random.randint(1,2)
    
    os.system("clear")

    #keeps track of the players progress through the level. Used to prevent cheating.
    the_mighty_lion_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    the_mighty_lion_list[1] = input("You have chosen to hunt The Mighty Lion.\nYou have been on your journey for about a week now.\nThe trail splits off into three sections.\nDo you choose to go through the canyon?\nHow about the prairie?\nOr what about keep continuing through the forest?\n1- Canyon; 2- Prairie; 3- Forest\nMake your choice " + name + ":\n")

    if the_mighty_lion_list[1] == "1":
        os.system("clear")
        
        pause = input("You have chosen to go through the canyon!\nThe canyon is the quickest route to The Mighty Lion.\nUnfortunately, you're almost out of the canyon when a flash flood occurs.\nYou get wiped away instantly and you drown to death.\n" + death_level)

        volor_savanna_original()

    if the_mighty_lion_list[1] == "2":
        os.system(clear)

        the_mighty_lion_list[2] = input("You have chosen to go through the prairie!\nWhich way do you travel?\n1- Left; 2- Right\nMake your choice " + name + ":\n")

    if the_mighty_lion_list[1] == "3":
        os.system("clear")

        the_mighty_lion_list[3] = input("You have chosen to go through the forest!\nYou see a river.\nDo you drink from it?\n1- Yes; 2- No\nMake your choice " + name + ":\n")

    if the_mighty_lion_list[2] == "1":
        os.system("clear")

        pause = input("You have chosen to go left.\nUnfortunately, there are hyenas in front of you after only about an hour of walking.\nThey see you and kill you.\n" + death_level)

        volor_savanna_original()

    if the_mighty_lion_list[2] == "2":
        os.system("clear")

        the_mighty_lion_list[4] = input("You have chosen to go right.\nThere are zebras in front of you after only about an hour of walking.\nDo you kill them for food?\n1- Yes; 2- No\nMake your choice " + name + ":\n")

def the_mighty_lion_terrain():
    global rand
    rand = random.randint(1,2)
    
    os.system("clear")

    #keeps track of the players progress through the level. Used to prevent cheating.
    the_mighty_lion_terrain_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    the_mighty_lion_terrain_list[1] = input("You have chosen to drink from the river.\nLuckily, the water doesn't have any diseases or viruses.\nYou are full.\nYou need to cross the river.\nHowever, the river is very deep.\nYou could make a temporary bridge but that would kill vital time to hunt The Mighty Lion.\nThe fastest way to cross the river is to make a raft.\nWhat do you do?\n1- Make a bridge; 2- Build a raft\nMake your choice " + name + ":\n")


user_name()
