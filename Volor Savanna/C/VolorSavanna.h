#include <cstring>

#ifndef VOLORSAVANNA_H
#define VOLORSAVANNA_H
char name[256];
string character;
int choice;
int level = 0;
string name_prompt = "What is your name?\n";
string character_prompt = "Welcome to Volor Savanna!\nYou are a member of an African Tribe!\nWho do you want to be?\n\n1- Hunter\n2- Warrior\n3- Crafter\n4- Farmer\n5- Medicine Person\ne- exit\n";

static inline const char * death_level(char * name)
{
    size_t length = strlen(name) + strlen(", YOU LOSE!\nTHE END!") + 1;
    char * result = (char *)malloc(length);
    strcpy(result, name);
    strcat(result, ", YOU LOSE!\nTHE END!");
    return result;
}

static inline const char * victory_level(char * name)
{
    size_t length = strlen(name) + strlen(", YOU WIN!\nTHE WIN!") + 1;
    char * result = (char *)malloc(length);
    strcpy(result, name);
    strcat(result, ", YOU WIN!\nTHE WIN!");
    return result;
}


static inline const char * VolorSavannaGame()
{       
    if (character == "1" && level == 0)
    {
        size_t length = strlen(name) + strlen("You have chosen to be a hunter!\nDo you want to go hunt or stay put?\n\n1- Hunt; 2- Stay put\nMake your choice ") + strlen(":\n") + 1;
        char * result = (char *)malloc(length);
        strcpy(result, "You have chosen to be a hunter!\nDo you want to go hunt or stay put?\n\n1- Hunt; 2- Stay put\nMake your choice ");
        strcat(result, name);
        strcat(result, ":\n");
        level = 1;
        return result;
    }
    
    else if (character == "1" && level == 1 && choice == 1)
    {
        size_t length = strlen(name) + strlen("You have chosen to go hunt!\nYou have gone hunting.\nYou didn't find any food.\nYou return to your village.\nLuckily, the farmer has enough crops to last your tribe a week.\nDo you want to go hunt right away to make up lost time or do you choose to go eat?\n\n1- Hunt; 2- Eat\nMake your choice ") + strlen(":\n") + 1;
        char * result = (char *)malloc(length);
        strcpy(result, "You have chosen to go hunt!\nYou have gone hunting.\nYou didn't find any food.\nYou return to your village.\nLuckily, the farmer has enough crops to last your tribe a week.\nDo you want to go hunt right away to make up lost time or do you choose to go eat?\n\n1- Hunt; 2- Eat\nMake your choice ");
        strcat(result, name);
        strcat(result, ":\n");
        level = 2;
        return result;
    }

    else if (character == "1" && level == 1 && choice == 2)
    {
        size_t length = strlen(name) + strlen("You have chosen to stay put.\nUnfortunately, your whole village parishes from hunger.\n") + strlen(death_level(name)) + 1;
        char * result = (char *)malloc(length);
        strcpy(result, "You have chosen to stay put.\nUnfortunately, your whole village parishes from hunger.\n");
        strcat(result, death_level(name));
        level = 0;
        return result;
    }

    else if (character == "1" && level == 2 && choice == 1)
    {
        size_t length = strlen(name) + strlen("You have chosen to go hunt!\nYou go on a successful hunt that should last your tribe a month.\nHowever, you are very tired and because you didn't eat, you have become very sick with malnutrition.\nUnluckily for you, the tribes medicine women is very busy and has a lot of patients to take care of first.\nDo you wish to wait for her or tough it out?\n\n1- Wait for her; 2- Tough it out\nMake your choice ") + strlen(":\n") + 1;
        char * result = (char *)malloc(length);
        strcpy(result, "You have chosen to go hunt!\nYou go on a successful hunt that should last your tribe a month.\nHowever, you are very tired and because you didn't eat, you have become very sick with malnutrition.\nUnluckily for you, the tribes medicine women is very busy and has a lot of patients to take care of first.\nDo you wish to wait for her or tough it out?\n\n1- Wait for her; 2- Tough it out\nMake your choice ");
        strcat(result, name);
        strcat(result, ":\n");
        level = 3;
        return result;
    }

    else if (character == "1" && level == 2 && choice == 2)
    {
        size_t length = strlen(name) + strlen("You have chosen to eat.\nYou are fully fueled with energy.\nDo you want to go hunting or play a game with the rest of your tribe?\n\n1- Hunt; 2- Play a game with the rest of my tribe\nMake your choice ") + strlen(":\n") + 1;
        char * result = (char *)malloc(length);
        strcpy(result, "You have chosen to eat.\nYou are fully fueled with energy.\nDo you want to go hunting or play a game with the rest of your tribe?\n\n1- Hunt; 2- Play a game with the rest of my tribe\nMake your choice ");
        strcat(result, name);
        strcat(result, ":\n");
        level = 4;
        return result;
    }

    else if (character == "1" && level == 3 && choice == 1)
    {
        size_t length = strlen(name) + strlen("You have chosen to wait for her.\nBecause You have chosen to wait for her patiently, she attends to you in a matter of a couple days.\nYou are better in a week.\nSome white men have come to your tribe.\nThey're asking to trade you guns for some of your tribe's animal pelts.\nDo you trade them pelts for guns?\n\n1- Trade; 2- Not trade\nMake your choice ") + strlen(":\n") + 1;
        char * result = (char *)malloc(length);
        strcpy(result,  "You have chosen to wait for her.\nBecause You have chosen to wait for her patiently, she attends to you in a matter of a couple days.\nYou are better in a week.\nSome white men have come to your tribe.\nThey're asking to trade you guns for some of your tribe's animal pelts.\nDo you trade them pelts for guns?\n\n1- Trade; 2- Not trade\nMake your choice ");
        strcat(result, name);
        strcat(result, ":\n");
        level = 5;
        return result;
    }

    else if (character == "1" && level == 3 && choice == 2)
    {
        size_t length = strlen(name) + strlen("You have chosen to tough it out.\nUnfortunately, because of this, you die from malnutrition.\n") + strlen(death_level(name)) + 1;
        char * result = (char *)malloc(length);
        strcpy(result, "You have chosen to tough it out.\nUnfortunately, because of this, you die from malnutrition.\n");
        strcat(result, death_level(name));
        level = 0;
        return result;
    }

    else if (character == "1" && level == 4 && choice == 1)
    {
        size_t length = strlen(name) + strlen("You have chosen to hunt.\nYou have found a bunch of zebras to eat.\nSome white men are willing to trade your tribe rifles for some of your zebras.\nRecently, there has been some highly wanted criminals that trade weapons and drugs on the black market.\nThe problem is, you don't know if that's them.\nDo you trade?\nWhat about decline the offer?\nOr do you report them to the authorities?\n\n1- Trade; 2- Decline the trade; 3- Report them to the authorities\nMake your choice ") + strlen(":\n") + 1;
        char * result = (char *)malloc(length);
        strcpy(result,  "You have chosen to hunt.\nYou have found a bunch of zebras to eat.\nSome white men are willing to trade your tribe rifles for some of your zebras.\nRecently, there has been some highly wanted criminals that trade weapons and drugs on the black market.\nThe problem is, you don't know if that's them.\nDo you trade?\nWhat about decline the offer?\nOr do you report them to the authorities?\n\n1- Trade; 2- Decline the trade; 3- Report them to the authorities\nMake your choice ");
        strcat(result, name);
        strcat(result, ":\n");
        level = 6;
        return result;
    }

    else if (character == "1" && level == 4 && choice == 2)
    {
        size_t length = strlen(name) + strlen("You have chosen to play a game with the rest of your tribe.\nEveryone has a good time and you guys have an awesome feast.\nThere is a hunting challenge that your tribe is having.\nThe challenge is to go hunt The Mighty Lion!\nDo you want to go hunt The Mighty Lion with your tribe to win the challenge?\n\n1- Yes; 2- No\nMake your choice ") + strlen(":\n") + 1;
        char * result = (char *)malloc(length);
        strcpy(result, "You have chosen to play a game with the rest of your tribe.\nEveryone has a good time and you guys have an awesome feast.\nThere is a hunting challenge that your tribe is having.\nThe challenge is to go hunt The Mighty Lion!\nDo you want to go hunt The Mighty Lion with your tribe to win the challenge?\n\n1- Yes; 2- No\nMake your choice ");
        strcat(result, name);
        strcat(result, ":\n");
        level = 7;
        return result;
    }

    else if (character == "1" && level == 5 && choice == 1)
    {
        size_t length = strlen(name) + strlen("You have chosen to trade.\nThey trade you guns.\nDo you want to go hunt The Mighty Lion?\n\n1- Yes; 2- No\nMake your choice ") + strlen(":\n") + 1;
        char * result = (char *)malloc(length);
        strcpy(result, "You have chosen to trade.\nThey trade you guns.\nDo you want to go hunt The Mighty Lion?\n\n1- Yes; 2- No\nMake your choice ");
        strcat(result, name);
        strcat(result, ":\n");
        level = 8;
        return result;
    }

    else if (character == "1" && level == 5 && choice == 2)
    {
        size_t length = strlen(name) + strlen("You have chosen not to trade.\nBecause of this they want to kill you.\nDo you escape?\n\n1- Find out!\nMake your choice ") + strlen(":\n") + 1;
        char * result = (char *)malloc(length);
        strcpy(result, "You have chosen not to trade.\nBecause of this they want to kill you.\nDo you escape?\n\n1- Find out!\nMake your choice ");
        strcat(result, name);
        strcat(result, ":\n");
        level = 9;
        return result;
    }

    else if (character == "1" && level == 6 && choice == 1)
    {
        size_t length = strlen(name) + strlen("You have chosen to trade.\nLuckily, these aren't the criminals that are wanted.\nA couple months later the white men settle here.\nPeople keep on flooding into the white men's settlement.\nBecause of this your village becomes rich.\n") + strlen(victory_level(name)) + 1;
        char * result = (char *)malloc(length);
        strcpy(result, "You have chosen to trade.\nLuckily, these aren't the criminals that are wanted.\nA couple months later the white men settle here.\nPeople keep on flooding into the white men's settlement.\nBecause of this your village becomes rich.\n");
        strcat(result, victory_level(name));
        level = 0;
        return result;
    }

    else if (character == "1" && level == 6 && choice == 2)
    {
        size_t length = strlen(name) + strlen("You have chosen to decline the trade.\nUnfortunately, these people have smallpox.\nThey transmit it to your tribe.\nBecause you tribe doesn't have any immunity against smallpox your whole tribe dies!\n") + strlen(death_level(name)) + 1;
        char * result = (char *)malloc(length);
        strcpy(result, "You have chosen to decline the trade.\nUnfortunately, these people have smallpox.\nThey transmit it to your tribe.\nBecause you tribe doesn't have any immunity against smallpox your whole tribe dies!\n");
        strcat(result, death_level(name));
        level = 0;
        return result;
    }

    else if (character == "1" && level == 6 && choice == 3)
    {
        size_t length = strlen(name) + strlen("You have chosen to report them to the authorities.\nThese guys turn out to be the wanted criminals after all.\nYour tribe gains importance in the African community because you turned these criminals into the authorities.\nDo you want to go hunt The Mighty Lion?\n\n1- Yes; 2- No\nMake your choice ") + strlen(":\n") + 1;
        char * result = (char *)malloc(length);
        strcpy(result, "You have chosen to report them to the authorities.\nThese guys turn out to be the wanted criminals after all.\nYour tribe gains importance in the African community because you turned these criminals into the authorities.\nDo you want to go hunt The Mighty Lion?\n\n1- Yes; 2- No\nMake your choice ");
        strcat(result, name);
        strcat(result, ":\n");
        level = 10;
        return result;
    }
   
    else
    {
        return 0;
    }
}
#endif
