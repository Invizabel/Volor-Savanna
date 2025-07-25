#include <cstring>

#ifndef VOLORSAVANNA_H
#define VOLORSAVANNA_H
char name[256];
int character;
string name_prompt = "What is your name?\n";
string character_prompt = "Welcome to Volor Savanna!\nYou are a member of an African Tribe!\nWho do you want to be?\n\n1- Hunter\n2- Warrior\n3- Crafter\n4- Farmer\n5- Medicine Person\ne- exit\n";

static inline const char * death_level(char * username)
{
    size_t length = strlen(username) + strlen(", YOU LOSE!\nTHE END!") + 1;
    char * result = (char *)malloc(length);
    strcpy(result, username);
    strcat(result, ", YOU LOSE!\nTHE END!");
    return result;
}

static inline const char * victory_level(char * username)
{
    size_t length = strlen(username) + strlen(", YOU LOSE!\nTHE WIN!") + 1;
    char * result = (char *)malloc(length);
    strcpy(result, username);
    strcat(result, ", YOU LOSE!\nTHE WIN!");
    return result;
}

static inline const char * warrior(int index)
{
    if (index == 1)
    {
        return "ABC";
    }

    else if (index == 2)
    {
        return "XYZ";
    }

    else
    {
        return 0;
    }
}
#endif
