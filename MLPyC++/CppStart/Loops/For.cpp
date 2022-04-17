#include <iostream>
using namespace std;

int main(){

    for(int num = 10; num >= 1; --num)
        if (num % 2 == 1)
            cout << num << endl;    
        
    return 0;
}