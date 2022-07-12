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
        fuel += number/3-2;
    }
    cout << fuel;
    return 0;
}