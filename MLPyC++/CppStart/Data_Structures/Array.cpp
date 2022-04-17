#include <iostream>
using namespace std;

int main(){

    int lista[5];

    for (int i = 0; i < 5; i++)
    {
        lista[i] = i + 1;
    }
    cout << "Testing array" << endl;
    cout << lista[2] << endl;
    cout << "-------------------------" << endl;

    cout << "Printing array" << endl;
    for (int i = 0; i < 5; i++){
        cout << lista[i] << endl;
    }
    
    return 0;
}