#include <iostream>
using namespace std;
extern "C"
{
    #include "VolorSavanna.h"
}

int main()
{
    cout << name_prompt;
    cin >> name;
    cout << character_prompt  << endl;
    cin >> character;
    return 0;
}
