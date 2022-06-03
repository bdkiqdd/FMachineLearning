#include <iostream>
using namespace std;

int main(){

    int num,*ptr;

    cout << "Type a number: ";
    cin >> num;

    cout << endl << "Value: " << num << endl;
    
    ptr = &num;

    cout << endl << "Pointer addres: " << ptr << endl;

    cout << endl << "Value by pointer: " << *ptr << endl;


    return 0;
}