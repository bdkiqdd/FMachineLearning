#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ofstream archOut("teste.txt");

    archOut << "Olá Mundo!";

    archOut.close();

    ifstream archIn("teste.txt");

    string lines;

    while (getline (archIn,lines))
    {
        cout << lines;
    }
    
    archIn.close();

    return 0;
}
