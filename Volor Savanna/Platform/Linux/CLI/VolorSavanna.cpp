#include <iostream>
using namespace std;
extern "C"
{
    #include "VolorSavanna.h"
}

int main()
{
    while (true)
    {
        cout << name_prompt;
        cin >> name;
        cout << character_prompt;
        cin >> character;
        if (character == "e")
        {
            return 0;
        }

        else
        {
            while (true)
            {
                cout << VolorSavannaGame();
                cin >> choice;
                if (level == 0)
                {
                    break;
                }
            }

        }
    }
    
    return 0;
}
