#include <iostream>
using namespace std;

int main(){
    char choice;
    int n1,n2;

    cout << "*********************************************" << endl;
    cout << "------- Welcome to my Calculator!! ----------" << endl;

    cout << "Type two numbers no calculate!" << endl;
    cout << "Number one: ";
    cin >> n1;
    cout << "Seconde one: ";
    cin >> n2;
    cout << endl; 

    cout << "Choice a operation below" << endl;
    cout << "1 - Addition" << endl;
    cout << "2 - Subtraction" << endl;
    cout << "3 - Division" << endl;
    cout << "4 - Multiplication" << endl;

    cin >> choice;

    switch (choice)
    {
    case '1':
        cout << "Result: " << n1 + n2 << endl;
        break;
    case '2':
        cout << "Result: " << n1 - n2 << endl;
        break;
    case '3':
        if (n2 == 0){
            cerr << "Can't devid by zero!" << endl;
            break;
        }else{
            cout << "Result: " << n1 / n2 << endl;
            break;
        }        
    case '4':
        cout << "Result: " << n1 * n2 << endl;
        break;
    default:
        cout << "We haven't this option!" << endl;
        break;
    }

    cout << "Thanks for using!";
    return 0;
}