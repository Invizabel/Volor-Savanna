#include <iostream>
#include <string.h>

using namespace std;
extern "C"
{
    #include "VolorSavanna.h"
}

int main()
{
    string pause;
    cout << name_prompt;
    cin >> name;
    
    while (true)
    {
        cout << character_prompt << endl;
        cin >> character;
        if (character == "e")
        {
            return 0;
        }

        else
        {
            while (true)
            {
                cout << VolorSavannaGame() << endl;
                if (level == 0)
                {
                    cin >> pause;
                    break;
                }
                cin >> choice;
            }

        }
    }
    
    return 0;
}
