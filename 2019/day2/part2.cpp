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
    int x = 0, y = 0;
    do
    {

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
            else if (c != ' ')
            {
                field[fields] *= 10;
                field[fields] += (c - '0');
            }
        }
        field[1] = x;
        field[2] = y++;
        if (y==100)
        {
            x++;
            y=0;
        }
        int i = 0;
        do
        {
            if (field[i*4] == 1)
                field[field[i * 4 + 3]] = field[field[i * 4 + 1]] + field[field[i * 4 + 2]];
            else if (field[i*4] == 2)
                field[field[i * 4 + 3]] = field[field[i * 4 + 1]] * field[field[i * 4 + 2]];
            i++;
        } while (field[i * 4] != 99);
    } while (field[0] != 19690720);
    cout << 100*field[1]+field[2] << endl;
    return 0;
}