#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>
using namespace std;

int main()
{
    string line;
    ifstream input("input.in");
    getline(input, line);
    int number = 0, fields = 1;
    char c;
    for (int i = 0; i < strlen(line.c_str()); i++)
    {  
        c = line[i];
        if (c == ',') fields++;
    }
    int field[fields];
    fields = 0;
    field[0] = 0;
    for (int i = 0; i < strlen(line.c_str()); i++)
    {
        c = line[i];
        if (c == ',')
        {
            fields++;
            field[fields] = 0;
        }
        else if(c != ' ')
        {
            field[fields] *= 10;
            field[fields] += (c - '0');
        }
    }
    int i = 0;
    do
    {
        if (field[i*4] == 1)
            field[field[i * 4 + 3]] = field[field[i * 4 + 1]] + field[field[i * 4 + 2]];
        else if (field[i*4] == 2)
            field[field[i * 4 + 3]] = field[field[i * 4 + 1]] * field[field[i * 4 + 2]];
        i++;
    } while (field[i*4] != 99);

    cout << field[0] << endl;
    return 0;
}