#include <iostream>
#include <fstream>
using namespace std;

int main(){

    fstream f;

    f.open("text.txt",fstream::out);
    
    f.close();

    return 0;
}