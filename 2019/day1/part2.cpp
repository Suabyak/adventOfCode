#include <iostream>
#include <sstream>
#include <fstream>
#include <stdlib.h>
using namespace std;

int main()
{
    string line;
    stringstream stream;
    ifstream input("input.in");
    int fuel = 0,  number = 0;
    

    while(getline(input, line))
    {
        number = atoi(line.c_str());
        do
        {
            number = number / 3 - 2;
            fuel += number;
        } while (number > 0);
        if (number < 0) fuel -= number;
    }
    cout << fuel;
    return 0;
}