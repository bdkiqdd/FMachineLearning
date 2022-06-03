#include <iostream>
using namespace std;

int main(){

    int A,*ptrA,B,*ptrB;

    cout << "Type the first number: ";
    cin >> A;

    cout << endl << "Type the second one: ";
    cin >> B;

    ptrA = &A;
    ptrB = &B;

    cout << "First Number: " << *ptrA << endl;
    cout << "Second one: " << *ptrB << endl;

    return 0;
}